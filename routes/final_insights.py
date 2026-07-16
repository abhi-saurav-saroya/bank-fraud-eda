import streamlit as st 

from components.final_insights.header import render as render_header
from components.final_insights.correlation_with_fraud import render as render_correlation_with_fraud
from components.final_insights.failed_attempts_insight import render as render_failed_attempts_insight
from components.final_insights.hourly_fraud_insight import render as render_hourly_fraud_insight

def render(df) -> None:
    """
    Render the Final Insights page.
    """

    render_header()

    st.divider()

    t1, t2, t3 = st.tabs(["Correlation with Fraud", "Fraud Rate by Failed Attempts", "Fraud Rate by Hour of Day"])

    with t1:
        render_correlation_with_fraud(df)

    with t2:
        render_failed_attempts_insight(df)

    with t3:
        render_hourly_fraud_insight(df)