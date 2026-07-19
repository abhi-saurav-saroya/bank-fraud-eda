import streamlit as st

from utils.icons import get_svg


LOCK_ICON = get_svg("lock")
HIGH_ICON = get_svg("triangle-alert")
GRAPH_ICON = get_svg("chart-column")
TARGET_ICON = get_svg("target")
CHECK_ICON = get_svg("check")
PROBLEM_ICON = get_svg("bug")
BENEFITS_ICON = get_svg("sparkles")


def render():
    """
    Render Failed Authentication Monitoring recommendation.
    """

    st.markdown(
        f'<div class="recommendation-card"> <div class="recommendation-header"> <div class="recommendation-icon"> {LOCK_ICON} </div> <div> <h2 class="recommendation-title"> Failed Authentication Monitoring </h2> <div class="recommendation-priority high"> {HIGH_ICON} High Priority </div> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {GRAPH_ICON} Supported Finding </h3> <p class="recommendation-text"> Exploratory analysis showed that transactions with multiple failed authentication attempts consistently exhibited substantially higher fraud rates than transactions with few or no failed attempts, making authentication failures a strong indicator of suspicious behaviour. </p> </div> <div class="column"> <h3 class="recommendation-section-title"> {PROBLEM_ICON} Problem </h3> <p class="recommendation-text"> Repeated failed authentication attempts often indicate credential stuffing, brute-force attacks, or unauthorized account access. Without additional monitoring, fraudulent users may eventually gain access and perform high-risk transactions. </p> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {TARGET_ICON} Recommended Actions </h3> <ol class="recommendation-list"> <li> {CHECK_ICON} Trigger Multi-Factor Authentication (MFA) after two or more failed authentication attempts. </li> <li> {CHECK_ICON} Temporarily lock accounts after exceeding predefined authentication failure thresholds. </li> <li> {CHECK_ICON} Generate real-time alerts for customers whenever repeated failed login attempts are detected. </li> <li> {CHECK_ICON} Incorporate failed authentication counts into fraud risk scoring models before transaction approval. </li> </ol> </div> <div class="column"> <h3 class="recommendation-section-title"> {BENEFITS_ICON} Expected Benefits </h3> <ul class="recommendation-list"> <li> {CHECK_ICON} Reduced risk of account takeover attacks. </li> <li> {CHECK_ICON} Improved protection against credential stuffing and brute-force login attempts. </li> <li> {CHECK_ICON} Faster identification of suspicious account activity through automated alerts. </li> <li> {CHECK_ICON} Increased overall reliability of fraud detection by incorporating behavioural authentication signals. </li> </ul> </div> </div> </div>',
        unsafe_allow_html=True,
    )