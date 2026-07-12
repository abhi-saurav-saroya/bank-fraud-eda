import streamlit as st

from components.univariate.header import render as render_header
from components.univariate.feature_selector import render as render_feature_selector
from components.univariate.summary_cards import render as render_summary_cards
from components.univariate.distribution_section import render as render_distribution_section
from components.univariate.insight_panel import render as render_insight_panel


def render(df):
    """
    Render the Univariate Analysis page.
    """
    
    render_header()

    st.markdown("<br>", unsafe_allow_html=True)
    
    feature_type, feature = render_feature_selector(df)

    render_summary_cards(df, feature_type, feature)

    render_distribution_section(df, feature_type, feature)

    render_insight_panel(df, feature_type, feature)