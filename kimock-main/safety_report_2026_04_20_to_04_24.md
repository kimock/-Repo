# 주간 안전점검 분석 리포트
## 분석 기간: 2026-04-20 ~ 2026-04-24

> **생성일**: 2026-04-29 | **분석 엔진**: Claude Code (claude-sonnet-4-6)
> **데이터 출처**: llm_context.md (Python 사전계산, 55건) · 전주 비교: llm_context_20260417.md (47건)

---

## ⚡ 이번 주 핵심 메시지

> 전주(47건) 대비 총 위반 건수가 **▲8건(+17%)** 증가한 55건을 기록하며 Module 2F로 작업 중심이 급격히 이동(▲17건)했다. 클러스터 분석 결과 전체 55건의 **25.5%(14건)가 "작업자 안전장구 고정·체결" 단일 패턴**으로 집약됐으며, 이는 Vendor 구분 없이 현장 전반의 추락방호 문화 결핍을 시사한다. `scissor lift`(▲3)·`just near`(▲3) 등 DSHI 장비 운용 위반은 2주 연속 급증 중이며, 행동적 위반(`unsafe manner` 4건·미완료)은 소급 Close-Out 대신 **작업자 의식교육으로 즉시 전환**한다.

---

## 1. 📊 핵심 지표 요약 (Executive Summary)

- **분석 기간**: 2026-04-20 ~ 2026-04-24 (데이터 집계, 섹션 1)
- **총 안전위반**: 55건 (전주 47건 → **▲8건 +17%**)
- **조치 완료**: 41건 / 완료율 **74.5%** (전주 70.2% → ▲4.3%p)
- **미완료 Open 항목**: **14건** (Hankuk 9건 · DSHI 5건)
- **최다 위험유형(SDN)**: 전도/낙하/부딪힘 27건 (49.1%)
- **최다 위험유형(한미)**: 추락 15건 (27.3%)

| Vendor | 건수 | 비중 | 전주 대비 | 핵심 Safety Phrase |
|--------|------|------|-----------|-------------------|
| Hankuk | 28건 | 50.9% | ▲3 | safety harness, near edge, green net |
| DSHI | 26건 | 47.3% | ▲4 | scissor lift, just near, earthing connection |
| Daemyoung | 1건 | 1.8% | ▲1 (신규) | open shear studs (⚠️ 소표본) |

**주목 포인트**: Module 1F 중심(전주 27건)에서 **Module 2F로 작업 무게중심 급전환(31건, 56.4%)**. Hankuk·DSHI 양사 동반 증가로 특정 업체 문제가 아닌 **현장 전반 관리 공백** 신호. (데이터 집계, 섹션 2·5·11)

---

## 2. 📈 주간 트렌드 분석

이번 주 55건은 전주(47건) 대비 **▲8건(+17%) 증가**했다. (데이터 집계, 섹션 7·12)

### 전주 대비 위험 지형 변화

| 지표 | 이번 주 | 전주 | 증감 | 해석 |
|------|---------|------|------|------|
| 총 발생 건수 | 55건 | 47건 | **▲8** | 전반적 관리 이완 |
| Module 2F | 31건 | 14건 | **▲17** | 신규 작업 구역 초기 안전 공백 |
| Module 1F | 20건 | 27건 | ▼7 | 작업 감소 또는 관리 개선 |
| Module GF | 4건 | 6건 | ▼2 | 소폭 감소 |
| 감전/합선 | 2건 | 8건 | **▼6** | 전주 지적 후 조치 효과 |
| 끼임(협착) | 6건 | 2건 | **▲4** | 설치·조립 공정 증가 |
| 전도/낙하/부딪힘 | 27건 | 21건 | **▲6** | Module 2F 고소작업 밀도 상승 |
| 붕괴 (한미 기준) | 11건 | 6건 | **▲5** | 비계·구조물 관련 급증 |
| 화재/탄화 | 5건 | 3건 | ▲2 | 화기 작업 통제 미흡 지속 |
| 조치 완료율 | 74.5% | 70.2% | ▲4.3%p | 완만한 개선세 유지 |

