import streamlit as st


PAGES = [
    "🏠 Home",
    "🗄️ Dataset",
    "📊 Univariate Analysis",
    "📈 Bivariate Analysis",
    "🔍 Multivariate Analysis",
    "💡 Final Insights",
    "🔐 Security Recommendations"
]


def render_sidebar() -> str:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-logo">
                🏦
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="sidebar-title">
                Bank Fraud
            </div>

            <div class="sidebar-subtitle">
                Analytics Dashboard
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        selected = st.radio(
            label="Navigation",
            options=PAGES,
            label_visibility="collapsed",
        )

        st.divider()

        st.markdown(
            '<div class="sidebar-footer">Interactive Dashboard using<br><b>Streamlit + Plotly</b><br><br>Version 1.0<br>Developed by <b>Abhi Saurav Saroya</b></div>',
            unsafe_allow_html=True,
        )

    # Remove emojis before returning
    return selected.split(" ", 1)[1]