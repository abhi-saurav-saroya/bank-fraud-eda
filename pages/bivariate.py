import streamlit as st

from components.bivariate.header import render as render_header
from components.bivariate.variable_selector import render as render_variable_selector
from components.bivariate.relationship_visualization import render as render_relationship_visualization
from components.bivariate.relationship_summary import render as render_relationship_summary
from components.bivariate.insight_panel import render as render_insight_panel

def render(df):
    """
    Render the Bivariate Analysis page.
    """
    
    render_header()

    st.divider()

    x_feature, y_feature, x_type, y_type = render_variable_selector(df)

    st.divider()

    render_relationship_visualization(df, x_feature, y_feature, x_type, y_type)

    st.divider()

    render_relationship_summary(df, x_feature, y_feature, x_type, y_type)

    st.divider()

    render_insight_panel(df, x_feature, y_feature, x_type, y_type)