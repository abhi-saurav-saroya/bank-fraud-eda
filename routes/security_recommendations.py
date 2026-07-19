import streamlit as st

from components.security_recommendations.header import render as render_header
from components.security_recommendations.time_based_detection import render as render_time_based_detection
from components.security_recommendations.failed_attempt_monitorring import render as render_failed_attempt_monitoring
from components.security_recommendations.merchant_category_risk_scoring import render as render_merchant_category_risk_scoring
from components.security_recommendations.pin_change_verification_policy import render as render_pin_change_verification_policy

def render() -> None:
    """
    Render the Security Recommendations page.
    """

    render_header()

    st.divider()

    render_time_based_detection()
    render_failed_attempt_monitoring()
    render_merchant_category_risk_scoring()
    render_pin_change_verification_policy()