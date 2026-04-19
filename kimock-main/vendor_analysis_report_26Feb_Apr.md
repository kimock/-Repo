# SDN Module Expansion PJT — 업체별 잠재위험 KeyBERT 심층 분석 보고서
## 점검 기간: 2026년 2월 ~ 4월 (ISO W6 – W14)

**Project:** SDN Module Expansion PJT  
**분석 도구:** KeyBERT `paraphrase-multilingual-MiniLM-L12-v2` + MMR 다양성(0.4) + 2–3gram  
**데이터:** (CM, SCT) 잠재위험발굴_발표용.xlsx — 26년 2월·3월·4월 시트 총 461건  
**보고서 작성일:** 2026-04-14  

---

## 분석 방법

- **KeyBERT 설정:** `keyphrase_ngram_range=(2,3)`, `use_mmr=True`, `diversity=0.4`, `top_n=15`
- **모델:** `paraphrase-multilingual-MiniLM-L12-v2` — 다국어 지원, 문맥 유사도 기반 추출
- **보완 지표:** 추출된 키워드 구성 단어(4자 이상)가 실제 위반 항목에 등장하는 건수(items)를 교차 검증
- **분석 단위:** 전체 corpus → 위험 카테고리별 세부 corpus 순서로 2단계 분석

---

## 1. 전체 요약

| Vendor | 총건수 | Major | Minor | 미조치 | 핵심 위험 키워드 (KeyBERT 최상위) |
|--------|------:|------:|------:|------:|-------------------------------|
| Hankuk C&T | 256 | 183 | 73 | 6 | `scaffolding`, `material lifting`, `unsafe opening` |
| DSHI | 158 | 121 | 37 | 4 | `lift signalman`, `earthing wire`, `barricade` |
| RTCC | 29 | 16 | 13 | 3 | `scaffolding inspection`, `msds`, `excavator` |
| Daemyoung | 13 | 9 | 4 | 1 | `pdb access`, `cable termination`, `housekeeping` |

---

## 2. Hankuk C&T — KeyBERT 심층 분석

> **총 256건 · Major 71.5% · 미조치 6건**

### 2-1. 전체 코퍼스 2–3gram 키워드 (Top 15)

| 순위 | 키워드 | KW Score | 관련 항목 수 | 의미 해석 |
|-----|--------|:--------:|:-----------:|---------|
| 1 | `grinder guard used` | 0.5827 | 20건 | 그라인더 가드 미착용·파손·제거 후 사용 반복 |
| 2 | `didn remove scaffolding` | 0.5219 | 41건 | 비계 철거·정리 미이행 (공정 후 방치) |
| 3 | `type damaged rope` | 0.4698 | 33건 | 파손·불량 로프·슬링 계속 사용 |
| 4 | `safety hooking properly` | 0.4583 | 29건 | 안전고리 연결 불량·미연결 |
| 5 | `rebars fall protection` | 0.4467 | 22건 | 철근 위 보행·작업 중 추락 방호 미설치 |
| 6 | `calble housekeeping didn` | 0.4398 | 10건 | 케이블 정리 미이행 — 통행·감전 위험 |
| 7 | `belt shifting calble` | 0.4290 | 16건 | 벨트·슬링 없이 자재 이동·케이블 취급 불량 |
| 8 | `earthing machine unsafe` | 0.4114 | 46건 | 전동 기계 접지 미연결·불량 (가장 많은 항목에서 등장) |
| 9 | `lanyard missing tools` | 0.3943 | 6건 | 공구 랜야드(낙하 방지 끈) 미부착 |
| 10 | `shouldn material lifting` | 0.3824 | 65건 | 부적절한 방법으로 자재 인양·이동 |
| 11 | `worker standing railings` | 0.3793 | 41건 | 난간·가드레일 위에 기립·이동 |
| 12 | `board shifted workers` | 0.3130 | 26건 | 발판·보드 이동 중 작업자 탑승·불안전 이동 |

> **핵심 신호:** `earthing machine unsafe` — 건수가 46건으로 가장 많이 등장. 감전 카테고리(5건)보다 훨씬 넓게 분포 → 감전 위험이 공식 분류 이상으로 현장 전반에 잠재

### 2-2. 카테고리별 2–3gram 심층 분석

#### ▶ 떨어짐/낙상 (73건)

