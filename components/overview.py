import streamlit as st

from utils.icons import get_svg

target_icon = get_svg("target")
analysis_icon = get_svg("chart-candlestick")
lightbulb_icon = get_svg("lightbulb")

def render():

    st.markdown('<div class="section">', unsafe_allow_html=True)

    st.markdown(
        '<h2 class="section-title"> Project Overview </h2> <div class="section-subtitle"> This dashboard presents an interactive exploratory data analysis of banking transactions to identify fraud patterns, understand customer behaviour, and generate actionable business insights. </div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f'<div class="overview-card"> <div class="overview-icon">{target_icon}</div> <h3 class="card-title">Objective</h3> <p class="card-description"> Identify transaction patterns associated with fraudulent activities and assist financial institutions in improving fraud prevention strategies.</p> </div>',
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            f'<div class="overview-card"> <div class="overview-icon">{analysis_icon}</div> <h3 class="card-title">Analysis</h3> <p class="card-description"> Perform univariate, bivariate, correlation and multivariate analyses to understand the behaviour of legitimate and fraudulent transactions. </p> </div>',
            unsafe_allow_html=True,
        )

    with col3:

        st.markdown(
            f'<div class="overview-card"> <div class="overview-icon">{lightbulb_icon}</div> <h3 class="card-title">Outcome</h3> <p class="card-description"> Generate meaningful insights and practical business recommendations that support better fraud detection and informed decision making. </p> </div>',
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)