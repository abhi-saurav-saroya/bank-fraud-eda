import pandas as pd
import streamlit as st


@st.cache_data
def load_raw():
    return pd.read_csv("data/raw/bank_fraud.csv")


@st.cache_data
def load_clean():
    return pd.read_csv("data/processed/bank_fraud_cleaned.csv")