| 순위 | 키워드 | Score | 항목 수/73 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `unsafe opening scaffolding` | 0.6309 | **38건** | 비계 내 개구부 미차단이 가장 광범위한 패턴 |
| 2 | `platforms height unsafe` | 0.5449 | **38건** | 고소 작업 발판 자체가 불안전한 상태로 운영 |
| 3 | `lifeline check scaffolding` | 0.6300 | **28건** | 생명줄 미연결·점검 미실시 + 비계 병행 |
| 4 | `safety hook lifeline` | 0.5096 | **26건** | 안전고리-생명줄 체계 전반 붕괴 |
| 5 | `scaffolding outrigger wrong` | 0.6832 | **19건** | 아우트리거 미설치·불량 설치 비계 사용 |
| 6 | `scaffolding guard railings` | 0.5922 | **18건** | 가드레일 없는 비계 사용 |
| 7 | `hook attached wrong` | 0.4875 | 7건 | 안전고리 잘못된 위치 체결 |
| 8 | `inspection broken ladder` | 0.5675 | 6건 | 파손 사다리 점검 없이 사용 |

**원인 분석:**
1. **비계 관리 3중 실패** — `unsafe opening`(38건) + `guard railings`(18건) + `outrigger wrong`(19건) 동시 등장 → 비계 설치 완료 기준(체크리스트) 없이 사용 개시. 아우트리거·가드레일·개구부 차단이 동일 비계에서 동시 누락
2. **생명줄-안전고리 체계 형식화** — `lifeline check`(28건) + `safety hook lifeline`(26건) → 착용은 하되 앵커포인트 연결 생략, 생명줄 매듭 사용, 점검 태그 없음. PPE 착용 확인만으로는 위험 통제 불가
3. **반복 재발 구조** — `unsafe opening` 38건 = 전체 추락 건수의 52% → 동일 개구부에서 반복 발굴. 개구부 목록 관리·일일 점검 제도 없음

---

#### ▶ 전도/낙하/부딪힘 (93건)

| 순위 | 키워드 | Score | 항목 수/93 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `shouldn material lifting` | 0.6143 | **42건** | 기준 위반 인양 — 45% 해당, 가장 근본적 문제 |
| 2 | `rope using material` | 0.5959 | **37건** | 비규격 로프로 자재 묶음·인양 |
| 3 | `avoid material falling` | 0.5358 | **27건** | 낙하 방지 조치 없이 자재 고소 취급 |
| 4 | `material bucket dangerous` | 0.5217 | **25건** | 버킷·용기에 자재 적재 인양 — 낙하 위험 |
| 5 | `didnt use material` | 0.4908 | **25건** | 인양 장비·보조도구 미사용 |
| 6 | `secured rope unsafe` | 0.4975 | **22건** | 로프 고정 불량 상태로 인양 |
| 7 | `used crane` | 0.5218 | 11건 | 크레인 운용 중 위험 — SWL·신호수 관련 |
| 8 | `scaffolding zoning` | 0.4018 | 5건 | 인양 구역 내 비계·작업자 구역 미분리 |

**원인 분석:**
1. **인양 기준 전무 (42건, 45%)** — `shouldn material lifting` 최고 빈도 → Pre-Lift Check 문서, 슬링 SWL 확인, 리거 자격 확인 절차 모두 미이행. "일단 올린다" 관행
2. **비규격 로프 만연** — `rope using material`(37건) + `secured rope unsafe`(22건) → 정식 슬링·샤클 대신 일반 로프·와이어 무결속 사용. 현장 리깅 자재 부족 또는 절차 무시
3. **낙하 방지 구역 통제 부재** — `avoid material falling`(27건) + `material bucket dangerous`(25건) → 인양 시 하부 출입 통제 없이 진행. 고소 가장자리 자재 방치

---

#### ▶ 감전/합선 (5건) — 소규모이나 HIGH RISK 집중

| 순위 | 키워드 | Score | 핵심 위반 |
|-----|--------|:-----:|---------|
| 1 | `grounding earthing damaged` | 0.5928 | 접지 케이블 파손·미연결 |
| 2 | `motor body grounding` | 0.5478 | 진동기(vibrator) 모터 본체 접지 미연결 |
| 3 | `vibrator motor body` | 0.5229 | 콘크리트 바이브레이터 접지 누락 |
| 4 | `board exposed` | 0.4153 | 전기 보드·케이블 노출 방치 |

**원인 분석:**
- 5건 중 **접지 관련 3건** → 콘크리트 타설 시 사용하는 바이브레이터·전동 장비 접지 체계 전무
- **W14 미조치 2건** 중 1건이 감전(RCCB 파손 + 노출 케이블) → 전기 임시 설비 점검 주기 없음
- **HIGH RISK (맨발+전선 근접)** — `bucket near electrical`: 절연 PPE 착용 의무화 미이행

---

#### ▶ 화재 (8건)

