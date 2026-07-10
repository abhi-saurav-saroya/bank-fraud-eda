import streamlit as st

from components.home_header import render as render_hero
from components.home_metric_cards import render as render_home_metric_cards
from components.overview import render as render_overview
from components.tech_stack import render as render_tech_stack


def render(df):

    render_hero(df)

    st.markdown("<br>", unsafe_allow_html=True)

    render_home_metric_cards(df)

    st.markdown("<br><br>", unsafe_allow_html=True)

    render_overview()

    st.markdown("<br>", unsafe_allow_html=True)

    render_tech_stack()