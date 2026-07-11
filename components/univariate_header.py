from pathlib import Path

import streamlit as st

from utils.icons import get_svg

IMAGE_PATH = Path("static/images/univariate-header-logo.png")

analysis_icon = get_svg("chart-no-axes-combined")

def render() -> None:
    """
    Render the header section for the Univariate Analysis page.
    """

    left, right = st.columns([2.2, 0.5])

    with left:
        st.markdown(
            f'<div class="hero"> <div class="hero-badge"> {analysis_icon} Exploratory Data Analysis </div> <div class="hero-title"> Univariate Analysis </div> <div class="hero-subtitle"> Analyze individual features of the banking transaction dataset through descriptive statistics and interactive visualizations. Explore the distribution, spread, central tendency, and frequency of both numerical and categorical variables. </div> </div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            '<div margin-top: 2rem>',
            unsafe_allow_html=True
        )
        if IMAGE_PATH.exists():
            st.image(
                str(IMAGE_PATH),
            )