| 순위 | 키워드 | Score | 항목 수/8 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `machine doing welding` | 0.4677 | 4건 | 용접 작업 중 화기 감시자·소화기 없음 |
| 2 | `sparks fall refueling` | 0.5061 | 2건 | 급유 중 스파크·화원 근접 |
| 3 | `prohibited inside company` | 0.4154 | 3건 | 회사 금지 구역 내 화기 작업 |
| 4 | `pump watchman strictly` | 0.4624 | 2건 | 펌프 가동 중 감시자 미배치 |

**원인 분석:**
- 용접 관련 4건 = 전체 화재의 50% → 열작업허가(Hot Work Permit) 발행 없이 용접 진행
- 급유·가연성 물질 관리 미흡 → 격리 보관·금연 구역 지정 미이행

---

#### ▶ 기타 (73건) — 실질 위험 포함

| 순위 | 키워드 | Score | 항목 수/73 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `material housekeeping goggles` | 0.3421 | **20건** | 자재 정리 + 보안경 동시 미이행 |
| 2 | `work permit work` | 0.3726 | **19건** | 작업허가서(PTW) 없이 작업 진행 |
| 3 | `poor housekeeping concrete` | 0.5458 | 9건 | 콘크리트 작업 후 하우스키핑 불량 |
| 4 | `sop boar safety` | 0.4301 | 9건 | SOP·안전 절차서 미비치·미준수 |

> **작업허가서(PTW) 미발행 19건** — '기타' 분류이나 실질적으로 고위험 무허가 작업. PTW 시스템 강화 시급

---

### 2-3. Hankuk C&T 종합 위험 구조 진단

```
[근본 원인 Tree]
Hankuk C&T 핵심 위험
├── 비계 관리 체계 부재
│   ├── 아우트리거 미설치 (19건)
│   ├── 가드레일 없는 비계 (18건)
│   └── 개구부 미차단 반복 (38건) ← 동일 지점 재발
├── 인양 절차 형식화
│   ├── Pre-Lift Check 미이행 (42건)
│   ├── 비규격 로프 사용 (37건)
│   └── 하부 통제 없음 (27건)
├── 전기 안전 무관리
│   ├── 임시 설비 무점검 (46건 earthing 관련)
│   └── HIGH RISK 맨발 전기 작업 (1건, 미조치)
└── PTW 미발행 (19건) → 무허가 작업 상시화
```

---

## 3. DSHI — KeyBERT 심층 분석

> **총 158건 · Major 76.6% · 미조치 4건**

### 3-1. 전체 코퍼스 2–3gram 키워드 (Top 15)

| 순위 | 키워드 | KW Score | 관련 항목 수 | 의미 해석 |
|-----|--------|:--------:|:-----------:|---------|
| 1 | `lift signalman unsafe` | 0.4408 | **64건** | 리프트 작업 중 신호수·안전 관리 전반 부재 |
| 2 | `work plan mismatch` | 0.2405 | **43건** | 작업계획서와 실제 작업 불일치 |
| 3 | `standing wall unsafe` | 0.3865 | **39건** | 벽면·구조물 위 불안전 자세로 기립·작업 |
| 4 | `area leakage lack` | 0.3425 | **36건** | 구역 내 유출·관리 결여 |
| 5 | `working signalman housekeeping` | 0.3418 | **26건** | 작업 중 신호수 없음 + 정리 불량 병행 |
| 6 | `condition just trailer` | 0.3852 | 24건 | 트레일러·이동 차량 불안전 상태 |
| 7 | `equipment plan cabin` | 0.4497 | 12건 | 장비 운용 계획·캐빈 도어 관리 미흡 |
| 8 | `missing swl working` | 0.4534 | 11건 | SWL(안전하중) 표시 없이 인양 작업 |
| 9 | `needs removed equipment` | 0.3985 | 11건 | 불량 장비 즉각 제거 미이행 |
| 10 | `cabin door open` | 0.3731 | 5건 | 작업 중 캐빈 도어 열린 상태 운전 |

> **핵심 신호:** `lift signalman unsafe` 64건 — DSHI 전체 건수의 40% 이상. 리프트·크레인·붐리프트 신호 체계가 DSHI의 구조적 취약점

### 3-2. 카테고리별 2–3gram 심층 분석

#### ▶ 떨어짐/낙상 (34건)

| 순위 | 키워드 | Score | 항목 수/34 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `fall height unsafe` | 0.5923 | **26건** | 고소 불안전 상태 포괄적 패턴 — 76% |
| 2 | `unsafe loose scaffolding` | 0.7189 | **19건** | 느슨·불안전 비계 구조물 사용 |
| 3 | `lift unsafe working` | 0.6471 | **19건** | 리프트 불안전 사용 중 추락 위험 |
| 4 | `harness retractable fall` | 0.5472 | **12건** | 안전고리·자기수축 랜야드 관련 문제 |
| 5 | `structure worker` | 0.5409 | 8건 | 구조물 위 작업자 위험 위치 |
| 6 | `elevated platform inadequate` | 0.4974 | 7건 | 고소 작업대·플랫폼 기준 미달 |
| 7 | `crane lifting steel` | 0.6576 | 4건 | 크레인 인양 중 추락 위험 |

