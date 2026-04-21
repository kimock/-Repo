"""
STEP 2: 차트 생성 모듈
new_CSV.csv + 날짜 범위 → 5종 차트

두 가지 사용 방식:
  make_charts()   — PNG 파일로 저장 (로컬 app.py용)
  make_figures()  — Figure 객체 dict 반환 (Streamlit st.pyplot() 직접 사용, 파일 I/O 없음)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from datetime import datetime
import platform

# 운영체제별 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
else:
    print('지원하지 않는 운영체제입니다.')

# ── 스타일 상수 ──────────────────────────────────────────────
NAVY_COLORS = [
    "#001F3F", "#003366", "#00509E",
    "#4A7AB5", "#7BAFD4", "#A3C1AD", "#C8D8E8"
]
SALMON_COLOR = "#FA8072"
LIGHT_NAVY   = "#00509E"
DARK_NAVY    = "#001F3F"

DPI       = 150
TITLE_FS  = 15
LABEL_FS  = 11
DATA_FS   = 9

# ── 레이블 순서 (고정) ──────────────────────────────────────
SDN_ORDER = [
    "떨어짐/낙상", "전도/낙하/부딪힘", "끼임",
    "감전/합선", "화재/탄화", "LEAK", "기타"
]

HANMI_ORDER = [
    "추락", "낙하", "비래", "전도", "협착",
    "충돌", "감전", "화재", "폭발", "붕괴", "기타"
]


def _setup_font():
    candidates = ["Malgun Gothic", "NanumGothic", "AppleGothic", "DejaVu Sans"]
    available  = {f.name for f in fm.fontManager.ttflist}
    for font in candidates:
        if font in available:
            plt.rcParams["font.family"] = font
            break
    plt.rcParams["axes.unicode_minus"] = False


def _charts_dir(base_dir: str) -> str:
    path = os.path.join(base_dir, "charts")
    os.makedirs(path, exist_ok=True)
    return path


# ════════════════════════════════════════════════════════════
# 내부 Figure 빌더 (_fig_*) — 저장 없이 Figure 객체 반환
# ════════════════════════════════════════════════════════════

def _fig_vendor_donut(df: pd.DataFrame, date_label: str) -> plt.Figure:
    counts   = df["vendor"].value_counts()
    labels   = counts.index.tolist()
    values   = counts.values.tolist()
    n        = len(labels)
    colors   = NAVY_COLORS[:n]
    max_idx  = values.index(max(values))
    explode  = [0.05 if i == max_idx else 0 for i in range(n)]

    fig, ax = plt.subplots(figsize=(9, 7))
    wedges, texts, autotexts = ax.pie(
        values, labels=labels,
        autopct=lambda p: f"{p:.1f}%\n({int(round(p * sum(values) / 100))}건)",
        startangle=140, colors=colors, explode=explode,
        pctdistance=0.72,
        wedgeprops={"edgecolor": "white", "linewidth": 2.5},
        textprops={"fontsize": 13, "fontweight": "bold"},
    )
    plt.setp(autotexts, size=10, weight="bold", color="white")

    centre_circle = plt.Circle((0, 0), 0.60, fc="white")
    ax.add_artist(centre_circle)
    ax.text(0, 0, f"총\n{sum(values)}건", ha="center", va="center",
            fontsize=13, fontweight="bold", color=DARK_NAVY)

    ax.set_title(f"Vendor별 안전위반 비중\n{date_label}",
                 fontsize=TITLE_FS, fontweight="bold", pad=18)
    fig.tight_layout()
    return fig


def _fig_sdn_risk_bar(df: pd.DataFrame, date_label: str) -> plt.Figure:
    counts         = df["SDN_risk"].value_counts()
    ordered_counts = [counts.get(label, 0) for label in SDN_ORDER]
    x              = np.arange(len(SDN_ORDER))

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(x, ordered_counts, width=0.6, color=DARK_NAVY, alpha=0.85,
                  edgecolor="white", linewidth=1.2)

    for bar, val in zip(bars, ordered_counts):
        if val > 0:
            ax.annotate(str(val),
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 4), textcoords="offset points",
                        ha="center", va="bottom",
                        fontsize=DATA_FS + 1, fontweight="bold", color=DARK_NAVY)

    ax.set_xticks(x)
    ax.set_xticklabels(SDN_ORDER, fontsize=LABEL_FS, rotation=20, ha="right")
    ax.set_ylabel("발생 건수", fontsize=LABEL_FS, fontweight="bold")
    ax.set_ylim(0, max(ordered_counts) * 1.2 + 1)
    ax.set_title(f"SDN 위험유형별 발생 빈도\n{date_label}",
                 fontsize=TITLE_FS, fontweight="bold", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


def _fig_hanmi_risk_bar(df: pd.DataFrame, date_label: str) -> plt.Figure:
    if "Hanmi_risk" not in df.columns:
        return None

    counts         = df["Hanmi_risk"].value_counts()
    ordered_counts = [counts.get(label, 0) for label in HANMI_ORDER]
    x              = np.arange(len(HANMI_ORDER))

    fig, ax = plt.subplots(figsize=(13, 6))
    bars = ax.bar(x, ordered_counts, width=0.6, color=LIGHT_NAVY, alpha=0.85,
                  edgecolor="white", linewidth=1.2)

    for bar, val in zip(bars, ordered_counts):
        if val > 0:
            ax.annotate(str(val),
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 4), textcoords="offset points",
                        ha="center", va="bottom",
                        fontsize=DATA_FS + 1, fontweight="bold", color=LIGHT_NAVY)

    ax.set_xticks(x)
    ax.set_xticklabels(HANMI_ORDER, fontsize=LABEL_FS, rotation=20, ha="right")
    ax.set_ylabel("발생 건수", fontsize=LABEL_FS, fontweight="bold")
    ax.set_ylim(0, max(ordered_counts) * 1.2 + 1)
    ax.set_title(f"한미 위험유형별 발생 빈도\n{date_label}",
                 fontsize=TITLE_FS, fontweight="bold", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


def _fig_weekly_trend(df: pd.DataFrame, date_label: str) -> plt.Figure:
    df         = df.copy()
    df["date_dt"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")
    df["week"] = df["date_dt"].dt.strftime("%Y-W%V")
    weekly     = df.groupby("week").size().reset_index(name="count").sort_values("week")
    x          = np.arange(len(weekly))

    fig, ax = plt.subplots(figsize=(max(10, len(weekly) * 1.2), 5))
    ax.plot(x, weekly["count"], color=SALMON_COLOR, marker="o",
            linewidth=2.5, markersize=8,
            markeredgecolor="white", markeredgewidth=1.5, label="주간 발생 건수")
    ax.fill_between(x, weekly["count"], alpha=0.15, color=SALMON_COLOR)

    for xi, yi in zip(x, weekly["count"]):
        ax.annotate(str(yi), xy=(xi, yi), xytext=(0, 8),
                    textcoords="offset points", ha="center", va="bottom",
                    fontsize=DATA_FS, fontweight="bold", color=SALMON_COLOR)

    ax.set_xticks(x)
    ax.set_xticklabels(weekly["week"], fontsize=LABEL_FS - 1, rotation=35, ha="right")
    ax.set_ylabel("발생 건수", fontsize=LABEL_FS, fontweight="bold")
    ax.set_ylim(0, weekly["count"].max() * 1.3 + 1)
    ax.set_title(f"주차별 안전위반 발생 빈도\n{date_label}",
                 fontsize=TITLE_FS, fontweight="bold", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    ax.legend(fontsize=LABEL_FS - 1)
    fig.tight_layout()
    return fig


def _fig_location_proportion(df: pd.DataFrame, date_label: str) -> plt.Figure:
    counts = df["location"].value_counts().sort_values(ascending=True)
    total  = counts.sum()
    pcts   = (counts / total * 100).round(1)
    n      = len(counts)
    colors = NAVY_COLORS[:n][::-1]

    fig, ax = plt.subplots(figsize=(10, max(4, n * 0.9)))
    bars = ax.barh(counts.index, pcts.values, color=colors,
                   edgecolor="white", linewidth=1.2, height=0.55)

    for bar, pct, cnt in zip(bars, pcts.values, counts.values):
        ax.annotate(f"{pct}%  ({cnt}건)",
                    xy=(bar.get_width(), bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0), textcoords="offset points",
                    ha="left", va="center",
                    fontsize=DATA_FS + 1, fontweight="bold", color=DARK_NAVY)

    ax.set_xlabel("비중 (%)", fontsize=LABEL_FS, fontweight="bold")
    ax.set_xlim(0, pcts.max() * 1.3)
    ax.set_title(f"Location별 안전위반 비중\n{date_label}",
                 fontsize=TITLE_FS, fontweight="bold", pad=14)
    ax.spines[["top", "right"]].set_visible(False)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
    fig.tight_layout()
    return fig


# ════════════════════════════════════════════════════════════
# 공개 API — 파일 저장용 (로컬 app.py)
# ════════════════════════════════════════════════════════════

def chart_vendor_donut(df, out_dir, date_label):
    fig = _fig_vendor_donut(df, date_label)
    fig.savefig(os.path.join(out_dir, "vendor_donut.png"), dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  [OK] vendor_donut.png saved")


def chart_sdn_risk_bar(df, out_dir, date_label):
    fig = _fig_sdn_risk_bar(df, date_label)
    fig.savefig(os.path.join(out_dir, "sdn_risk_bar.png"), dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  [OK] sdn_risk_bar.png saved")


def chart_hanmi_risk_bar(df, out_dir, date_label):
    fig = _fig_hanmi_risk_bar(df, date_label)
    if fig is None:
        print("  [SKIP] Hanmi_risk 컬럼 없음")
        return
    fig.savefig(os.path.join(out_dir, "hanmi_risk_bar.png"), dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  [OK] hanmi_risk_bar.png saved")


def chart_weekly_trend(df, out_dir, date_label):
    fig = _fig_weekly_trend(df, date_label)
    fig.savefig(os.path.join(out_dir, "weekly_trend_line.png"), dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  [OK] weekly_trend_line.png saved")


def chart_location_proportion(df, out_dir, date_label):
    fig = _fig_location_proportion(df, date_label)
    fig.savefig(os.path.join(out_dir, "location_proportion.png"), dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print("  [OK] location_proportion.png saved")


# ════════════════════════════════════════════════════════════
# 공개 API — Figure 반환용 (배포용 app_cloud.py)
# ════════════════════════════════════════════════════════════

def make_figures(
    start_date: datetime,
    end_date:   datetime,
    df:         pd.DataFrame,
) -> dict:
    """
    날짜 범위로 필터된 DataFrame에서 5종 Figure를 생성해 dict로 반환.
    파일 저장 없음 — st.pyplot(fig)에 직접 전달 가능.

    Returns:
        {
            "vendor_donut":        plt.Figure,
            "sdn_risk_bar":        plt.Figure,
            "hanmi_risk_bar":      plt.Figure | None,
            "weekly_trend_line":   plt.Figure,
            "location_proportion": plt.Figure,
        }
    Raises:
        ValueError: 해당 기간 데이터 없음
    """
    _setup_font()

    mask = (
        (df["date_dt"] >= pd.Timestamp(start_date)) &
        (df["date_dt"] <= pd.Timestamp(end_date))
    )
    df_f = df[mask].copy()

    if df_f.empty:
        raise ValueError(
            f"선택한 기간({start_date.strftime('%Y.%m.%d')} ~ "
            f"{end_date.strftime('%Y.%m.%d')})에 데이터가 없습니다."
        )

    date_label = (
        f"{start_date.strftime('%Y.%m.%d')} ~ {end_date.strftime('%Y.%m.%d')}"
    )

    return {
        "vendor_donut":        _fig_vendor_donut(df_f, date_label),
        "sdn_risk_bar":        _fig_sdn_risk_bar(df_f, date_label),
        "hanmi_risk_bar":      _fig_hanmi_risk_bar(df_f, date_label),
        "weekly_trend_line":   _fig_weekly_trend(df_f, date_label),
        "location_proportion": _fig_location_proportion(df_f, date_label),
    }


# ════════════════════════════════════════════════════════════
# 공개 API — 파일 저장 일괄 (로컬 app.py)
# ════════════════════════════════════════════════════════════

def make_charts(
    start_date: datetime,
    end_date:   datetime,
    csv_path:   str = "new_CSV.csv",
) -> str:
    """날짜 범위 내 데이터로 5종 차트를 charts/ 폴더에 PNG로 저장. Returns: charts 경로."""
    _setup_font()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, csv_path) if not os.path.isabs(csv_path) else csv_path

    print(f"\n[STEP 2] 차트 생성 시작")
    print(f"  · 기간: {start_date.strftime('%Y.%m.%d')} ~ {end_date.strftime('%Y.%m.%d')}")

    df = pd.read_csv(csv_file, encoding="utf-8-sig")
    df["date_dt"] = pd.to_datetime(df["date"], format="%d.%m.%Y", errors="coerce")

    mask       = (df["date_dt"] >= pd.Timestamp(start_date)) & \
                 (df["date_dt"] <= pd.Timestamp(end_date))
    df_filtered = df[mask].copy()

    if df_filtered.empty:
        raise ValueError(
            f"선택한 기간({start_date.strftime('%Y.%m.%d')} ~ "
            f"{end_date.strftime('%Y.%m.%d')})에 데이터가 없습니다."
        )

    print(f"  · 필터 결과: {len(df_filtered)}건")

    date_label = f"{start_date.strftime('%Y.%m.%d')} ~ {end_date.strftime('%Y.%m.%d')}"
    charts_dir = _charts_dir(base_dir)

    chart_vendor_donut(df_filtered, charts_dir, date_label)
    chart_sdn_risk_bar(df_filtered, charts_dir, date_label)
    chart_hanmi_risk_bar(df_filtered, charts_dir, date_label)
    chart_weekly_trend(df_filtered, charts_dir, date_label)
    chart_location_proportion(df_filtered, charts_dir, date_label)

    print(f"[STEP 2] 완료 → {charts_dir}")
    return charts_dir


if __name__ == "__main__":
    from step1_csv_mapper import run as run_mapper
    run_mapper()

    df_all = pd.read_csv(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "new_CSV.csv"),
        encoding="utf-8-sig"
    )
    df_all["date_dt"] = pd.to_datetime(df_all["date"], format="%d.%m.%Y", errors="coerce")
    make_charts(df_all["date_dt"].min().to_pydatetime(),
                df_all["date_dt"].max().to_pydatetime())
