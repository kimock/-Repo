"""
STEP 1: CSV 매핑 모듈  (v3 — 3-레이어 분류)

분류 파이프라인:
  Layer 1 (결정론적) : remarks가 명확한 카테고리 → 고정 맵으로 직결, ML 스킵
  Layer 2 (ML)       : remarks가 모호(falling/dropping)인 경우 → 임베딩 유사도 분류
  Layer 3 (충돌 해결): Layer 2 결과의 SDN-Hanmi 의미 충돌 → Hanmi 기준으로 SDN 보정

개선 내역 (v3):
  [Layer 1] remarks 결정론적 매핑 — explosion→폭발, collapse→붕괴 등 ML 오분류 방지
  [Layer 2] remarks가 모호할 때만 ML 실행 — 불필요한 모델 호출 제거
  [Layer 3] SDN-Hanmi 비호환 쌍 감지 후 Hanmi 우선 보정 (Hanmi 기준 역매핑)

기존 개선 내역 (v2 유지):
  [수정1] 앵커 텍스트 중복 단어 제거
  [수정2] remarks 별도 임베딩 후 가중 평균
  [수정3] 유사도 임계값 0.25 + remarks 직접 매핑 fallback
"""

import os
import pandas as pd
import numpy as np
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# ── 분류 레이블 ──────────────────────────────────────────────
SDN_LABELS = [
    "떨어짐/낙상", "전도/낙하/부딪힘", "끼임",
    "감전/합선", "화재/탄화", "LEAK", "기타"
]

HANMI_LABELS = [
    "추락", "낙하", "비래", "전도", "협착",
    "충돌", "감전", "화재", "폭발", "붕괴", "기타"
]

# ── 앵커 텍스트 ──────────────────────────────────────────────
SDN_ANCHORS = {
    "떨어짐/낙상":     "worker fell off edge scaffold ladder platform height slip trip lost footing",
    "전도/낙하/부딪힘": "object dropped toppled overturned struck tipped unstable material descended collision",
    "끼임":           "caught entangled pinched squeezed trapped between machinery rotating body part crush",
    "감전/합선":       "electric shock electrocution short circuit live wire cable insulation current",
    "화재/탄화":       "fire flame ignition combustion burn scorch smoke extinguisher fire hydrant",
    "LEAK":           "leak leakage spill chemical fluid oil dripping overflow",
    "기타":           "housekeeping storage documentation administrative PPE training expired tag",
}

HANMI_ANCHORS = {
    "추락":  "worker fell off edge platform scaffold ladder height plunged dropped elevation",
    "낙하":  "object tool material fell descended from above dropped overhead struck below",
    "비래":  "flying projectile fragment debris airborne scattered thrown object",
    "전도":  "overturning tipping toppled equipment vehicle rolled unstable tipped over",
    "협착":  "caught pinched crushed trapped squeezed between machinery body rotating",
    "충돌":  "struck collision impact bumped hit vehicle equipment swinging moving",
    "감전":  "electric shock electrocution live wire cable current insulation",
    "화재":  "fire flame ignition combustion burn scorch smoke heat",
    "폭발":  "explosion blast pressure gas cylinder detonation ignited",
    "붕괴":  "collapse structural failure scaffold toppled wall fell apart cave",
    "기타":  "housekeeping storage documentation PPE training expired administrative",
}

# ════════════════════════════════════════════════════════════
# Layer 1 — remarks 결정론적 매핑
# ════════════════════════════════════════════════════════════
# remarks 값이 명확한 카테고리를 가리킬 때 ML 없이 고정 레이블로 직결.
# (SDN_label, Hanmi_label) 튜플.
# "falling" / "dropping" 은 사람 추락 vs 물체 낙하 구분이 필요 → ML 처리.
REMARKS_DETERMINISTIC: dict[str, tuple[str, str]] = {
    "explosion":        ("화재/탄화",       "폭발"),
    "fire":             ("화재/탄화",       "화재"),
    "electric shock":   ("감전/합선",       "감전"),
    "entrapment":       ("끼임",           "협착"),
    "overturning":      ("전도/낙하/부딪힘", "전도"),
    "flying objection": ("전도/낙하/부딪힘", "비래"),
    "impact":           ("전도/낙하/부딪힘", "충돌"),
    "collapse":         ("전도/낙하/부딪힘", "붕괴"),
    "others":           ("기타",            "기타"),
}

