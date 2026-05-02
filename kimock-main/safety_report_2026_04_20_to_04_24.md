# 주간 안전점검 분석 리포트
## 분석 기간: 2026-04-20 ~ 2026-04-24

> **생성일**: 2026-05-02 | **분석 엔진**: Claude Code (claude-sonnet-4-6) · prompt_v2.md
> **데이터 출처**: llm_context.md (Python 사전계산, 55건) · 전주 비교: 섹션 12 (47건)

---

## ⚡ 이번 주 핵심 메시지

> 전주(47건) 대비 총 위반 건수가 **▲8건(+17%)** 증가한 55건을 기록했으며, Module 2F의 위반 집중도가 전주 14건에서 **31건(▲17)으로 배증**되어 공정 전환에 따른 관리 공백이 확인됐다. 14개 반복 Safety Phrase 패턴이 지속되는 가운데, DSHI의 scissor lift 운용 위반(Cluster 3, DSHI 87.5% 집중)과 가스실린더 보관 위반(Cluster 1, DSHI 100% 집중)은 **Vendor 특정 시스템 개선**이 필요한 Red Flag이며, 미완료 14건 중 `unsafe manner` 4건은 재현 불가 특성상 **즉시 작업자 의식교육으로 전환 Close-Out**해야 한다.

---

## 1. 📊 핵심 지표 요약 (Executive Summary)

- **분석 기간**: 2026-04-20 ~ 2026-04-24 (데이터 집계, 섹션 1)
- **총 안전위반**: 55건 (전주 47건 → **▲8건 +17%**) (데이터 집계, 섹션 12)
- **조치 완료**: 41건 / 완료율 **74.5%** (전주 70.2% → ▲4.3%p) (데이터 집계, 섹션 12)
- **미완료 Open 항목**: **14건** (Hankuk 9건 · DSHI 5건) (데이터 집계, 섹션 14)
- **최다 위험유형(SDN)**: 전도/낙하/부딪힘 27건 (49.1%) ▲6 (데이터 집계, 섹션 3·12)
- **최다 위험유형(한미)**: 추락 15건 (27.3%) ▼3 (데이터 집계, 섹션 4·12)

| Vendor | 건수 | 비중 | 핵심 Safety Phrase | 전주 대비 |
|--------|------|------|-------------------|----------|
| Hankuk | 28건 | 50.9% | safety harness, near edge, green net | ▲3 |
| DSHI | 26건 | 47.3% | scissor lift, just near, earthing connection | ▲4 |
| Daemyoung | 1건 | 1.8% | open shear studs ⚠️ | ▲1 (신규) |

(데이터 집계, 섹션 2·9·12)

**주목 포인트**: Module 1F(전주 27건)에서 **Module 2F로 작업 무게중심 급전환**(31건, 56.4%, ▲17건). Hankuk·DSHI 양사 동반 증가로 특정 업체 단독 문제가 아닌 **현장 전반 안전관리 공백** 신호. (데이터 집계, 섹션 5·12)

감전/합선(Electrocution/Short-circuit) 위험은 ▼6으로 뚜렷한 개선세가 확인됐으나, **끼임 ▲4, 화재 ▲3, 붕괴 ▲5**의 다원화된 위험 증가는 별도 모니터링이 필요하다. (데이터 집계, 섹션 4·12)

---

## 2. 📈 주간 트렌드 분석

### 주차별 발생 건수 추이

| 주차 | 건수 |
|------|------|
| 2026-04-13 ~ 2026-04-17 | 47건 (전주 기준) |
| 2026-04-20 ~ 2026-04-24 | **55건** (이번 주) |

(데이터 집계, 섹션 7·12)

현재 2주 연속 데이터로 단기 상승 추이가 확인된다. **▲8건(+17%)** 증가 폭은 단순 통계 변동 범위를 초과하는 수준으로 주의가 필요하다.

### 전주 대비 급증 항목 (섹션 12)

| 지표 | 이번 주 | 전주 | 증감 |
|------|---------|------|------|
| 총 건수 | 55건 | 47건 | ▲8 |
| Module 2F | 31건 | 14건 | **▲17** (급증) |
| Module 1F | 20건 | 27건 | ▼7 |
| 전도/낙하/부딪힘 (SDN) | 27건 | 21건 | ▲6 |
| 붕괴 (한미) | 11건 | 6건 | ▲5 |
| 끼임 (한미) | 6건 | 2건 | **▲4** |
| 협착 (한미) | 6건 | 2건 | **▲4** |
| 화재 (한미) | 4건 | 1건 | **▲3** |
| 감전/합선 (SDN) | 2건 | 8건 | ▼6 (개선) |