**원인 분석:**
1. **비계 구조 불량 만연** — `unsafe loose scaffolding`(19건) + `elevated platform inadequate`(7건) → DSHI 투입 구역 비계 품질 관리 미흡. 조립 완료 전 사용, 볼트 미체결 상태 확인
2. **리프트 = 추락 위험 도구** — `lift unsafe working`(19건) → 붐리프트·시저리프트 안전 교육 미이행. 아웃리거 미설치, 과부하, 출구 없는 위치 진입
3. **안전고리 사용 방법 오류** — `harness retractable fall`(12건) → 착용은 하나 체결 위치 잘못됨, 자기수축 랜야드 꼬임 방치

---

#### ▶ 전도/낙하/부딪힘 (66건)

| 순위 | 키워드 | Score | 항목 수/66 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `lifting work barricade` | 0.5689 | **30건** | 인양 작업 중 하부 바리케이드 미설치 — 45% |
| 2 | `rope connected work` | 0.5317 | **24건** | 로프 연결·고정 불량 인양 |
| 3 | `area cordoned kindly` | 0.4586 | **18건** | 위험 구역 코든(통제선) 없이 작업 |
| 4 | `slanted boom bucket` | 0.4700 | 11건 | 붐 장비 기울어진 상태 버킷 이동 |
| 5 | `protruding bolts steel` | 0.5686 | 5건 | 돌출 볼트·철재로 부딪힘 위험 |
| 6 | `missing wire ceiling` | 0.6372 | 3건 | 천장부 와이어·배선 누락·낙하 위험 |
| 7 | `crain swl signage` | 0.4242 | 1건 | 크레인 SWL 표시 없이 운용 |

**원인 분석:**
1. **인양 하부 통제 구조적 부재** — `lifting work barricade`(30건) = 전도/낙하 건수의 45%. 리거 배치·하부 통제·코든 설치가 DSHI 인양 작업에서 습관적으로 생략
2. **로프·리깅 기술 부족** — `rope connected work`(24건) → 슬링 각도 계산 없이 연결, 비규격 로프 사용, 샤클 핀 풀림 방치
3. **구역 통제 개념 부재** — `area cordoned`(18건) → 인양·고소 작업 반경 내 일반 작업자 자유 통행

---

#### ▶ 감전/합선 (7건) — 접지 집중

| 순위 | 키워드 | Score | 항목 수/7 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `damaged earthing holder` | 0.5297 | **5건** | 접지 홀더 파손 상태 계속 사용 |
| 2 | `body earthing wire` | 0.5036 | **5건** | 기계 본체 접지 와이어 미연결 |
| 3 | `earthing operator safety` | 0.4989 | **4건** | 접지 연결 절차 작업자 미준수 |
| 4 | `earthing connection stand` | 0.4047 | **5건** | 코어 드릴·전동 공구 스탠드 접지 미연결 |
| 5 | `boomlift cutting wire` | 0.5447 | 2건 | 붐리프트 이동 중 전선 절단 위험 |
| 6 | `drill machine safety` | 0.5471 | 3건 | 코어드릴 기계 안전장치 미비 |

**원인 분석:**
1. **접지 연결 = DSHI 구조적 취약점** — `earthing` 관련 4개 키워드 모두 5건 이상 → 단순 실수가 아닌 절차 자체가 없음. 용접기·코어드릴·전동 공구 Pre-use 점검 시 접지 확인 항목 없음
2. **파손 장비 계속 사용** — `damaged earthing holder` 5건 → 접지 홀더 파손 인지 후에도 교체 없이 사용. 불량 장비 신고·교체 절차 부재

---

#### ▶ 화재 (9건)

| 순위 | 키워드 | Score | 항목 수/9 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `hot work area` | 0.4449 | **5건** | 열작업 구역 관리 미흡 |
| 2 | `near lpg cylinder` | 0.3903 | 4건 | LPG 실린더 근접 화기 작업 |
| 3 | `lock arc welding` | 0.5229 | 3건 | 아크 용접 중 잠금·격리 미이행 |
| 4 | `extinguisher hydrant access` | 0.4680 | 2건 | 소화기·소화전 접근 차단 |
| 5 | `repeated safety violation` | 0.3897 | 1건 | 동일 안전 위반 반복 (점검 기록에 명시) |