# ════════════════════════════════════════════════════════════
# Layer 3 — SDN-Hanmi 호환 쌍 & Hanmi → SDN 역매핑
# ════════════════════════════════════════════════════════════
# 각 SDN 레이블에서 의미상 허용 가능한 Hanmi 레이블 집합.
# 이 집합에 없는 Hanmi 결과가 나오면 충돌로 간주.
COMPATIBLE: dict[str, set[str]] = {
    "떨어짐/낙상":     {"추락", "낙하"},
    "전도/낙하/부딪힘": {"추락", "낙하", "충돌", "전도", "비래", "붕괴"},
    "끼임":           {"협착", "충돌"},
    "감전/합선":       {"감전"},
    "화재/탄화":       {"화재", "폭발"},
    "LEAK":           {"기타"},         # 한미 체계에 LEAK 없음 → 기타만 허용
    "기타":           {"기타"},
}

# Hanmi 레이블 → SDN 레이블 역매핑 (충돌 해결 시 Hanmi 기준으로 SDN 보정)
HANMI_TO_SDN: dict[str, str] = {
    "추락": "떨어짐/낙상",
    "낙하": "전도/낙하/부딪힘",
    "비래": "전도/낙하/부딪힘",
    "전도": "전도/낙하/부딪힘",
    "협착": "끼임",
    "충돌": "전도/낙하/부딪힘",
    "감전": "감전/합선",
    "화재": "화재/탄화",
    "폭발": "화재/탄화",
    "붕괴": "전도/낙하/부딪힘",
    "기타": "기타",
}

# ── Layer 2 fallback (ML 임계값 미달 시) ─────────────────────
REMARKS_FALLBACK_SDN = {
    "falling":          "떨어짐/낙상",
    "dropping":         "전도/낙하/부딪힘",
    "impact":           "전도/낙하/부딪힘",
    "overturning":      "전도/낙하/부딪힘",
    "flying objection": "전도/낙하/부딪힘",
    "collapse":         "전도/낙하/부딪힘",
    "entrapment":       "끼임",
    "electric shock":   "감전/합선",
    "fire":             "화재/탄화",
    "explosion":        "화재/탄화",
    "others":           "기타",
}

REMARKS_FALLBACK_HANMI = {
    "falling":          "추락",
    "dropping":         "낙하",
    "flying objection": "비래",
    "overturning":      "전도",
    "collapse":         "붕괴",
    "entrapment":       "협착",
    "impact":           "충돌",
    "electric shock":   "감전",
    "fire":             "화재",
    "explosion":        "폭발",
    "others":           "기타",
}

# ── 파라미터 ─────────────────────────────────────────────────
SIMILARITY_THRESHOLD  = 0.25
TOP_N_KEYWORDS        = 8
NGRAM_RANGE           = (2, 3)
REMARKS_WEIGHT        = 0.45   # remarks 임베딩 가중치 (keyword: 0.55)
CONFLICT_TOLERANCE    = 0.90   # Hanmi score >= SDN score × 이 값이면 Hanmi 우선


# ── Vendor 정규화 ────────────────────────────────────────────
VENDOR_NORMALIZE = {
    "dshi":      "DSHI",
    "hankuk":    "Hankuk",
    "daemyoung": "Daemyoung",
    "halim":     "Halim",
    "kosca":     "Kosca",
    "rtcc":      "RTCC",
    "samho":     "Samho",
}

def normalize_vendor(name: str) -> str:
    cleaned = name.strip().lower()
    return VENDOR_NORMALIZE.get(cleaned, name.strip().title())


# ── 모델 로드 ────────────────────────────────────────────────
def _load_models(model_name: str = "all-MiniLM-L6-v2"):
    print(f"  · 모델 로드 중: {model_name}")
    st_model = SentenceTransformer(model_name)
    kb_model = KeyBERT(model=st_model)
    return kb_model, st_model


def _encode_anchors(st_model, anchors: dict):
    labels     = list(anchors.keys())
    embeddings = st_model.encode(list(anchors.values()), normalize_embeddings=True)
    return labels, embeddings