Module 2F의 급증은 해당 층 신규 공정 시작 또는 작업자 배치 집중에 기인할 가능성이 높다. **(추정)** 현장 공정 스케줄과의 교차 확인이 필요하다.

### 🔁 반복 위험 패턴 (섹션 13 — 전주부터 2주 이상 연속)

다음 Safety Phrase는 **구조적 위험 신호**다. 전반적으로 건수는 감소하고 있으나, 완전 소멸에 도달한 패턴이 없다는 점에서 근원 해결이 이뤄지지 않았음을 의미한다.

| 🔁 Safety Phrase | 이번 주 | 전주 | 증감 | 위험 맥락 |
|---|---|---|---|---|
| unsafe manner | 4건 | 7건 | ▼3 | 행동적 위반 — 미완료 4건 100% 포함 |
| scissor lift | 4건 | 9건 | ▼5 | 장비 운용 위반 — DSHI 집중 |
| just near | 4건 | 10건 | ▼6 | 위험 구역 근접 행동 |
| safety harness | 4건 | 6건 | ▼2 | 추락방호 안전대 미착용/미체결 |
| near edge | 3건 | 4건 | ▼1 | 개구부·단부 위험 노출 |
| retractable fall arrestor | 2건 | 5건 | ▼3 | 자동감김 안전장치(SRL) 불량 |
| gas cylinders | 2건 | 6건 | ▼4 | 가스실린더 보관 위반 |
| lifeline rope | 2건 | 4건 | ▼2 | 생명줄(Lifeline) 미설치/불량 |
| risky condition | 2건 | 6건 | ▼4 | 위험 환경 방치 |
| earthing connection | 2건 | 3건 | ▼1 | 접지 불량 — 감전 위험 |
| name tag | 2건 | 5건 | ▼3 | 장비 TPI 스티커 미부착 |
| green net | 2건 | 4건 | ▼2 | 낙하물 방지망 불량 |
| fall arrestor | 2건 | 5건 | ▼3 | 추락방지기 결함 |
| retractable fall arrestor | 2건 | 5건 | ▼3 | SRL 결함 (위와 중복 n-gram) |

(데이터 집계, 섹션 13)

**주목**: 전주 소멸 패턴 `unsafe opening`(19건→0), `materials scattered`(12건→0), `body earthing`(11건→0)은 긍정적 개선 신호. 그러나 소멸이 일시적 억제인지 구조적 해결인지는 추가 관찰 필요. **(추정)**

---

## 3. 🔑 Vendor × Location 심층 분석

### Hankuk — 28건 (50.9%) · 섹션 2·9·6 인용

**Top Safety Phrases (섹션 9 빈도 기준):**

| 순위 | Safety Phrase | 빈도수 | 의미 해석 |
|------|---------------|--------|-----------|
| 1 | safety harness | 4건 | 추락방호구(안전대) 미착용 또는 체결 불량 — 고소작업 중 가장 치명적인 위반 유형 |
| 2 | near edge | 2건 ⚠️ | 슬래브·개구부 단부 근접 작업 — 즉각 추락 위험 노출 |
| 3 | green net | 2건 ⚠️ | 낙하물 방지망(Green Net) 미설치 또는 파손 상태 방치 |
| 4 | unsafe manner | 2건 ⚠️ | 작업자 불안전 행동 — 행동 관리 이슈, 미완료 포함 |
| 5 | web slings | 2건 ⚠️ | 슬링벨트(Web Slings) 손상·불량 상태로 인양 작업 수행 |
| 6 | safe access | 2건 ⚠️ | 안전통로(Safe Access Way) 미확보 또는 자재 차단 |

**위험 집중 Location / 작업 공정:**
- 섹션 6 교차집계: Hankuk은 떨어짐/낙상 7건(전체 9건 중 78%)을 독점 — 고소작업 추락방호가 타 Vendor 대비 취약. (데이터 집계)
- Cluster 4(Missing Guard Railing, Hankuk 71.4%)·Cluster 2(Floor Access Blocked, Hankuk 71.4%)가 Hankuk 고유 구조적 문제를 교차 확증. (데이터 집계, 섹션 11)