**원인 분석:**
- LPG 실린더 근접 열작업 4건 → 가스 실린더 격리 보관·사용 중 거리 기준(3m) 미적용
- `repeated safety violation` — 점검자가 반복 위반으로 명시 기록 → DSHI 특정 작업조의 상습 위반 패턴

---

#### ▶ 기타 (39건) — 관리 체계 부재

| 순위 | 키워드 | Score | 항목 수/39 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `locked material barricaded` | 0.5440 | **10건** | 자재 잠금·바리케이드 미설치 |
| 2 | `equipment plan cabin` | 0.4233 | 8건 | 장비 운용 계획서·캐빈 도어 관리 |
| 3 | `removed equipment boom` | 0.3839 | 6건 | 불량 장비 제거 미이행 (붐 장비) |
| 4 | `barication swl working` | 0.4504 | 4건 | 바리케이드 + SWL 표시 동시 누락 |
| 5 | `trolley shifting unsecured` | 0.3659 | 4건 | 트롤리 이동 중 화물 미고정 → NEAR MISS |

---

### 3-2. DSHI 종합 위험 구조 진단

```
[근본 원인 Tree]
DSHI 핵심 위험
├── 리프트·크레인 운용 체계 붕괴
│   ├── 신호수 미배치 (64건) ← 전체 40% 관여
│   ├── SWL 표시 없는 인양 (11건)
│   └── 붐리프트 점검 태그 미부착 (미조치)
├── 인양 하부 통제 전무
│   ├── 바리케이드 미설치 (30건)
│   ├── 코든(통제선) 없음 (18건)
│   └── 로프 불량 연결 (24건)
├── 접지(Earthing) 절차 부재
│   ├── 접지 홀더 파손 → 계속 사용 (5건)
│   └── Pre-use 점검 항목 없음
└── 반복 위반 (repeated violation 명시)
    └── 특정 작업조 상습 위반 → 개인 조치 필요
```

---

## 4. RTCC — KeyBERT 심층 분석

> **총 29건 · Major 55.2% · 미조치 3건 (완료율 89.7% — 주요 Vendor 최저)**

### 4-1. 전체 코퍼스 2–3gram 키워드 (Top 15)

| 순위 | 키워드 | KW Score | 관련 항목 수 | 의미 해석 |
|-----|--------|:--------:|:-----------:|---------|
| 1 | `scaffolding inspection bad` | 0.5330 | 2건 | 비계 점검 불량·미실시 |
| 2 | `wire insulation msds` | 0.4923 | 2건 | 전선 절연 + MSDS 미비치 동시 |
| 3 | `power tools inspected` | 0.4462 | 1건 | 전동 공구 점검 미이행 |
| 4 | `msds attached material` | 0.4410 | 6건 | 자재 MSDS 미부착 — 가장 넓은 분포 |
| 5 | `stored rigging machine` | 0.4385 | 3건 | 가연성 자재 리깅 기계 내 보관 |
| 6 | `reinstall safety net` | 0.3971 | 4건 | 안전망 재설치 불량 |
| 7 | `cover safety signage` | 0.3750 | 5건 | 덮개·안전 표지판 미설치 |
| 8 | `non standard ladder` | 0.3726 | 2건 | 비표준 사다리 사용 |
| 9 | `stopper damaged rusted` | 0.3577 | 2건 | 파손·녹슨 고임목·스토퍼 |
| 10 | `guide rope concrete` | 0.3359 | 5건 | 콘크리트 호스 가이드 로프 없이 핸들링 |

> **핵심 신호:** `msds attached material` 6건 — 29건 중 21% → 화학물질·가연성 자재 MSDS 관리가 RTCC의 고질적 문제. 화재 4건과 직결

### 4-2. 카테고리별 2–3gram 심층 분석

#### ▶ 떨어짐/낙상 (7건) — 미조치 1건 포함

| 순위 | 키워드 | Score | 항목 수/7 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `damaged rusted scaffolding` | 0.4685 | 1건 | **미조치** — 파손·녹슨 비계 현재 사용 중 |
| 2 | `bad reinstall safety` | 0.4821 | 1건 | 안전망 재설치 불량 |
| 3 | `open concrete pit` | 0.5426 | 1건 | 콘크리트 피트 개구부 미차단 |
| 4 | `ladder soil dumped` | 0.4449 | 2건 | 사다리 주변 토사 투기 — 기반 불안전 |
| 5 | `climbing working rebar` | 0.4108 | 1건 | 철근 위 기어오르며 작업 |

**원인 분석:**
- 7건 중 5개 패턴이 모두 다름 → 추락 관련 단일 집중 원인이 아닌 **기초 안전 의식 전반 미흡**
- `damaged rusted scaffolding` 미조치 = 파손 자재 교체 조달 체계 부재 or 즉각 교체 거부

---

