import streamlit as st

from components.bivariate.header import render as render_header
from components.bivariate.variable_selector import render as render_variable_selector
from components.bivariate.relationship_visualization import render as render_relationship_visualization

def render(df):
    """
    Render the Bivariate Analysis page.
    """
    
    render_header()

    st.markdown("<br>", unsafe_allow_html=True)

    x_feature, y_feature, x_type, y_type = render_variable_selector(df)

    st.markdown("<br>", unsafe_allow_html=True)

    render_relationship_visualization(df, x_feature, y_feature, x_type, y_type)