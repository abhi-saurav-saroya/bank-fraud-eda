import streamlit as st

from components.hero import render as render_hero


def render(df):

    render_hero(df)

    st.write("Home page under development...")