#### ▶ 전도/낙하/부딪힘 (3건) — 중장비 집중

| 순위 | 키워드 | Score | 항목 수/3 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `excavator operator safety` | 0.6547 | 1건 | 굴착기 운전자 안전 미준수 |
| 2 | `concrete pump hose` | 0.6024 | 1건 | 콘크리트 펌프 호스 핸들링 불량 |
| 3 | `pipe handled directly` | 0.5336 | 1건 | 맨손으로 콘크리트 호스 직접 핸들링 |
| 4 | `installed outrigger piling` | 0.3818 | 1건 | 파일링 장비 아우트리거 미설치 |

**원인 분석:**
- 3건 모두 중장비(굴착기·펌프·파일링) 관련 → RTCC 주 업무(콘크리트·토목 공사) 특성상 중장비 안전 절차가 핵심인데 기본 수칙 미이행
- 가이드 로프 없이 콘크리트 호스 맨손 핸들링 → 호스 반동으로 작업자 충격 위험

---

#### ▶ 화재 (4건) — MSDS 연동

| 순위 | 키워드 | Score | 항목 수/4 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `msds flammable materials` | 0.5895 | 2건 | 가연성 자재 MSDS 없이 보관 |
| 2 | `stored rigging machine` | 0.5047 | 1건 | 리깅 기계 내부 가연성(그리스) 보관 |
| 3 | `training welder doing` | 0.3671 | 1건 | 훈련 미이수 용접공이 현장 용접 작업 |

**원인 분석:**
- `msds flammable materials`(2건) + `stored rigging machine`(1건) → 가연성 물질 격리 보관 절차 없음, MSDS 없이 화학물질 취급
- **무자격 용접** — `training welder doing` → 자격 미인증 용접공 현장 투입. 열작업 허가·자격 확인 체계 부재

---

#### ▶ 기타 (13건) — 관리 문서 전반 부재

| 순위 | 키워드 | Score | 항목 수/13 | 인사이트 |
|-----|--------|:-----:|:---------:|---------|
| 1 | `scaffolding inspection checklist` | 0.4880 | 2건 | 비계 점검 체크리스트 미이행 |
| 2 | `safety signage module` | 0.3806 | 3건 | Module GF/Roof 구역 안전 표지 없음 |
| 3 | `inspected washroom tank` | 0.4925 | 2건 | 화장실·탱크 점검 미이행 |
| 4 | `soil collapse rtcc` | 0.2977 | 2건 | RTCC 작업 구역 토사 붕괴 위험 |

> `soil collapse` — 토목 공사 특성상 흙막이·굴착면 붕괴 위험. 유일하게 RTCC 특유의 지반 위험 등장

---

### 4-3. RTCC 종합 위험 구조 진단

```
[근본 원인 Tree]
RTCC 핵심 위험
├── 자재 관리 부재
│   ├── 파손·녹슨 비계 교체 없이 사용 (미조치)
│   ├── MSDS 없는 가연성 자재 보관 (6건)
│   └── 비표준 사다리·공구 사용
├── 중장비 안전 절차 미이행
│   ├── 콘크리트 호스 맨손 핸들링 (가이드 로프 없음)
│   ├── 굴착기 안전 미준수
│   └── 아우트리거 미설치
├── 용접·화기 관리
│   ├── 무자격 용접공 현장 투입
│   └── 가연성 물질 격리 보관 미이행
└── 문서 관리 전반 미흡
    ├── MSDS 미부착 (21% 해당)
    └── 점검 체크리스트 미이행
```

---

## 5. Daemyoung — KeyBERT 심층 분석

> **총 13건 · Major 69.2% · 미조치 1건 · 감전 집중(46.2%)**

### 5-1. 전체 코퍼스 2–3gram 키워드 (Top 15)

| 순위 | 키워드 | KW Score | 관련 항목 수 | 의미 해석 |
|-----|--------|:--------:|:-----------:|---------|
| 1 | `stopper unattended material` | 0.5785 | 5건 | 자재 스토퍼 없음 + 무감시 방치 |
| 2 | `tray work ensure` | 0.4917 | 3건 | 케이블 트레이 작업 절차 준수 요구 |
| 3 | `irresponsible behaviour pdb` | 0.4398 | 1건 | PDB 관련 무책임한 행동 (점검자 직접 명시) |
| 4 | `electric panel access` | 0.4339 | 3건 | 전기 패널 접근 차단·불량 |
| 5 | `work area clean` | 0.4308 | 5건 | 작업 구역 청결 미유지 |
| 6 | `safety regulations` | 0.4188 | 1건 | 안전 규정 전반 미준수 |
| 7 | `date cable termination` | 0.3933 | 4건 | 케이블 단자 처리 날짜·기준 미준수 |
| 8 | `ensure proper housekeeping` | 0.3773 | 4건 | 하우스키핑 지속 요구 (반복 지적) |
| 9 | `material shifting pipe` | 0.3480 | 5건 | 파이프 랙 자재 이동 방법 위반 |
| 10 | `inspection checklist date` | 0.3694 | 2건 | 점검 체크리스트 날짜 만료·미갱신 |