**인사이트:** Hankuk의 위반 패턴은 `safety harness` → `near edge` → `green net` 순으로 **고소작업 추락방호 체계 전반의 결핍**을 나타낸다. `safety harness` 4건이 TOP 1이면서 미완료 상위 패턴 `lifeline rope`(2건)과 연계되어, 작업 중 미착용 → 미조치 구조가 반복되고 있다.

---

### DSHI — 26건 (47.3%) · 섹션 2·9·6 인용

**Top Safety Phrases (섹션 9 빈도 기준):**

| 순위 | Safety Phrase | 빈도수 | 의미 해석 |
|------|---------------|--------|-----------|
| 1 | scissor lift | 4건 | 시저 리프트(Scissor Lift) 운용 중 신호수(Signalman) 미배치 또는 안전규정 위반 |
| 2 | just near | 3건 ⚠️ | 인양·장비 작동 구역 내 작업자 무단 접근 |
| 3 | earthing connection | 2건 ⚠️ | 용접기 접지(Earthing) 불량 — 감전(Electrocution) 위험 |
| 4 | lifeline rope | 2건 ⚠️ | 생명줄(Lifeline Rope) 미설치 또는 파손 |
| 5 | sharp metal | 2건 ⚠️ | 절단부·버(Burr) 등 날카로운 금속면 노출 — 부상 위험 |
| 6 | gas cylinders | 2건 ⚠️ | 가스실린더 혼재 보관 — 산소·연료가스 분리 미흡 |
| 7 | retractable fall arrestor | 2건 ⚠️ | 자동감김 추락방지기(SRL, Self-Retracting Lifeline) 결함 |

**위험 집중 Location / 작업 공정:**
- 섹션 6: DSHI는 감전/합선 2건 전체 담당 — 전기용접·접지 관련 작업 집중. (데이터 집계)
- 섹션 6: 화재/탄화 5건 중 DSHI 4건(80%) — 가스 작업·Hot Work 관리 취약. (데이터 집계)
- Cluster 3(Signalman Scissor Lift): DSHI 7건/8건(87.5%) → **🚨 Red Flag: DSHI 장비 운용 관리 시스템 부재**. (데이터 집계, 섹션 11)
- Cluster 1(Gas Cylinder Cage): DSHI 5건/5건(100%) → **🚨 Red Flag: DSHI 가스 보관 전담 위반**. (데이터 집계, 섹션 11)

**인사이트:** DSHI 위반은 크게 두 계열로 분리된다. ① **장비 운용계** (`scissor lift`, `just near`) — 시저 리프트 작업 절차 미준수; ② **에너지 위험계** (`earthing connection`, `gas cylinders`) — 용접·가스 작업 중 에너지 격리(Isolation) 및 보관 규정 위반. 두 계열이 독립적으로 반복되는 패턴은 **DSHI 내 안전관리 감독 체계의 구조적 공백**을 시사한다.

---

### Daemyoung — 1건 (1.8%) · 섹션 2·9 인용

| 순위 | Safety Phrase | 빈도수 | 비고 |
|------|---------------|--------|------|
| 1 | open shear studs → trip fall → risky condition | 1건 각 | ⚠️ 소표본 — 참고 수준 |

Daemyoung 이번 주 신규 진입(전주 0건 → ▲1). 데크 위 노출 전단 스터드(Shear Studs)로 인한 발걸림/낙상 위험 1건 기록. ⚠️ 소표본으로 과대해석을 지양하나, 신규 참여 업체의 현장 적응 교육(Site Induction) 이행 여부 확인 권장. (데이터 집계, 섹션 9)

---

## 3-B. 🔬 의미 클러스터 기반 구조 패턴 (섹션 11 인용)