# ── Layer 2: ML 분류 함수 ────────────────────────────────────
def _classify_ml(
    raw_content:      str,
    remarks:          str,
    kb_model:         KeyBERT,
    st_model:         SentenceTransformer,
    labels:           list,
    label_embs:       np.ndarray,
    fallback_map:     dict,
    fallback_default: str = "기타",
) -> tuple[str, float]:
    """임베딩 유사도 기반 단일 행 분류. Returns (label, score)."""
    raw     = raw_content.strip() if isinstance(raw_content, str) else ""
    remarks = remarks.strip()     if isinstance(remarks, str)     else ""

    if not raw and not remarks:
        return fallback_default, 0.0

    # remarks 직접 임베딩
    remarks_emb = None
    if remarks:
        remarks_emb = st_model.encode([remarks], normalize_embeddings=True)

    # KeyBERT 키워드 추출
    kw_text = raw
    if raw:
        keywords = kb_model.extract_keywords(
            f"{raw} {remarks}".strip(),
            keyphrase_ngram_range=NGRAM_RANGE,
            stop_words="english",
            top_n=TOP_N_KEYWORDS,
            use_mmr=True,
            diversity=0.5,
        )
        if keywords:
            kw_text = " ".join([kw for kw, _ in keywords])

    kw_emb = st_model.encode([kw_text], normalize_embeddings=True)

    # 가중 평균 임베딩
    if remarks_emb is not None:
        combined = (1 - REMARKS_WEIGHT) * kw_emb + REMARKS_WEIGHT * remarks_emb
        norm     = np.linalg.norm(combined, axis=1, keepdims=True)
        combined = combined / np.where(norm == 0, 1, norm)
    else:
        combined = kw_emb

    # 코사인 유사도
    sims       = cosine_similarity(combined, label_embs)[0]
    best_idx   = int(np.argmax(sims))
    best_score = float(sims[best_idx])

    # 임계값 미달 → remarks fallback
    if best_score < SIMILARITY_THRESHOLD:
        return fallback_map.get(remarks.lower(), fallback_default), best_score

    return labels[best_idx], best_score