> **핵심 신호:** `irresponsible behaviour pdb` — 점검자가 직접 "무책임한 행동"으로 기재. 단순 절차 위반이 아닌 안전 의식 수준 문제로 점검자가 판단

### 5-2. 카테고리별 2–3gram 심층 분석

#### ▶ 감전/합선 (6건) — Daemyoung의 핵심 위험

| 순위 | 키워드 | Score | 항목 수/6 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `area infront pdb` | 0.5904 | **4건** | PDB 전면 구역 관리 불량 — 67% |
| 2 | `infront pdb water` | 0.5950 | 3건 | PDB 전면 수분 침투·배수 불량 |
| 3 | `pdb access blocked` | 0.6178 | 1건 | PDB 접근 자체 차단 (자재 적재) |
| 4 | `water ingress sockets` | 0.4519 | 2건 | 소켓 연결부 수분 침투 |
| 5 | `cover connections standard` | 0.4265 | 3건 | 비표준 덮개(폴리에틸렌) 연결부 사용 |
| 6 | `cable termination need` | 0.4282 | 1건 | 케이블 단자 처리 미완료 |

**원인 분석:**
1. **PDB 구역 = Daemyoung 위험 집중 지점** — `area infront pdb`(4건), `infront pdb water`(3건), `pdb access blocked`(1건) → PDB 전방에 자재 적재, 배수 불량, 접근 차단이 동시 발생. PDB 관리 책임자 미지정
2. **비표준 임시 처리 관행** — `cover connections standard`(3건) → 폴리에틸렌 봉투로 소켓 덮음. 공식 방수 커버·밀폐 캡 조달 없이 현장에서 임시방편 처리
3. **수분+전기 공존** — `water ingress sockets`(2건) + `infront pdb water`(3건) → SIEL 케이블 트레이 작업 구역 방수 처리 미흡. 전기 설비 인근 누수·지표수 방치

---

#### ▶ 기타 (4건) — 관리 체계 전반

| 순위 | 키워드 | Score | 항목 수/4 | 인사이트 |
|-----|--------|:-----:|:--------:|---------|
| 1 | `clear unattended material` | 0.4454 | 3건 | 무감시 자재 정리 요구 |
| 2 | `inspection date expired` | 0.4697 | 1건 | 점검 만료 자재 계속 전시·사용 |
| 3 | `tray work ensure` | 0.4655 | 1건 | 케이블 트레이 작업 절차 |
| 4 | `material tag inspection` | 0.4004 | 2건 | 자재 점검 태그 관리 미흡 |

> `inspection date expired` — 점검 만료일(2026.01.31)이 지난 자재를 2월에도 계속 전시·사용. 자재 수명 관리 절차 전무

---

### 5-3. Daemyoung 종합 위험 구조 진단

```
[근본 원인 Tree]
Daemyoung 핵심 위험
├── PDB(전기 패널) 관리 부재 ← 46.2% 집중
│   ├── PDB 전방 자재 적재 (접근 차단)
│   ├── PDB 전방 배수 불량 (수분+전기 공존)
│   ├── 소켓 비표준 임시 덮개 (폴리에틸렌)
│   └── 케이블 단자 처리 미완료
├── 자재·장비 관리 부재
│   ├── 점검 만료 자재 계속 사용 (01.31 만료 → 2월 이후 사용)
│   ├── 자재 스토퍼 없음 (5건)
│   └── 파이프 랙 비규격 자재 이동 (로프 묶음 이동 금지 위반)
├── 하우스키핑·5S 미이행
│   ├── 반복 지적에도 개선 없음
│   └── 점검자 "irresponsible behaviour" 직접 기재
└── 신규 투입 적응 미흡
    └── 3월 투입 → 현장 절차 교육 불충분 상태 공정 진입
```

---

## 6. Vendor 간 KeyBERT 교차 비교

### 6-1. 공통 위험 패턴 (복수 Vendor 동시 등장)

| 위험 패턴 | Hankuk C&T | DSHI | RTCC | Daemyoung |
|---------|:----------:|:----:|:----:|:---------:|
| 비계 불량·미점검 | ●(38건) | ●(19건) | ●(미조치) | — |
| 인양 절차 미이행 | ●(42건) | ●(30건) | — | — |
| 접지 미연결 | ●(5건) | ●(5건) | — | — |
| 자재 정리(Housekeeping) | ●(20건) | ●(10건) | — | ●(5건) |
| 바리케이드·코든 미설치 | ●(5건) | ●(18건) | — | — |
| MSDS·서류 미비 | — | ●(8건) | ●(6건) | ●(2건) |
| 장비 사전 점검 미이행 | ●(10건) | ●(12건) | ●(1건) | — |