**해석:**
- **Module 2F 급증(▲17, +121%)**: 1F에서 2F로 Work Band 이동 초기, 가시설 및 추락방호 장치 선행 설치 없이 본작업이 투입된 것으로 판단. (추정)
- **감전/합선 ▼6**: 전주 earthing connection 지적 이후 DSHI 측 부분 조치 효과. 단 이번 주에도 earthing connection 2건 반복 — 완전 해소 아님. (추정)
- **끼임·협착 ▲4, 붕괴 ▲5**: Module 2F 조립·설치 공정 밀도 증가와 연동된 기계적·구조적 위험 동반 상승. (추정)

---

### 🔁 반복 위험 패턴 (2주 이상 연속, 섹션 13)

> `unsafe manner`·`just near`·`name tag` 등 **행동적 위반**은 작업 완료 후 소급 Close-Out 불가 — 후속 조치는 작업자 의식교육 및 행동 감독 강화로 즉시 전환.

| Safety Phrase | 이번 주 | 전주 | 증감 | 유형 |
|---|---|---|---|---|
| **unsafe manner** | 4건 | 4건 | ─ | 행동적 위반 (교육 대상) |
| **safety harness** | 4건 | 3건 | ▲1 | 장비 미착용 (물리적 조치 가능) |
| **scissor lift** | 4건 | 1건 | **▲3 급증** | 장비 운용 절차 위반 |
| **just near** | 4건 | 1건 | **▲3 급증** | 근접 위험 (행동적) |
| near edge | 3건 | 2건 | ▲1 | 단부 근접 (구조적 보완 가능) |
| earthing connection | 2건 | 2건 | ─ | 물리적 결함 (조치 가능) |
| lifeline rope | 2건 | 2건 | ─ | 물리적 결함 (조치 가능) |
| green net | 2건 | 2건 | ─ | 구조적 결함 (조치 가능) |
| mid railing | 2건 | 2건 | ─ | 구조적 결함 (조치 가능) |
| web slings | 2건 | 2건 | ─ | 장비 불량 (조치 가능) |

> **`unsafe manner` 4건은 섹션 14(미완료) 주요 Phrase로 확인**. 행동적 순간 위반으로 소급 Close-Out 사실상 불가 — 해당 작업자 개별 Toolbox Meeting 및 재발 방지 서약으로 후속조치 대체 완결.

---

## 3. 🔑 Vendor × Location 심층 분석

### Hankuk — 28건 (50.9%) · 섹션 6·9 인용

> 교차집계: 전도/낙하/부딪힘 15건, 떨어짐/낙상 7건, 끼임 3건, 기타 2건, 화재/탄화 1건 (데이터 집계, 섹션 6)

| 순위 | Safety Phrase | 빈도수 | 의미 해석 |
|------|---------------|--------|-----------|
| 1 | safety harness | 4건 | 안전대(추락방호구) 미착용 또는 불완전 체결 |
| 2 | near edge | 2건 | 단부·개구부 근접 작업 중 추락방지 조치 미흡 |
| 3 | green net | 2건 | 낙하방지망(Green Safety Net) 미설치 또는 훼손 |
| 4 | unsafe manner | 2건 | 불안전 행동 — 행동적 위반, 교육 대상 ⚠️ |
| 5 | web slings | 2건 | 리깅 작업 중 불량 슬링 사용 ⚠️ |
| 6 | safe access | 2건 | 작업 구역 안전 통로 미확보 ⚠️ |

**위험 집중 Location**: Module 2F (데이터 집계, 섹션 5·6)
- **떨어짐/낙상 7건 = 전체 9건의 77.8%가 Hankuk** 발생 — 추락 리스크 극도 편중 (데이터 집계, 섹션 6)
- `safety harness`(4건) + `near edge`(2건) + `green net`(2건) 동시 출현: 안전대·단부 난간·낙하방지망 **추락방호 3요소 동시 누락** 최악 조건 (추정)
- KeyBERT 대표 키워드 `missing guard railing` · `worker anchoring safety` · `wires web slings` — 구조적 보호설비와 개인보호장구 양측 모두 결함 (데이터 집계, 섹션 9)

