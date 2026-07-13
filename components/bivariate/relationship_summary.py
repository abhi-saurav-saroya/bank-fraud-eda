import streamlit as st

from components.metric_card import render as render_metric_card
from utils.icons import get_svg


CORRELATION_ICON = get_svg("chart-scatter")
TREND_ICON = get_svg("activity")
GROUP_ICON = get_svg("layers")
UNIQUE_ICON = get_svg("fingerprint-pattern")
TARGET_ICON = get_svg("badge-check")
MISSING_ICON = get_svg("circle-off")
PAIR_ICON = get_svg("git-compare")


def render(df, x_feature, y_feature, x_type, y_type):
    """
    Render summary metrics for the selected relationship.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Relationship Summary </h2> <div class="section-subtitle"> Key statistics describing the selected relationship. </div> </div>',
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)


    if x_type == "Numerical" and y_type == "Numerical":

        corr = df[x_feature].corr(df[y_feature])

        if abs(corr) >= 0.8:
            relation = "Very Strong"

        elif abs(corr) >= 0.6:
            relation = "Strong"

        elif abs(corr) >= 0.4:
            relation = "Moderate"

        elif abs(corr) >= 0.2:
            relation = "Weak"

        else:
            relation = "Very Weak"

        missing = (
            df[[x_feature, y_feature]]
            .isna()
            .sum()
            .sum()
        )

        samples = len(df)

        with c1:
            render_metric_card(
                icon=CORRELATION_ICON,
                value=f"{corr:.3f}",
                label="Correlation",
            )

        with c2:
            render_metric_card(
                icon=TREND_ICON,
                value=relation,
                label="Relationship",
            )

        with c3:
            render_metric_card(
                icon=PAIR_ICON,
                value=f"{samples:,}",
                label="Samples",
            )

        with c4:
            render_metric_card(
                icon=MISSING_ICON,
                value=missing,
                label="Missing Values",
            )



    elif (
        (x_type == "Numerical" and y_type != "Numerical")
        or
        (y_type == "Numerical" and x_type != "Numerical")
    ):

        if x_type == "Numerical":
            num = x_feature
            cat = y_feature
        else:
            num = y_feature
            cat = x_feature

        grouped = df.groupby(cat)[num].mean()

        highest = grouped.idxmax()
        lowest = grouped.idxmin()

        groups = df[cat].nunique()

        missing = (
            df[[num, cat]]
            .isna()
            .sum()
            .sum()
        )

        with c1:
            render_metric_card(
                icon=GROUP_ICON,
                value=groups,
                label="Groups",
            )

        with c2:
            render_metric_card(
                icon=TARGET_ICON,
                value=str(highest),
                label="Highest Mean",
            )

        with c3:
            render_metric_card(
                icon=TREND_ICON,
                value=str(lowest),
                label="Lowest Mean",
            )

        with c4:
            render_metric_card(
                icon=MISSING_ICON,
                value=missing,
                label="Missing Values",
            )



    else:

        unique_x = df[x_feature].nunique()
        unique_y = df[y_feature].nunique()

        pair_counts = (
            df.groupby([x_feature, y_feature])
            .size()
            .sort_values(ascending=False)
        )

        top_pair = pair_counts.index[0]
        total_pairs = len(pair_counts)

        with c1:
            render_metric_card(
                icon=UNIQUE_ICON,
                value=unique_x,
                label=f"{x_feature.replace('_', ' ').title()} Values",
            )

        with c2:
            render_metric_card(
                icon=UNIQUE_ICON,
                value=unique_y,
                label=f"{y_feature.replace('_', ' ').title()} Values",
            )

        with c3:
            render_metric_card(
                icon=PAIR_ICON,
                value=f"{top_pair[0]} x {top_pair[1]}",
                label="Most Common Pair",
            )

        with c4:
            render_metric_card(
                icon=GROUP_ICON,
                value=total_pairs,
                label="Unique Pairs",
            )