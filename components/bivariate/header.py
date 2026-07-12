from pathlib import Path

import streamlit as st

from utils.icons import get_svg

IMAGE_PATH = Path("static/images/bivariate-header-logo.png")

analysis_icon = get_svg("chart-scatter")

def render():
    """
    Render the bivariate analysis header.
    """

    left, right = st.columns([2.2, 0.5])

    with left:
        st.markdown(
            f'<div class="hero"> <div class="hero-badge"> {analysis_icon} Relationship Analysis </div> <div class="hero-title"> Bivariate Analysis </div> <div class="hero-subtitle"> Explore relationships between two variables to understand how customer attributes, transaction characteristics and behavioural patterns influence fraudulent transactions. </div> </div>',
            unsafe_allow_html=True,
        )

    with right:
        if IMAGE_PATH.exists():
            st.markdown(
                '<div margin-top: 2rem>',
                unsafe_allow_html=True
            )
            st.image(
                str(IMAGE_PATH),
                width='stretch',
            )