**인사이트**: Hankuk은 Module 2F 고소작업 집중 투입 중이며, 구조적 방호설비(난간·안전망)가 선행 설치되지 않은 상태에서 본작업이 진행되고 있다. `safety harness`·`green net`은 즉각 물리적 조치 가능, `unsafe manner`(2건)는 교육으로 전환 처리.

---

### DSHI — 26건 (47.3%) · 섹션 6·9 인용

> 교차집계: 전도/낙하/부딪힘 12건, 기타 4건, 화재/탄화 4건, 감전/합선 2건, 끼임 2건, 떨어짐/낙상 2건 (데이터 집계, 섹션 6)

| 순위 | Safety Phrase | 빈도수 | 의미 해석 |
|------|---------------|--------|-----------|
| 1 | scissor lift | 4건 | 시저리프트 불안전 운용 — PTW·Pre-use Check 미이행 |
| 2 | just near | 3건 | 작업 반경 내 근접 위험 — 행동적 위반, 교육 대상 ⚠️ |
| 3 | name tag | 2건 | 장비 Tag Out 미부착 — LOTO 절차 위반 ⚠️ |
| 4 | earthing connection | 2건 | 용접기 접지선 불량 — 감전 직접 원인 (조치 가능) |
| 5 | lifeline rope | 2건 | 생명줄(Lifeline) 미연결 (조치 가능) |
| 6 | sharp metal | 2건 | 금속 절단면 노출 — 절상·찔림 위험 ⚠️ |
| 7 | gas cylinders | 2건 | 가스 실린더 불안전 보관 — 화재 직접 원인 (조치 가능) |
| 8 | retractable fall arrestor | 2건 | 자동잠금형 추락방지기 미착용 ⚠️ |

**위험 집중 Location**: 감전/합선 2건 전부·화재/탄화 4건 전부 DSHI 발생 (데이터 집계, 섹션 6)
- KeyBERT 대표 키워드 `scissor lift unsafe` · `lifeline rope lifeline` · `earthing connection welding` — 장비 운용·생명줄·접지 3개 축 구조적 반복 (데이터 집계, 섹션 9)
- `gas cylinders`(2건)·`earthing connection`(2건) **2주 연속 동일 패턴** 지속 — 전주 지적 후 근본 개선 없이 형식 조치에 그친 것으로 판단 (추정)
- `name tag`(2건) + `without tag`(2건, 섹션 8): **LOTO 절차 체계적 미이행** — 행동적 위반, 교육 대상

**인사이트**: DSHI는 화기 작업(가스 실린더·접지 불량)과 장비 운용(시저리프트) 양 축에서 위험이 구조화되고 있다. `just near`·`name tag`은 교육으로 전환하고, `earthing connection`·`gas cylinders`·`lifeline rope`는 물리적 즉각 조치 대상.

---

### Daemyoung — 1건 (⚠️ 소표본, 참고 수준)

KeyBERT 키워드 `open shear studs` · `fall hazards deck` — Shear Stud 가공 후 돌출부 미처리로 보행 중 걸림·낙상 위험 유발. 1건으로 통계 해석 불가, 현장 마감 조치 또는 작업자 교육으로 처리. (데이터 집계, 섹션 9)

---

## 3-B. 🧩 의미 기반 클러스터 패턴 분석 (Sentence Transformer + K-means)

> vendor·위험유형 라벨과 무관하게 raw_content 임베딩 유사도로 55건을 8개 클러스터로 자동 분류. 라벨 기반 분석이 놓치는 **크로스컷 위험 패턴**을 식별한다. (데이터 집계, 섹션 11)

