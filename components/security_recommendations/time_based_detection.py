import streamlit as st

from utils.icons import get_svg


CLOCK_ICON = get_svg("clock")
HIGH_ICON = get_svg("triangle-alert")
GRAPH_ICON = get_svg("chart-column")
TARGET_ICON = get_svg("target")
CHECK_ICON = get_svg("check")
PROBLEM_ICON = get_svg("bug")
BENEFITS_ICON = get_svg("sparkles")


def render():
    """
    Render Time-Based Fraud Detection recommendation.
    """

    st.markdown(
        f'<div class="recommendation-card"> <div class="recommendation-header"> <div class="recommendation-icon"> {CLOCK_ICON} </div> <div> <h2 class="recommendation-title"> Time-Based Fraud Detection </h2> <div class="recommendation-priority high"> {HIGH_ICON} High Priority </div> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {GRAPH_ICON} Supported Finding </h3> <p class="recommendation-text"> The exploratory analysis revealed that fraudulent transactions are not distributed uniformly throughout the day. Certain hours consistently record higher fraud rates, indicating that attackers tend to operate during predictable time windows. </p> </div> <div class="column"> <h3 class="recommendation-section-title"> {PROBLEM_ICON} Problem </h3> <p class="recommendation-text"> Treating every transaction equally regardless of the time it occurs may allow suspicious nighttime or off-hour transactions to bypass additional security checks, increasing the likelihood of successful fraudulent activity. </p> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {TARGET_ICON} Recommended Actions </h3> <ol class="recommendation-list"> <li> {CHECK_ICON} Increase transaction risk scores during identified high-risk hours. </li> <li> {CHECK_ICON} Trigger additional authentication for large or unusual transactions performed during peak fraud periods. </li> <li> {CHECK_ICON} Enable real-time fraud monitoring during high-risk time windows. </li> <li> {CHECK_ICON} Continuously update high-risk time intervals using recent transaction data. </li> </ol> </div> <div class="column"> <h3 class="recommendation-section-title"> {BENEFITS_ICON} Expected Benefits </h3> <ul class="recommendation-list"> <li> {CHECK_ICON} Earlier detection of suspicious transactions. </li> <li> {CHECK_ICON} Reduced financial losses caused by fraudulent activity. </li> <li> {CHECK_ICON} Improved efficiency by focusing monitoring efforts during high-risk periods instead of continuously applying the same level of scrutiny. </li> <li> {CHECK_ICON} Enhanced customer security without increasing friction for all users. </li> </ul> </div> </div> </div>',
        unsafe_allow_html=True,
    )