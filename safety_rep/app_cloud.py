"""
안전점검 데이터 분석 대시보드 — 배포용 (Streamlit Cloud)
실행: streamlit run app_cloud.py

· ML 의존성 없음 (keybert / sentence-transformers / torch 불필요)
· new_CSV.csv를 업로드하거나, 레포에 포함된 파일을 자동으로 사용
· 날짜 범위 선택 → 차트 즉시 생성 (파일 저장 없이 st.pyplot() 직접 렌더링)
"""

import os
import io
import pandas as pd
import streamlit as st
from datetime import datetime

from step2_chart_maker import make_figures

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BUNDLED_CSV = os.path.join(BASE_DIR, "new_CSV.csv")

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="안전점검 분석 대시보드",
    page_icon="🦺",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main { background: #f0f3f8; }
[data-testid="stAppViewContainer"]          { background: #f0f3f8; }
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e2e8f0;
}

.dash-header {
    background: linear-gradient(135deg, #001F3F 0%, #00509E 100%);
    border-radius: 16px; padding: 1.6rem 2.2rem;
    margin-bottom: 1.6rem;
}
.dash-title { font-size: 1.9rem; font-weight: 900; color: white; margin: 0; }
.dash-sub   { font-size: 0.9rem; color: rgba(255,255,255,0.72); margin: 0.4rem 0 0; }
.filter-badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 20px; padding: 0.25rem 0.9rem;
    font-size: 0.82rem; color: white; margin-top: 0.8rem; font-weight: 600;
}

.kpi-card {
    background: white; border-radius: 14px;
    padding: 1.2rem 1.5rem;
    box-shadow: 0 2px 12px rgba(0,31,63,0.08);
    border-top: 4px solid #001F3F;
}
.kpi-label {
    font-size: 0.72rem; font-weight: 700; color: #94a3b8;
    text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.5rem;
}
.kpi-value { font-size: 2rem; font-weight: 900; color: #001F3F; line-height: 1; margin-bottom: 0.3rem; }
.kpi-sub   { font-size: 0.8rem; color: #64748b; }

.section-header {
    font-size: 1.1rem; font-weight: 800; color: #001F3F;
    padding-bottom: 0.5rem; border-bottom: 2px solid #001F3F;
    margin: 1.4rem 0 1.2rem;
}

.chart-card {
    background: white; border-radius: 14px;
    padding: 1.2rem 1.4rem 0.6rem;
    box-shadow: 0 2px 12px rgba(0,31,63,0.08);
    margin-bottom: 1.2rem;
}
.chart-card-title { font-size: 1rem; font-weight: 800; color: #001F3F; margin-bottom: 0.2rem; }
.chart-card-desc  {
    font-size: 0.78rem; color: #94a3b8; margin-bottom: 0.8rem;
    padding-bottom: 0.8rem; border-bottom: 1px solid #f1f5f9;
}
</style>
""", unsafe_allow_html=True)


# ── 데이터 로드 ──────────────────────────────────────────────
@st.cache_data
def parse_csv(raw_bytes: bytes) -> pd.DataFrame:
    df = pd.read_csv(io.BytesIO(raw_bytes), encoding="utf-8-sig")
    df["date_dt"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
    return df

@st.cache_data
def load_bundled() -> pd.DataFrame | None:
    if not os.path.exists(BUNDLED_CSV):
        return None
    df = pd.read_csv(BUNDLED_CSV, encoding="utf-8-sig")
    df["date_dt"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
    return df


# ── 사이드바 ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🦺 안전점검 대시보드")
    st.markdown("---")

    # CSV 업로드
    st.markdown("**📂 데이터 불러오기**")
    uploaded = st.file_uploader(
        "new_CSV.csv 업로드",
        type=["csv"],
        help="STEP 1로 생성된 new_CSV.csv 파일을 업로드하세요.",
    )

    if uploaded:
        df = parse_csv(uploaded.read())
        st.success(f"업로드 완료 — {len(df)}건")
    else:
        df = load_bundled()
        if df is not None:
            st.info(f"기본 파일 사용 — {len(df)}건")
        else:
            st.warning("new_CSV.csv 파일을 업로드해주세요.")
            st.stop()

    # 날짜 범위
    st.markdown("---")
    st.markdown("**📅 분석 기간 설정**")
    min_date = df["date_dt"].min().date()
    max_date = df["date_dt"].max().date()
    st.caption(f"데이터 범위: {min_date} ~ {max_date}")

    start_date = st.date_input("시작일", value=min_date, min_value=min_date, max_value=max_date)
    end_date   = st.date_input("종료일", value=max_date, min_value=min_date, max_value=max_date)

    if start_date > end_date:
        st.error("시작일이 종료일보다 늦을 수 없습니다.")
        st.stop()

    run_btn = st.button("▶ 차트 생성", use_container_width=True, type="primary")

    st.markdown("---")
    st.markdown(
        "**사용법**\n"
        "1. new_CSV.csv 업로드 (또는 기본 파일 사용)\n"
        "2. 분석 기간 선택\n"
        "3. **차트 생성** 클릭\n\n"
        "날짜만 바꿔 반복 실행할 수 있습니다."
    )


# ── 탭 ──────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["📊 대시보드", "📋 데이터", "⬇ 다운로드"])


# ════════════════════════════════════════════════════════════
# Tab 1: 대시보드
# ════════════════════════════════════════════════════════════
with tab1:

    # 헤더 (항상 표시)
    badge = f"📅 {start_date} ~ {end_date}"
    st.markdown(f"""
    <div class="dash-header">
        <div class="dash-title">🦺 안전점검 데이터 분석 대시보드</div>
        <div class="dash-sub">날짜 범위를 선택하고 차트 생성 버튼을 누르세요</div>
        <div class="filter-badge">{badge}</div>
    </div>
    """, unsafe_allow_html=True)

    if not run_btn and "figs" not in st.session_state:
        st.info("사이드바에서 기간을 설정하고 **▶ 차트 생성** 버튼을 클릭하세요.")
        st.stop()

    # 차트 생성
    if run_btn:
        with st.spinner("차트 생성 중..."):
            try:
                figs = make_figures(
                    start_date=datetime.combine(start_date, datetime.min.time()),
                    end_date=datetime.combine(end_date,   datetime.min.time()),
                    df=df,
                )
                st.session_state["figs"]         = figs
                st.session_state["fig_start"]    = start_date
                st.session_state["fig_end"]      = end_date
                st.session_state["fig_df_mask"]  = (
                    (df["date_dt"].dt.date >= start_date) &
                    (df["date_dt"].dt.date <= end_date)
                )
            except ValueError as e:
                st.error(str(e))
                st.stop()

    figs    = st.session_state["figs"]
    df_view = df[st.session_state["fig_df_mask"]]

    # ── KPI 카드 ──────────────────────────────────────────────
    st.markdown('<div class="section-header">핵심 지표</div>', unsafe_allow_html=True)

    total_cnt    = len(df_view)
    top_vendor   = df_view["vendor"].value_counts().idxmax()
    top_vendor_n = df_view["vendor"].value_counts().max()
    top_risk     = df_view["SDN_risk"].value_counts().idxmax() if "SDN_risk" in df_view.columns else "-"
    top_risk_n   = df_view["SDN_risk"].value_counts().max()    if "SDN_risk" in df_view.columns else 0
    comp_rate    = (
        (df_view["is_completed"].str.strip().str.lower() == "yes").mean() * 100
        if "is_completed" in df_view.columns else 0.0
    )
    comp_color = "#2ecc71" if comp_rate >= 80 else "#e74c3c"
    comp_label = "양호" if comp_rate >= 80 else "미흡 — 조치 필요"

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-label">총 안전위반 건수</div>
            <div class="kpi-value">{total_cnt:,}</div>
            <div class="kpi-sub">건</div>
        </div>""", unsafe_allow_html=True)
    with k2:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-label">최다 위반 Vendor</div>
            <div class="kpi-value" style="font-size:1.4rem">{top_vendor}</div>
            <div class="kpi-sub">{top_vendor_n}건 발생</div>
        </div>""", unsafe_allow_html=True)
    with k3:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-label">최다 위험유형 (SDN)</div>
            <div class="kpi-value" style="font-size:1.3rem">{top_risk}</div>
            <div class="kpi-sub">{top_risk_n}건 발생</div>
        </div>""", unsafe_allow_html=True)
    with k4:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{comp_color}">
            <div class="kpi-label">조치 완료율</div>
            <div class="kpi-value" style="color:{comp_color}">{comp_rate:.1f}%</div>
            <div class="kpi-sub">{comp_label}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 차트 렌더링 헬퍼 ──────────────────────────────────────
    CHART_META = {
        "vendor_donut":        ("Vendor별 안전위반 비중",     "업체별 안전위반 건수의 상대적 비중을 보여줍니다."),
        "sdn_risk_bar":        ("SDN 위험유형별 발생 빈도",   "SDN 기준 7개 유형의 발생 빈도를 고정 순서로 비교합니다."),
        "hanmi_risk_bar":      ("한미 위험유형별 발생 빈도",  "한미 기준 11개 유형의 발생 빈도를 고정 순서로 비교합니다."),
        "weekly_trend_line":   ("주차별 발생 빈도 추이",      "주 단위 발생 건수의 시계열 흐름을 나타냅니다."),
        "location_proportion": ("Location별 발생 비중",       "현장 위치별 안전위반 발생 비중을 비교합니다."),
    }

    def render_chart(key: str, col=None):
        ctx = col if col else st
        title, desc = CHART_META[key]
        ctx.markdown(f"""<div class="chart-card">
            <div class="chart-card-title">{title}</div>
            <div class="chart-card-desc">{desc}</div>
        </div>""", unsafe_allow_html=True)
        fig = figs.get(key)
        if fig:
            ctx.pyplot(fig, use_container_width=True)
        else:
            ctx.warning(f"{key} 차트를 생성할 수 없습니다.")

    # ── 1행: Vendor 도넛 | 주차별 추이 ───────────────────────
    st.markdown('<div class="section-header">분석 차트</div>', unsafe_allow_html=True)
    col_l, col_r = st.columns(2, gap="medium")
    render_chart("vendor_donut",      col_l)
    render_chart("weekly_trend_line", col_r)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 2행: SDN | 한미 (나란히 비교) ────────────────────────
    st.markdown("""
    <div style="background:#e8f0fe; border-radius:10px; padding:0.6rem 1rem;
                margin-bottom:1rem; font-size:0.85rem; color:#001F3F; font-weight:600;">
        ⚖️ 동일 데이터를 SDN 분류 기준과 한미 분류 기준으로 각각 집계한 결과입니다.
    </div>
    """, unsafe_allow_html=True)
    col_l, col_r = st.columns(2, gap="medium")
    render_chart("sdn_risk_bar",   col_l)
    render_chart("hanmi_risk_bar", col_r)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── 3행: Location (전체 폭) ───────────────────────────────
    render_chart("location_proportion")


# ════════════════════════════════════════════════════════════
# Tab 2: 데이터 테이블
# ════════════════════════════════════════════════════════════
with tab2:
    if "fig_df_mask" not in st.session_state:
        st.info("대시보드 탭에서 차트를 먼저 생성하세요.")
    else:
        df_show = df[st.session_state["fig_df_mask"]].drop(columns=["date_dt"], errors="ignore")
        f_start = st.session_state["fig_start"]
        f_end   = st.session_state["fig_end"]

        st.markdown(f"**기간 {f_start} ~ {f_end} · {len(df_show)}건**")

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("총 건수",   f"{len(df_show)}건")
        m2.metric("Vendor 수", df_show["vendor"].nunique())
        m3.metric("완료율",
                  f"{(df_show['is_completed'].str.strip().str.lower() == 'yes').mean()*100:.1f}%"
                  if "is_completed" in df_show.columns else "-")
        m4.metric("Location",  df_show["location"].nunique() if "location" in df_show.columns else "-")

        st.dataframe(df_show, use_container_width=True, height=420)


# ════════════════════════════════════════════════════════════
# Tab 3: 다운로드
# ════════════════════════════════════════════════════════════
with tab3:
    if "fig_df_mask" not in st.session_state:
        st.info("대시보드 탭에서 차트를 먼저 생성하세요.")
    else:
        df_dl = df[st.session_state["fig_df_mask"]].drop(columns=["date_dt"], errors="ignore")
        f_start = st.session_state["fig_start"]
        f_end   = st.session_state["fig_end"]

        st.markdown("### 데이터 다운로드")
        csv_bytes = df_dl.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
        st.download_button(
            label="⬇ 필터링된 데이터 CSV 다운로드",
            data=csv_bytes,
            file_name=f"safety_report_{f_start}_{f_end}.csv",
            mime="text/csv",
            use_container_width=True,
        )

        st.markdown("### 차트 이미지 다운로드")
        figs = st.session_state.get("figs", {})
        for key, (title, _) in CHART_META.items():
            fig = figs.get(key)
            if fig is None:
                continue
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
            buf.seek(0)
            st.download_button(
                label=f"⬇ {title} (PNG)",
                data=buf,
                file_name=f"{key}_{f_start}_{f_end}.png",
                mime="image/png",
                use_container_width=True,
            )