| 클러스터명 | 건수 | 지배 Vendor (비중) | 위험 판정 |
|-----------|------|-------------------|----------|
| Cluster 5: worker anchoring safety | 14건 | Hankuk 57% / DSHI 36% | 현장 전반 구조적 위험 |
| Cluster 7: lifeline rope wrapped | 9건 | Hankuk 67% / DSHI 33% | 현장 전반 (Hankuk 우세) |
| Cluster 3: signalman scissor lift | **8건** | **DSHI 87.5%** | **🚨 Red Flag: DSHI 국한** |
| Cluster 4: missing guard railing | **7건** | **Hankuk 71.4%** | **🚨 Red Flag: Hankuk 국한** |
| Cluster 2: floor access blocked | **7건** | **Hankuk 71.4%** | **🚨 Red Flag: Hankuk 국한** |
| Cluster 1: gas cylinder cage | **5건** | **DSHI 100%** | **🚨 Red Flag: DSHI 국한** |
| Cluster 6: toolbox inspection tag | 4건 ⚠️ | Hankuk 75% | 소표본 참고 |
| Cluster 8: tighten cylinders | 1건 ⚠️ | DSHI 100% | 소표본 참고 |

(데이터 집계, 섹션 11)

### 확증 위험 (섹션 8~9 n-gram 빈도 + 클러스터 패턴 일치 항목)

1. **`scissor lift` — DSHI 확증 위험**: 섹션 8 전체 TOP 2(4건) + 섹션 9 DSHI TOP 1(4건) + Cluster 3(DSHI 87.5%) — 3개 분석 축이 일치하는 **가장 강력한 확증 위험**. DSHI의 시저 리프트 작업 절차 위반은 데이터 전반에 걸쳐 일관되게 확인.

2. **`safety harness` / `near edge` — Hankuk 확증 위험**: 섹션 9 Hankuk TOP 1(4건) + Cluster 5 내 safety harness 4건 + Cluster 7(Hankuk 67%) — 고소작업 추락방호 체계 결핍이 복수 분석 축에서 교차 확인.

3. **`gas cylinders` — DSHI 확증 위험**: 섹션 9 DSHI 6위(2건) + Cluster 1(DSHI 100%, 5건) — 클러스터가 가스실린더 보관 위반을 DSHI 전담 패턴으로 확증.

---

## 4. 🌳 종합 위험 구조 진단 (Root Cause Tree)

> 대상 선정 기준: ① Cluster 단일 Vendor 집중 ≥ 70% 대표 Phrase / ② 섹션 14 미완료 × 섹션 8 빈도 교차 Phrase | 최대 5개·깊이 3단계 고정

---

### Tree 1: Scissor Lift 운용 위반 — DSHI 87.5% 집중 (현상, L1)

```
Scissor Lift 작업 중 안전규정 위반 (8건, DSHI 87.5% — Cluster 3)
├── 직접 원인 A: 신호수(Signalman) 미배치 (L2) — (데이터 집계, 섹션 9·11 Cluster 3)
│   └── 근본 원인 A-1: PTW(Permit-to-Work) 상 신호수 배치 요건 미기재 또는
│       DSHI 내부 감독자 체크 누락 (L3)
├── 직접 원인 B: 장비 인근 구역 작업자 무단 접근 (`just near` 3건) (L2)
│   — (데이터 집계, 섹션 9 DSHI)
│   └── 근본 원인 B-1: 인양·장비 작동 구역 출입 통제(Barricade) 절차 미이행 및
│       작업자 위험 인식 부족 (L3)
└── 직접 원인 C: 장비 사전 안전 점검 미흡 (L2) — (추정)
    └── 근본 원인 C-1: DSHI 내 장비 Pre-Use Inspection 체계 부재 또는 형식적 이행 (L3)
```

---

### Tree 2: Gas Cylinder 보관 위반 — DSHI 100% 집중 (현상, L1)

```
가스실린더(산소·LPG) 혼재 보관 및 관리 위반 (5건, DSHI 100% — Cluster 1)
├── 직접 원인 A: 산소-연료가스 분리 보관 미이행 (L2)
│   — (데이터 집계, 섹션 11 Cluster 1)
│   └── 근본 원인 A-1: DSHI 가스 취급 작업자 대상 MSDS·보관 규정 교육 미실시 또는
│       현장 적용 실패 (L3)
├── 직접 원인 B: 실린더 고정 불량 (1개 스트랩만 사용 확인) (L2)
│   — (데이터 집계, 섹션 11 Cluster 8)
│   └── 근본 원인 B-1: 가스실린더 전용 캐리어/케이지 미확보 및 임시 보관 관행화 (L3)
└── 직접 원인 C: Hot Work 구역 가스 사용 관리 미흡 (L2) — (추정)
    └── 근본 원인 C-1: Hot Work Permit 상 가스실린더 위치·수량 사전 신고 절차 미준수 (L3)
```

