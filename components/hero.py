from pathlib import Path

import streamlit as st


IMAGE_PATH = Path("static/images/bank.jpg")


def render(df) -> None:
    """
    Render the dashboard hero section.
    """

    left, right = st.columns([2.2, 1])

    with left:

        st.markdown(
            '<div class="hero"><div class="hero-badge">🔒 Fraud Detection Dashboard</div><div class="hero-title">Bank Fraud Analytics Dashboard</div><div class="hero-subtitle">Explore fraud patterns, transaction behaviour,customer characteristics and business insights through interactive visualisations built with Streamlit and Plotly.</div></div>',
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)

        with c1:
            st.button(
                "📊 Explore Dataset",
                use_container_width=True,
                type="primary",
            )

        with c2:
            st.button(
                "💡 View Insights",
                use_container_width=True,
            )

    with right:

        if IMAGE_PATH.exists():
            st.image(
                str(IMAGE_PATH),
                use_container_width=True,
            )

        fraud_rate = (
            df["is_fraud"].mean() * 100
        )

        st.markdown(
            f'<div class="hero-card"><div class="hero-stat">{fraud_rate:.2f}</div><div class="hero-label">Fraud Rate</div></div>',
            unsafe_allow_html=True,
        )