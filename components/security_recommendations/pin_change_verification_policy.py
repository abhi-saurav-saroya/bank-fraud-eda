import streamlit as st

from utils.icons import get_svg


KEY_ICON = get_svg("key-round")
MEDIUM_ICON = get_svg("circle-alert")
GRAPH_ICON = get_svg("chart-column")
TARGET_ICON = get_svg("target")
CHECK_ICON = get_svg("check")
PROBLEM_ICON = get_svg("bug")
BENEFITS_ICON = get_svg("sparkles")


def render():
    """
    Render PIN Change Verification Policy recommendation.
    """

    st.markdown(
        f'<div class="recommendation-card"> <div class="recommendation-header"> <div class="recommendation-icon"> {KEY_ICON} </div> <div> <h2 class="recommendation-title"> PIN Change Verification Policy </h2> <div class="recommendation-priority medium"> {MEDIUM_ICON} Medium Priority </div> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {GRAPH_ICON} Supported Finding </h3> <p class="recommendation-text"> The exploratory analysis showed a noticeable difference in fraud rates between accounts that had recently changed their PIN and those that had not. Although a PIN update is generally a legitimate security action, it can also coincide with compromised accounts or unauthorized credential changes, making it a valuable contextual feature for fraud detection. </p> </div> <div class="column"> <h3 class="recommendation-section-title"> {PROBLEM_ICON} Problem </h3> <p class="recommendation-text"> Treating PIN change events as isolated account updates overlooks valuable behavioural context. Fraudulent actors may attempt to modify account credentials before initiating unauthorized transactions, while genuine users may also become more vulnerable immediately after changing security credentials. </p> </div> </div> <div class="two-column"> <div class="column"> <h3 class="recommendation-section-title"> {TARGET_ICON} Recommended Actions </h3> <ol class="recommendation-list"> <li> {CHECK_ICON} Include recent PIN change history as an input feature in transaction risk scoring models. </li> <li> {CHECK_ICON} Increase monitoring of high-value or unusual transactions immediately following a PIN update. </li> <li> {CHECK_ICON} Send instant notifications to customers whenever a transaction occurs shortly after a PIN change. </li> <li> {CHECK_ICON} Require additional authentication when recent PIN changes coincide with other high-risk indicators such as international transactions or repeated failed authentication attempts. </li> </ol> </div> <div class="column"> <h3 class="recommendation-section-title"> {BENEFITS_ICON} Expected Benefits </h3> <ul class="recommendation-list"> <li> {CHECK_ICON} Earlier detection of potentially compromised accounts following credential updates. </li> <li> {CHECK_ICON} Improved fraud detection accuracy by incorporating credential-related behavioural signals. </li> <li> {CHECK_ICON} Enhanced customer confidence through timely alerts after sensitive account changes. </li> <li> {CHECK_ICON} Reduced likelihood of unauthorized transactions immediately following security credential modifications. </li> </ul> </div> </div> </div>',
        unsafe_allow_html=True,
    )