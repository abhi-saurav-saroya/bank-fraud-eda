from pathlib import Path

import streamlit as st

from utils.icons import get_svg

IMAGE_PATH = Path("static/images/multivariate-header-logo.png")

result_icon = get_svg("lightbulb")

def render() -> None:
    """
    Render the header section for the Final Insights page.
    """

    left, right = st.columns([2.2, 0.5])

    with left:
        st.markdown(
            f'<div class="hero"> <div class="hero-badge"> {result_icon}  Final Results </div> <div class="hero-title"> Final Insights </div> <div class="hero-subtitle"> Explore the most significant findings uncovered during the exploratory data analysis. This section highlights the strongest fraud indicators, customer behaviour patterns and business observations supported by the analyses performed throughout the dashboard, providing a concise summary of the most actionable insights. </div> </div>',
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