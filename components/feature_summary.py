import pandas as pd
import plotly.express as px
import streamlit as st

from components.metric_card import render as render_metric_card
from utils.icons import get_svg


NUMERIC_ICON = get_svg("calculator")
CATEGORY_ICON = get_svg("list")
BINARY_ICON = get_svg("binary")
TARGET_ICON = get_svg("shield-check")


def render(df):
    """
    Render feature summary section.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Feature Summary </h2> <div class="section-subtitle"> Overview of feature types and target variable. </div> </div>',
        unsafe_allow_html=True,
    )


    binary_cols_list = [col for col in df.columns if df[col].nunique() == 2]
    binary_cols = len(binary_cols_list)
    remaining_df = df.drop(columns=binary_cols_list)
    numeric_cols = len(remaining_df.select_dtypes(include="number").columns)
    categorical_cols = len(remaining_df.select_dtypes(include=["object", "category", "datetime"]).columns)


    left, right = st.columns([1.4, 1])

    with left:
        c1, c2 = st.columns(2)

        with c1:
            render_metric_card(
                icon=NUMERIC_ICON,
                value=numeric_cols,
                label="Numeric Features",
            )

        with c2:
            render_metric_card(
                icon=CATEGORY_ICON,
                value=categorical_cols,
                label="Categorical Features",
            )

        st.markdown("<br>", unsafe_allow_html=True)

        c3, c4 = st.columns(2)

        with c3:
            render_metric_card(
                icon=BINARY_ICON,
                value=binary_cols,
                label="Binary Features",
            )

        with c4:
            render_metric_card(
                icon=TARGET_ICON,
                value="is_fraud",
                label="Target Variable",
            )


    with right:
        summary = pd.DataFrame(
            {
                "Feature Type": [
                    "Numeric",
                    "Categorical",
                    "Binary",
                ],
                "Count": [
                    numeric_cols,
                    categorical_cols,
                    binary_cols,
                ],
            }
        )

        fig = px.pie(
            data_frame=summary,
            names="Feature Type",
            values="Count",
            hole=0.65,
        )

        fig.update_layout(
            margin=dict(
                l=10,
                r=10,
                t=10,
                b=10,
            ),
            showlegend=True,
            height=360,
        )

        st.plotly_chart(
            fig,
            width='stretch',
        )