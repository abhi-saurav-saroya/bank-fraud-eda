import streamlit as st

from utils.icons import get_svg


STORE_ICON = get_svg("store")
MEDIUM_ICON = get_svg("circle-alert")
GRAPH_ICON = get_svg("chart-column")
TARGET_ICON = get_svg("target")
CHECK_ICON = get_svg("check")
PROBLEM_ICON = get_svg("bug")
BENEFITS_ICON = get_svg("sparkles")


def render():
    """
    Render Merchant Category Risk Scoring recommendation.
    """

    st.markdown(
        f'<div class="recommendation-card"> <div class="recommendation-header"> <div class="recommendation-icon"> {STORE_ICON} </div> <div> <h2 class="recommendation-title"> Merchant Category Risk Scoring </h2> <div class="recommendation-priority medium"> {MEDIUM_ICON} Medium Priority </div> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {GRAPH_ICON} Supported Finding </h3> <p class="recommendation-text"> The analysis revealed noticeable variation in fraud rates across merchant categories. Certain sectors consistently experienced higher fraud rates, indicating that merchant type is an important contextual feature for identifying suspicious transactions. </p> </div> <div class="column"> <h3 class="recommendation-section-title"> {PROBLEM_ICON} Problem </h3> <p class="recommendation-text"> Applying identical security policies across all merchant categories ignores the fact that some business sectors are naturally more vulnerable to fraudulent activity. This can reduce detection effectiveness while increasing unnecessary alerts for lower-risk merchants. </p> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {TARGET_ICON} Recommended Actions </h3> <ol class="recommendation-list"> <li> {CHECK_ICON} Assign dynamic fraud risk scores to merchant categories based on historical fraud patterns. </li> <li> {CHECK_ICON} Increase monitoring and verification for transactions originating from high-risk merchant categories. </li> <li> {CHECK_ICON} Periodically recalculate merchant risk scores using recent transaction data to adapt to changing fraud trends. </li> <li> {CHECK_ICON} Combine merchant category risk with customer behaviour and transaction characteristics to improve fraud prediction accuracy. </li> </ol> </div> <div class="column"> <h3 class="recommendation-section-title"> {BENEFITS_ICON} Expected Benefits </h3> <ul class="recommendation-list"> <li> {CHECK_ICON} More targeted fraud detection focused on historically high-risk business sectors. </li> <li> {CHECK_ICON} Reduced false positives for transactions from lower-risk merchant categories. </li> <li> {CHECK_ICON} Improved allocation of fraud investigation resources. </li> <li> {CHECK_ICON} Enhanced adaptability as merchant-specific fraud patterns evolve over time. </li> </ul> </div> </div> </div>',
        unsafe_allow_html=True,
    )