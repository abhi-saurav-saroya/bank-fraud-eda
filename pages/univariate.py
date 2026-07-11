import streamlit as st

# Components
from components.univariate_header import render as render_header
# from components.feature_selector import render as render_feature_selector
# from components.summary_cards import render as render_summary_cards
# from components.distribution_section import render as render_distribution_section
# from components.statistics_table import render as render_statistics_table
# from components.insight_panel import render as render_insight_panel


def render(df):
    """
    Render the Univariate Analysis page.
    """
    
    render_header()

    st.markdown("<br>", unsafe_allow_html=True)

    # --------------------------------------------------
    # Feature Selector
    # --------------------------------------------------

    # feature_type, feature = render_feature_selector(df)

    # --------------------------------------------------
    # Summary Cards
    # --------------------------------------------------

    # render_summary_cards(df, feature)

    # --------------------------------------------------
    # Distribution Section
    # --------------------------------------------------

    # render_distribution_section(df, feature)

    # --------------------------------------------------
    # Statistics Table
    # --------------------------------------------------

    # render_statistics_table(df, feature)

    # --------------------------------------------------
    # Insight Panel
    # --------------------------------------------------

    # render_insight_panel(df, feature)