---

### Tree 3: 추락방호구(Safety Harness / Lifeline) 미착용 — Hankuk 주도 (현상, L1)

```
고소작업 중 추락방호구 미착용·미체결·불량 (14건, Hankuk 57% — Cluster 5)
├── 직접 원인 A: 안전대(Safety Harness) 미착용 또는 체결 미흡 (`safety harness` 4건) (L2)
│   — (데이터 집계, 섹션 9 Hankuk·섹션 11 Cluster 5)
│   └── 근본 원인 A-1: 작업 전 안전대 착용 여부 감독자 확인 절차 부재 —
│       TBM(Toolbox Meeting) 체크리스트 미적용 (L3)
├── 직접 원인 B: 자동감김 추락방지기(SRL) 결함 (`retractable fall arrestor` 2건) (L2)
│   — (데이터 집계, 섹션 8·11 Cluster 5)
│   └── 근본 원인 B-1: SRL 정기 점검 및 결함 교체 체계 미흡 — 사용 전 기능 검사 생략 (L3)
└── 직접 원인 C: 단부·개구부 인근 생명줄(Lifeline) 미설치 (`near edge` 2건·`lifeline rope` 2건) (L2)
    — (데이터 집계, 섹션 9 Hankuk)
    └── 근본 원인 C-1: Module 2F 신규 작업 구역 전개 시 생명줄 앵커 포인트
        사전 설치 절차 누락 (L3)
```

---

### Tree 4: Guard Railing·안전통로 미확보 — Hankuk 71% 집중 (현상, L1)

```
가드레일(Guard Railing) 미설치 및 안전통로(Safe Access) 차단
(7건, Hankuk 71% — Cluster 4·Cluster 2)
├── 직접 원인 A: 미드레일(Mid Railing)·발판(Toe Board) 누락
│   (`missing guard`·`mid railing`·`toe board`) (L2)
│   — (데이터 집계, 섹션 9 Hankuk)
│   └── 근본 원인 A-1: 임시 작업 발판 설치 후 가드레일 재설치 절차 미이행 —
│       공정 단계 전환 시 안전설비 인수인계 체계 부재 (L3)
├── 직접 원인 B: 안전통로 자재 적치·차단 (`safe access` 2건) (L2)
│   — (데이터 집계, 섹션 9 Hankuk·섹션 11 Cluster 2)
│   └── 근본 원인 B-1: Module 2F 급격한 작업 집중에 따른 임시 자재 관리 계획 부재 —
│       자재 반입/야적 통제 미흡 (L3)
└── 직접 원인 C: 낙하물 방지망(Green Net) 손상 또는 미설치 (`green net` 2건) (L2)
    — (데이터 집계, 섹션 9 Hankuk)
    └── 근본 원인 C-1: Module 층별 공정 전환 시 낙하물 방지망 설치 기준 미적용 (L3)
```

---

### Tree 5: Unsafe Manner (행동적 위반) — 미완료 4건 전건 포함 (현상, L1)

```
작업자 불안전 행동 (`unsafe manner`) — 전체 4건·미완료 4건 100% 일치
├── 직접 원인 A: 불안전 행동 발생 후 즉각 시정 조치 미이행 (L2)
│   — (데이터 집계, 섹션 8·14)
│   └── 근본 원인 A-1: 행동적 위반은 작업 종료 시 재현 불가(Temporary)로
│       Close-Out 기준 불명확 → 담당자 조치 보류 반복 (L3)
├── 직접 원인 B: TBM(Toolbox Meeting) 또는 작업 전 안전교육 효과 미흡 (L2) — (추정)
│   └── 근본 원인 B-1: 반복 지도 누적에도 행동 변화 미발생 —
│       교육 방식·내용 구조적 개편 필요 (L3)
└── 직접 원인 C: 현장 감독자의 순찰·지도 빈도 부족 (L2) — (추정)
    └── 근본 원인 C-1: 감독자 1인당 담당 작업자 수 과다 또는 순찰 구역 집중화 미흡 (L3)
```

> ⚠️ `unsafe manner` 미완료 4건은 행동적 위반 특성상 사후 Close-Out이 사실상 불가하다. **작업자 의식교육 이행 확인서로 대체 Close-Out 처리**를 권고한다.