| 클러스터 | 대표 키워드 | 건수 | 주요 Vendor | 위험유형(SDN) | 시사점 |
|---|---|---|---|---|---|
| C5 | worker anchoring safety | **14건** | Hankuk 8 / DSHI 5 | 전도/낙하 7·낙상 4·끼임 3 | 전사적 안전장구 고정 문화 결핍 |
| C7 | lifeline rope wrapped | 9건 | Hankuk 6 / DSHI 3 | 전도/낙하 6 | 생명줄·슬링 손상·불량 집중 |
| C3 | signalman scissor lift | 8건 | **DSHI 7** / Hankuk 1 | 전도/낙하 6·끼임 1 | DSHI 시저리프트 단독 집중 |
| C4 | missing guard railing | 7건 | Hankuk 5 / DSHI 2 | 전도/낙하 4·낙상 2 | 가설 방호구조물 미설치 |
| C2 | floor access blocked | 7건 | Hankuk 5 / DSHI 2 | 전도/낙하 3·낙상 2·화재 1 | 통로·접근로 차단 + 화기 |
| C1 | gas cylinder cage | **5건** | **DSHI 5 (독점)** | 화재/탄화 3·기타 2 | DSHI 가스 관리 단독 책임 |
| C6 | toolbox inspection tag | 4건 | Hankuk 3 / DSHI 1 | 기타 3·끼임 1 | 공구·장비 검사 태그 누락 |
| C8 | tighten cylinders | 1건 | DSHI 1 | 전도/낙하 1 | 소표본 ⚠️ |

**클러스터 인사이트:**

1. **C5 "worker anchoring safety" (14건, 25.5%)** — 이번 주 최대 클러스터. Hankuk·DSHI·Daemyoung 전 Vendor에 분산, 위험유형도 3종 혼재. 특정 업체·작업 문제가 아닌 **현장 전반의 추락방호 장구 체결 문화 부재**를 나타낸다. `unsafe manner`·`risky condition`·`near edge`가 함께 출현해 장비 미착용과 불안전 행동이 동시에 발생 중. (데이터 집계)

2. **C3 "signalman scissor lift" (8건)** — 8건 중 DSHI 7건. `scissor lift`(4건) + `incomple scaffold without tag`가 동일 클러스터에서 출현 — 시저리프트 주변 비계 미완성 상태에서 장비를 운용하는 **복합 위험** 패턴. (데이터 집계)

3. **C1 "gas cylinder cage" (5건)** — DSHI 5건 독점, 화재/탄화 집중. 가스 실린더 혼합 보관(산소+가연성 가스 미분리)이 반복되고 있으며 2주 연속 지적에도 근본 미해결 상태. (데이터 집계)

4. **C4·C2 방호구조물 클러스터 합산 (14건)** — `missing guard railing`·`floor access blocked`·`safe access` 집중. Module 2F 투입 전 가시설 선행 설치가 이루어지지 않았음을 데이터가 직접 확인. (데이터 집계)

---

## 4. 🌳 종합 위험 구조 진단 (Root Cause Tree)

> Safety Phrase 전 항목 5건 미만(⚠️ 소표본)이나, 위험유형 고빈도 집계·2주 반복 패턴·클러스터 분석 결과를 종합하여 분석 수행. (데이터 집계)