# ── 메인 실행 ────────────────────────────────────────────────
def run(
    input_path:  str = "data.csv",
    output_path: str = "new_CSV.csv",
    model_name:  str = "all-MiniLM-L6-v2",
) -> pd.DataFrame:
    base_dir    = os.path.dirname(os.path.abspath(__file__))
    input_file  = input_path  if os.path.isabs(input_path)  else os.path.join(base_dir, input_path)
    output_file = output_path if os.path.isabs(output_path) else os.path.join(base_dir, output_path)

    print("[STEP 1] CSV 매핑 시작 (v3 — 3-레이어 분류)")
    print(f"  · 입력: {input_file}")

    df = pd.read_csv(input_file, encoding="utf-8")
    total = len(df)
    print(f"  · 원본 데이터: {total}건\n")

    df["date"]    = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
    df["vendor"]  = df["vendor"].fillna("").apply(normalize_vendor)
    df["remarks"] = df["remarks"].fillna("").str.strip()

    # ML이 필요한 행만 모델 로드
    ml_needed = df["remarks"].str.strip().str.lower().apply(
        lambda r: r not in REMARKS_DETERMINISTIC
    )
    ml_count = ml_needed.sum()
    det_count = total - ml_count
    print(f"  · Layer 1 (결정론적) 대상: {det_count}건")
    print(f"  · Layer 2 (ML)       대상: {ml_count}건")

    kb_model, st_model = None, None
    sdn_labels = sdn_emb = hanmi_labels = hanmi_emb = None

    if ml_count > 0:
        kb_model, st_model = _load_models(model_name)
        sdn_labels,   sdn_emb   = _encode_anchors(st_model, SDN_ANCHORS)
        hanmi_labels, hanmi_emb = _encode_anchors(st_model, HANMI_ANCHORS)
        print(f"  · 레이블 임베딩 완료 (SDN {len(sdn_labels)}개 / Hanmi {len(hanmi_labels)}개)")
        print(f"  · 유사도 임계값: {SIMILARITY_THRESHOLD}  remarks 가중치: {REMARKS_WEIGHT}")

    print(f"\n  · 분류 진행 중...")
    sdn_results, hanmi_results     = [], []
    sdn_scores,  hanmi_scores      = [], []
    method_log                     = []   # "det" | "ml" | "ml+resolved"
    conflict_count = ml_fallback_count = 0

    for idx, row in df.iterrows():
        raw        = str(row.get("raw_content", ""))
        remarks_raw = str(row.get("remarks", "")).strip()
        remarks_key = remarks_raw.lower()

        # ── Layer 1: 결정론적 매핑 ──────────────────────────
        if remarks_key in REMARKS_DETERMINISTIC:
            sdn_lbl, hanmi_lbl = REMARKS_DETERMINISTIC[remarks_key]
            sdn_sc  = hanmi_sc = 1.0
            method  = "det"

        else:
            # ── Layer 2: ML 분류 ─────────────────────────────
            sdn_lbl, sdn_sc = _classify_ml(
                raw, remarks_raw, kb_model, st_model,
                sdn_labels, sdn_emb, REMARKS_FALLBACK_SDN, "기타"
            )
            hanmi_lbl, hanmi_sc = _classify_ml(
                raw, remarks_raw, kb_model, st_model,
                hanmi_labels, hanmi_emb, REMARKS_FALLBACK_HANMI, "기타"
            )

            if sdn_sc < SIMILARITY_THRESHOLD or hanmi_sc < SIMILARITY_THRESHOLD:
                ml_fallback_count += 1

            method = "ml"

            # ── Layer 3: 충돌 감지 → Hanmi 기준 SDN 보정 ────
            if hanmi_lbl not in COMPATIBLE.get(sdn_lbl, set()):
                conflict_count += 1
                # Hanmi 점수가 SDN 점수의 CONFLICT_TOLERANCE 이상이면 Hanmi 우선
                if hanmi_sc >= sdn_sc * CONFLICT_TOLERANCE:
                    sdn_lbl = HANMI_TO_SDN.get(hanmi_lbl, "기타")
                    method  = "ml+resolved"

        sdn_results.append(sdn_lbl)
        hanmi_results.append(hanmi_lbl)
        sdn_scores.append(round(sdn_sc, 4))
        hanmi_scores.append(round(hanmi_sc, 4))
        method_log.append(method)

        n = idx + 1
        if n % 50 == 0:
            print(f"    {n}/{total} 완료...")

    df["SDN_risk"]    = sdn_results
    df["Hanmi_risk"]  = hanmi_results
    df["SDN_score"]   = sdn_scores
    df["Hanmi_score"] = hanmi_scores
    df["_method"]     = method_log   # 검증용 (저장 시 제거)

    # ── 결과 요약 ────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"  분류 완료 — {total}건")
    print(f"  · Layer 1 (결정론적):  {method_log.count('det')}건")
    print(f"  · Layer 2 (ML 정상):   {method_log.count('ml')}건")
    print(f"  · Layer 3 (충돌 보정): {method_log.count('ml+resolved')}건")
    print(f"  · ML fallback 적용:    {ml_fallback_count}건")
    print(f"{'='*50}")

    print(f"\n  · SDN_risk 분포:")
    for label, cnt in df["SDN_risk"].value_counts().items():
        print(f"    - {label}: {cnt}건")

    print(f"\n  · Hanmi_risk 분포:")
    for label, cnt in df["Hanmi_risk"].value_counts().items():
        print(f"    - {label}: {cnt}건")

    if ml_count > 0:
        ml_mask = df["_method"].isin(["ml", "ml+resolved"])
        avg_sdn   = float(df.loc[ml_mask, "SDN_score"].mean())
        avg_hanmi = float(df.loc[ml_mask, "Hanmi_score"].mean())
        print(f"\n  · ML 평균 유사도  SDN: {avg_sdn:.4f} / Hanmi: {avg_hanmi:.4f}")

    # ── 저장 ─────────────────────────────────────────────────
    df_save = df.drop(columns=["_method"]).copy()
    df_save["date"] = df_save["date"].dt.strftime("%d.%m.%Y")
    df_save.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"\n[STEP 1] 완료 → {output_file} ({total}건 저장)")

    return df


if __name__ == "__main__":
    run()