---

## 5. 💡 우선순위 개선 권고

### 단기 (즉시~1주): 미완료 14건 포함 현장 즉각 조치

1. **미완료 14건 Close-Out 일정 확정** (Hankuk 9건·DSHI 5건): 각 Vendor 안전담당자와 일자별 Close-Out 계획 수립. `unsafe manner` 4건은 의식교육 이행 확인서로 대체 Close-Out. (데이터 집계, 섹션 14)
2. **DSHI Scissor Lift 작업 즉시 점검**: 현장 내 전체 시저 리프트 PTW 재검토 및 신호수(Signalman) 배치 현황 확인. Cluster 3(8건, DSHI 87.5%) 대응. (데이터 집계, 섹션 11)
3. **DSHI 가스실린더 즉시 실사**: 산소/연료가스 분리 여부, 전용 케이지 고정 상태, 실린더 캡 체결 전수 확인. Cluster 1(DSHI 100%) 대응. (데이터 집계, 섹션 11)
4. **Module 2F 추락방호 일제 점검**: 생명줄 앵커 포인트·가드레일·낙하물 방지망(Green Net) 설치 현황 전수 확인. 전주 대비 ▲17건 급증 구역. (데이터 집계, 섹션 5·12)
5. **Daemyoung 신규 진입 교육 확인**: Site Induction 이수 및 현장 안전규정 숙지 여부 확인. ⚠️ 소표본이나 신규 업체 진입 관리 원칙 적용. (데이터 집계, 섹션 2)

### 중기 (1개월 이내): 프로세스·교육 개선

1. **DSHI 대상 Scissor Lift 전용 안전 교육 실시**: 시저 리프트 SOP 재정비 — 신호수 배치, 출입 통제 바리케이드 설치, 탑승자 하네스 체결 3개 항목 의무화. 섹션 13 🔁 2주 연속 패턴 대응. (데이터 집계)
2. **Hankuk 추락방호 TBM 강화**: 매일 작업 전 안전대·SRL 기능 점검을 TBM 체크리스트에 항목화. `safety harness`(🔁, 섹션 13) 및 미완료 `lifeline rope` 대응. (데이터 집계)
3. **Module 2F 공정 전환 시 안전설비 인수인계 SOP 마련**: 가드레일·낙하물 방지망·생명줄 앵커 재설치 의무화 절차 수립. Cluster 4·Cluster 2 반복 위반 구조적 대응. (데이터 집계, 섹션 11)
4. **`unsafe manner` Close-Out 기준 명문화**: 행동적 위반에 대한 별도 Close-Out 절차(의식교육 이행 확인서) 현장 안전관리 지침에 반영. (데이터 집계, 섹션 14)
5. **Hot Work Permit 가스 관리 항목 추가**: 가스실린더 위치·수량·분리 보관 여부를 Hot Work Permit 발급 전 체크리스트 필수 항목으로 포함. Cluster 1 대응. (데이터 집계, 섹션 11)

### 장기 (분기 이상): 시스템·제도 구조적 개선

1. **Vendor 안전 KPI 체계 도입**: 주간 위반 건수·미완료율·반복 위반 패턴 횟수를 Vendor 평가 지표에 연동. DSHI·Hankuk 반복 패턴에 대한 Vendor 책임 체계 구축.
2. **현장 전 구역 추락방호 고정점(Anchor Point) 사전 설계**: Module별 고소작업 예정 구역을 착공 전 확정하고, 생명줄 설치점을 구조도에 선 반영. Cluster 5·7 반복 구조 대응.
3. **Safety Phrase 반복 패턴 자동 알림 체계 구축**: 동일 Phrase가 N주 연속 등장 시 CM 안전관리자에게 자동 알림 발송 — 데이터 기반 선행 지표(Leading Indicator) 체계 전환.
4. **Scissor Lift 장비 Pre-Use Inspection 전자화**: 종이 체크리스트를 디지털 폼으로 전환, 미체크 항목 존재 시 작업 잠금 기능 도입. DSHI Cluster 3 구조적 대응. **(추정)**

---

*이 리포트는 `llm_context.md` Python 사전계산값만 인용하며, 모든 수치는 (데이터 집계) 출처와 섹션 번호를 병기하였습니다. 수치 없이 추론한 내용은 (추정)으로 명기하였습니다.*
