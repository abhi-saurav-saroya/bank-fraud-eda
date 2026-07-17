from pathlib import Path

import streamlit as st

from utils.icons import get_svg

IMAGE_PATH = Path("static/images/security-recommendations-header-logo.png")

recommendation_icon = get_svg("shield-check")

def render() -> None:
    """
    Render the header section for the Security Recommendations page.
    """

    left, right = st.columns([2.2, 0.5])

    with left:
        st.markdown(
            f'<div class="hero"> <div class="hero-badge"> {recommendation_icon} Security Recommendations </div> <div class="hero-title"> Fraud Prevention Strategies </div> <div class="hero-subtitle"> Based on the insights obtained from the exploratory data analysis, this section presents practical security recommendations aimed at reducing fraudulent transactions. The proposed measures focus on strengthening authentication, improving transaction monitoring, enhancing risk assessment, and supporting proactive fraud prevention within banking systems. </div> </div>',
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