```
[L1: 현상] 전도/낙하/부딪힘 27건 (49.1%, 전주 대비 ▲6건)
├── [L2: A] Scissor Lift 불안전 운용 (C3 클러스터 DSHI 7건)
│   │   근거: scissor lift 4건(▲3), signalman scissor lift 클러스터 (데이터 집계, 섹션 9·11)
│   └── [L3] PTW 발급 형식화 및 Pre-use Inspection 미이행
│            — 비완성 비계 옆 장비 운용 허용 관행 (추정)
├── [L2: B] 안전난간·방호망·생명줄 미설치 (C4 클러스터 7건)
│   │   근거: missing guard railing 클러스터, mid railing 2건, green net 2건 (데이터 집계, 섹션 11)
│   └── [L3] Module 2F 신규 투입 전 가시설 선행 설치 요건 미적용
│            — 본작업 선진입 구조적 반복 (추정)
└── [L2: C] 불안전 행동 반복 — 감독자 제지 실패
        근거: unsafe manner 4건 2주 연속 미완료, just near ▲3 급증 (데이터 집계, 섹션 13·14)
        └── [L3] Stop-Work Authority(SWA) 비작동:
                 지적 후 재발 시 제재 루프 부재 (추정)

[L1: 현상] 떨어짐/낙상 9건 (Hankuk 7건 = 77.8% 집중)
├── [L2: A] 안전대(Safety Harness) 미착용·불완전 체결 (C5 클러스터 핵심)
│   │   근거: safety harness 4건, near edge 2건, C5 "worker anchoring" 14건 (데이터 집계, 섹션 9·11)
│   └── [L3] 고소작업 시 안전대 체결 불편 회피 + 감독 공백 (추정)
└── [L2: B] 생명줄·추락방지기 앵커포인트 미설치 (C7 클러스터 9건)
        근거: lifeline rope 2건, retractable fall arrestor 2건, C7 클러스터 (데이터 집계, 섹션 9·11)
        └── [L3] Module 2F 신규 구역 앵커포인트 사전 설치 계획 누락 (추정)

[L1: 현상] 화재/탄화 5건 (전주 3건 대비 ▲2건, DSHI 독점)
└── [L2] 가스 실린더 혼합 보관 + 화기 작업 구역 관리 미흡 (C1 클러스터 5건)
        근거: gas cylinders 2건, C1 "gas cylinder cage" DSHI 5건 독점 (데이터 집계, 섹션 9·11)
        └── [L3] Hot Work Permit 현장 적용 미흡 + 2주 연속 미해결
                 — 형식 조치 후 구조 개선 없는 반복 (추정)

[L1: 현상] 붕괴 11건 (한미 기준, 전주 6건 대비 ▲5건)
├── [L2: A] 미완성 비계 태그 미부착 임의 사용
│   │   근거: incomple scaffold without tag, C3 클러스터 내 동시 출현 (데이터 집계, 섹션 10·11)
│   └── [L3] 비계 검사 완료 전 사용 차단 게이트 부재 (추정)
└── [L2: B] 리깅 보조구(Web Sling) 불량 사용
        근거: web slings 2건, C7 "lifeline rope wrapped" 클러스터 내 동시 출현 (데이터 집계)
        └── [L3] Pre-lift Inspection 절차 미이행 (추정)
```

---

## 5. 💡 우선순위 개선 권고

> 미완료 14건을 **물리적 조치 가능** 유형과 **행동적 위반(교육 전환)** 으로 구분하여 처리한다.

### 🔴 단기 (즉시~1주)

**① 미완료 14건 — 유형별 분리 처리** (데이터 집계, 섹션 14)

| 구분 | 대상 | 건수 | 처리 방향 |
|------|------|------|-----------|
| 물리적 조치 가능 | lifeline rope · green net · earthing connection · 난간 관련 | 추정 7~9건 | 이번 주 내 현장 설치·수리 완결 |
| 행동적 위반 — 교육 전환 | **unsafe manner 4건** | 4건 | 해당 작업자 개별 Toolbox Meeting + 재발 방지 서약 + 기록 보존 |
| 작업 완료 후 소급 불가 | 일회성 근접·접촉 위반 | 잔여 | 위험 구역 추가 표식 + 교육 기록 |

> `unsafe manner` 4건: **작업자 신원 확인 → 개별 면담 → 의식교육 이수 → 기록 보존** 절차로 공식 완결 처리. 수치 74.5%에 포함된 행동 위반 Close-Out의 실질적 의미 재검토 필요.

**② Module 2F 긴급 가시설 일제 점검** (데이터 집계, 섹션 11 · C4·C2 클러스터 14건)
- 전 구역 Guard Railing·Green Net·개구부 커버 설치 상태 일제 점검
- Hankuk 소속 고소작업자 전원 안전대 착용 및 앵커포인트 체결 현장 확인
- `missing guard railing`·`floor access blocked` 클러스터 해당 위치 우선 타겟

