import pandas as pd

import streamlit as st

from components.metric_card import render as render_metric_card
from utils.icons import get_svg


MEAN_ICON = get_svg("sigma")
MEDIAN_ICON = get_svg("chart-column")
STD_ICON = get_svg("chart-no-axes-column")
MISSING_ICON = get_svg("circle-off")
UNIQUE_ICON = get_svg("fingerprint-pattern")
MODE_ICON = get_svg("star")
CATEGORY_ICON = get_svg("list")
TRUE_ICON = get_svg("badge-check")
FALSE_ICON = get_svg("badge-x")


def render(df, feature_type, feature):
    """
    Render summary cards for the selected feature.
    """

    series = df[feature]

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Feature Summary </h2> <div class="section-subtitle"> Quick statistics for the selected feature. </div> </div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)


    if feature_type == "Numerical":
        mean = series.mean()
        median = series.median()
        std = series.std()
        missing = series.isna().sum()

        with c1:
            render_metric_card(
                icon=MEAN_ICON,
                value=f"{mean:.2f}",
                label="Mean",
            )

        with c2:
            render_metric_card(
                icon=MEDIAN_ICON,
                value=f"{median:.2f}",
                label="Median",
            )

        with c3:
            render_metric_card(
                icon=STD_ICON,
                value=f"{std:.2f}",
                label="Std. Deviation",
            )

        with c4:
            render_metric_card(
                icon=MISSING_ICON,
                value=missing,
                label="Missing Values",
            )

    
    elif feature_type == "Categorical" or feature_type == "Discrete Numerical":
        unique = series.nunique()
        mode = series.mode().iloc[0] if not series.mode().empty else "-"
        least = (
            series.value_counts().index[-1]
            if len(series.value_counts()) > 0
            else "-"
        )
        missing = series.isna().sum()

        with c1:
            render_metric_card(
                icon=UNIQUE_ICON,
                value=unique,
                label="Unique Values",
            )

        with c2:
            render_metric_card(
                icon=MODE_ICON,
                value=mode,
                label="Most Frequent",
            )

        with c3:
            render_metric_card(
                icon=CATEGORY_ICON,
                value=least,
                label="Least Frequent",
            )

        with c4:
            render_metric_card(
                icon=MISSING_ICON,
                value=missing,
                label="Missing Values",
            )

    
    elif feature_type == "Binary":
        counts = series.value_counts()
        zeros = counts.get(0, 0)
        ones = counts.get(1, 0)
        missing = series.isna().sum()
        positive = (ones / len(series)) * 100

        with c1:
            render_metric_card(
                icon=TRUE_ICON,
                value=ones,
                label="Positive Count",
            )

        with c2:
            render_metric_card(
                icon=FALSE_ICON,
                value=zeros,
                label="Negative Count",
            )

        with c3:
            render_metric_card(
                icon=MODE_ICON,
                value=f"{positive:.2f}%",
                label="Positive %",
            )

        with c4:
            render_metric_card(
                icon=MISSING_ICON,
                value=missing,
                label="Missing Values",
            )