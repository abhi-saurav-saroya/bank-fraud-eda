import streamlit as st

from components.hero import render as render_hero
from components.metric_cards import render as render_metric_cards


def render(df):

    render_hero(df)

    st.markdown('<br>', unsafe_allow_html=True)

    render_metric_cards(df)