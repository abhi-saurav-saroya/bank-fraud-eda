import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="Bank Fraud Analytics Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------- Utilities ----------
from utils.css_loader import load_css
from utils.data_loader import load_clean, load_raw

# ---------- Components ----------
from components.sidebar import render_sidebar

# ---------- Pages ----------
from pages.home import render as render_home
from pages.dataset import render as render_dataset
from pages.univariate import render as render_univariate
# from pages.bivariate import render as render_bivariate
# from pages.multivariate import render as render_multivariate
# from pages.recommendations import render as render_recommendations
# from pages.future_scope import render as render_future_scope



# LOAD CSS
load_css()

# LOAD DATA
raw_df, clean_df = load_raw(), load_clean()


# SIDEBAR
selected_page = render_sidebar()


# ROUTING
if selected_page == "Home":
    render_home(clean_df)

elif selected_page == "Dataset":
    render_dataset(raw_df, clean_df)

elif selected_page == "Univariate Analysis":
    render_univariate(clean_df)

# elif selected_page == "Bivariate Analysis":

#     render_bivariate(clean_df)

# elif selected_page == "Multivariate Analysis":

#     render_multivariate(clean_df)

# elif selected_page == "Recommendations":

#     render_recommendations(clean_df)

# elif selected_page == "Future Scope":

#     render_future_scope()