import streamlit as st

st.set_page_config(
    page_title="Bank Fraud Analytics Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


from utils.css_loader import load_css
from utils.data_loader import load_clean, load_raw

from components.sidebar import render_sidebar

from routes.home import render as render_home
from routes.dataset import render as render_dataset
from routes.univariate import render as render_univariate
from routes.bivariate import render as render_bivariate
from routes.multivariate import render as render_multivariate
from routes.final_insights import render as render_final_insights
from routes.security_recommendations import render as render_security_recommendations
# from routes.future_scope import render as render_future_scope



load_css()
raw_df, clean_df = load_raw(), load_clean()


selected_page = render_sidebar()


if selected_page == "Home":
    render_home(clean_df)

elif selected_page == "Dataset":
    render_dataset(raw_df, clean_df)

elif selected_page == "Univariate Analysis":
    render_univariate(clean_df)

elif selected_page == "Bivariate Analysis":
    render_bivariate(clean_df)

elif selected_page == "Multivariate Analysis":
    render_multivariate(clean_df)

elif selected_page == "Final Insights":
    render_final_insights(clean_df)

elif selected_page == "Security Recommendations":
    render_security_recommendations()

# elif selected_page == "Future Scope":
#     render_future_scope()