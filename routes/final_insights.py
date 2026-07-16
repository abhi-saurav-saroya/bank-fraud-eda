import streamlit as st 

from components.final_insights.header import render as render_header
from components.final_insights.correlation_with_fraud import render as render_correlation_with_fraud
from components.final_insights.failed_attempts_insight import render as render_failed_attempts_insight
from components.final_insights.hourly_fraud_insight import render as render_hourly_fraud_insight
from components.final_insights.international_transactions_insight import render as render_international_transactions_insight
from components.final_insights.merchant_category_insight import render as render_merchant_category_insight

def render(df) -> None:
    """
    Render the Final Insights page.
    """

    render_header()

    st.divider()

    tabs = st.tabs(
        [
            "📊 Correlation",
            "🔐 Failed Attempts",
            "🕒 Hourly Fraud",
            "🌍 International",
            "🏪 Merchant Category"
        ]
    )

    renderers = [
        render_correlation_with_fraud,
        render_failed_attempts_insight,
        render_hourly_fraud_insight,
        render_international_transactions_insight,
        render_merchant_category_insight
    ]

    for tab, renderer in zip(tabs, renderers):
        with tab:
            renderer(df)