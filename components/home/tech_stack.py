import streamlit as st


def render():

    st.markdown(
        """
        <h2 class="section-title">
            Technology Stack
        </h2>

        <p>
            Technologies used to build this interactive analytics dashboard:
            <p align="centre">
                <img src="https://go-skill-icons.vercel.app/api/icons?i=numpy,pandas,matplotlib,seaborn,plotly,streamlit" />
            </p>
        </p>
        """,
        unsafe_allow_html=True,
    )