**③ DSHI Scissor Lift 운용 즉시 검토** (데이터 집계, 섹션 9·11 · C3 클러스터 7건)
- 자격 보유 운전자 명단 확인, 비자격자 즉시 운용 중단
- 시저리프트 주변 비완성 비계 확인 — 인접 작업 즉시 분리
- Name Tag / LOTO 미부착 장비 가동 즉시 중단

**④ DSHI 화기 작업 구역 가스 실린더 전수 점검** (데이터 집계, 섹션 9·11 · C1 클러스터 5건)
- 가스 실린더 혼합 보관 현황 확인 및 즉시 분리 조치
- 손상된 Fire Blanket 즉시 교체 (섹션 10, damaged fire blanket)
- 접지선(Earthing Wire) 전수 점검 — 2주 연속 반복이므로 전수 교체 검토

---

### 🟡 중기 (1개월 이내)

**① Module 2F 전용 추락방호 계획 수립** (C5 클러스터 14건 근거)
- 신규 구역 투입 전 생명줄 앵커포인트·안전난간 설치 완료를 **선행 조건(Gate)** 으로 명문화
- Hankuk·DSHI 전 Vendor 고소작업자 대상 추락방호 실습 교육 (안전대 올바른 착용법·앵커 체결)
- C5 클러스터가 전 Vendor 분산 패턴임을 감안, Vendor별 개별 교육이 아닌 현장 전체 공통 교육 우선

**② Scissor Lift PTW·사전점검 체계 강화** (C3 클러스터 DSHI 7건)
- 시저리프트 사용 전 일일 Pre-use Check 양식 표준화 및 감독자 서명 의무화
- 비완성 비계 인접 장비 운용 금지 기준 규정화

**③ 행동적 반복 위반자 의식교육 체계 구축**
- `unsafe manner`·`just near` 등 2주 이상 연속 행동 위반: 개인별 위반 이력 기록 시작
- 2회 반복 시 → 개별 안전 면담, 3회 이상 시 → 배치 재검토
- Close-Out 불가 위반의 **교육 이수 기록 대체 완결 기준** 문서화

**④ 가스 실린더 정기 점검 및 Hot Work Permit 강화** (C1 클러스터)
- 화기 작업 구역 내 가스 실린더 이격 보관 기준 주 1회 정기 점검 도입
- DSHI 화기 작업 담당자 Hot Work Permit 절차 재교육 — 2주 연속 미해결 구조 개선

---

### 🔵 장기 (분기 이상)

**① Stop-Work Authority(SWA) 실질화**
- `unsafe manner` 4건 2주 연속 미완료 — 현장 SWA가 실질적으로 작동하지 않음을 시사
- Foreman 이상 전원 SWA 교육 이수 의무화 및 행사 실적을 안전 KPI에 반영

**② Module 단계별 Phase-specific Safety Induction 제도화**
- GF → 1F → 2F 작업 이동 시 해당 층 특화 위험 맞춤 Safety Induction 실시
- 신규 구역 진입 첫 주: 가시설 완료 여부 확인 후 투입 Gate 운영 (C4 클러스터 반복 패턴 차단)

**③ 위반 유형 분류 체계 도입 (Closeable vs. Behavioral)**
- Closeable: 현장 물리적 조치 완결 기준 유지
- Behavioral: 교육 이수 → 기록 보존 → 이력 관리로 KPI 산정 개선
- 현재 완료율 74.5%에 행동 위반 Close-Out이 혼재 — **실질 완료율 재정의** 필요 (추정)

**④ 클러스터 기반 선제적 위험 관리 체계 도입**
- 매주 STEP 3 클러스터 분석 결과를 현장 안전 브리핑에 반영
- C5(안전장구 체결) · C3(시저리프트) · C1(가스 관리) 3개 고위험 클러스터를 정기 모니터링 대상으로 지정

---

*보고서 기준: llm_context.md (2026-04-20~24 · 55건) · llm_context_20260417.md (2026-04-13~17 · 47건)*
*수치 출처 미표기 항목은 (추정) 구분 · 작성: Claude Code (claude-sonnet-4-6) · 2026-04-29*