### 6-2. Vendor별 고유 위험 (타 업체 미등장)

| Vendor | 고유 위험 키워드 | 의미 |
|--------|--------------|-----|
| Hankuk C&T | `work permit work` (19건) | PTW 미발행 무허가 작업 — 타 업체 미기록 |
| Hankuk C&T | `grinder guard used` (20건) | 그라인더 가드 반복 위반 집중 |
| DSHI | `repeated safety violation` | 점검자가 상습 위반으로 명시 |
| DSHI | `cabin door open working` | 장비 캐빈 도어 열림 운전 |
| RTCC | `soil collapse` | 토공·굴착 지반 붕괴 위험 (RTCC 유일 토목 패턴) |
| RTCC | `excavator operator safety` | 굴착기 운용 — RTCC 전담 중장비 |
| Daemyoung | `irresponsible behaviour pdb` | 행동 자체를 무책임으로 점검자 명시 |
| Daemyoung | `water ingress sockets` | PDB 수분 침투 — 전기 작업 특화 위험 |

---

## 7. 즉각 조치 및 우선 개선 과제

### 7-1. 미조치 14건 긴급 조치 순위

| 우선순위 | Vendor | 내용 | 위험 등급 |
|---------|--------|-----|---------|
| ★★★ | Hankuk C&T | 맨발+전선+회전 기계 근접 작업 | **HIGH RISK** |
| ★★★ | RTCC | 파손·녹슨 비계 자재 현재 사용 중 | 5Major |
| ★★★ | Daemyoung | 바닥 노출 볼트 — 걸림·추락 | 5Major |
| ★★ | Hankuk C&T | 노출 케이블 전기 보드 (X 처리) | 3Major |
| ★★ | DSHI | 유압 팔레트 트롤리 NEAR MISS | Minor |
| ★ | RTCC | 콘크리트 트럭 고임목 미설치 | Minor |
| ★ | RTCC | 콘크리트 작업 중 PPE 미착용 | Minor |

### 7-2. KeyBERT 기반 구조적 개선 과제

| 과제 | 대상 | KeyBERT 근거 | 권고 조치 |
|-----|-----|------------|---------|
| 비계 설치 완료 기준 체크리스트 도입 | Hankuk C&T, DSHI, RTCC | `scaffolding outrigger wrong`(19), `unsafe loose scaffolding`(19), `damaged rusted`(미조치) | 아우트리거·가드레일·개구부 차단 3항목 동시 확인 후 사용 허가 |
| 인양 Pre-Lift Check 의무화 | Hankuk C&T, DSHI | `shouldn material lifting`(42), `lifting work barricade`(30) | 인양 전 5분 체크: SWL 확인, 신호수 배치, 하부 통제, 슬링 검수 |
| 접지(Earthing) Pre-use 점검 항목 추가 | DSHI, Hankuk C&T | `body earthing wire`(5), `earthing damaged`(5) | 전동 공구·용접기 사용 전 접지 클램프 연결 확인 필수화 |
| PTW(작업허가서) 이행 강화 | Hankuk C&T | `work permit work`(19건) | 무허가 작업 발견 즉각 작업 중지, PTW 발행 확인 후 재개 |
| PDB 구역 전담 관리 지정 | Daemyoung | `area infront pdb`(4), `pdb access blocked`(1) | PDB 전방 1m 자재 적재 금지 + 수분 침투 일일 점검 |
| MSDS 비치 현장 점검 | RTCC, DSHI | `msds flammable materials`(2), `msds attached material`(6) | 가연성 자재 입고 시 MSDS 동봉 의무화, 월 1회 현장 확인 |
| 개구부 목록 관리 + 일일 점검 | Hankuk C&T | `unsafe opening scaffolding`(38건) | 개구부 위치 도면 관리, 매일 오전 점검자 확인 서명 |
| 무자격 용접 차단 | RTCC | `training welder doing welding` | 열작업 허가 발행 시 자격증 확인 필수 |

---

*본 보고서는 KeyBERT `paraphrase-multilingual-MiniLM-L12-v2`, `keyphrase_ngram_range=(2,3)`, `use_mmr=True`, `diversity=0.4` 설정으로 분석한 결과를 바탕으로 작성됐습니다. 키워드 관련 항목 수(items)는 구성 단어(4자 이상) 기반 교차 검증값입니다.*
