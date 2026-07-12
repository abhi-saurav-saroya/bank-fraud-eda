import streamlit as st


def render(df):
    """
    Render an interactive column explorer.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Column Explorer </h2> <div class="section-subtitle"> Inspect the properties and sample values of every feature in the dataset. </div> </div>',
        unsafe_allow_html=True,
    )

    column = st.selectbox(
        "Select a Column",
        df.columns,
    )

    series = df[column]
    dtype = str(series.dtype)
    missing = series.isna().sum()
    unique = series.nunique()
    duplicates = len(series) - unique
    memory = series.memory_usage(deep=True) / 1024


    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Data Type",
            dtype,
        )

        st.metric(
            "Missing Values",
            missing,
        )

    with c2:
        st.metric(
            "Unique Values",
            unique,
        )

        st.metric(
            "Duplicate Values",
            duplicates,
        )

    with c3:
        st.metric(
            "Memory Usage",
            f"{memory:.2f} KB",
        )

        st.metric(
            "Non-null Values",
            series.notna().sum(),
        )

    st.markdown("#### Basic Statistics")

    if series.dtype == "object":
        st.dataframe(
            series.value_counts()
            .head(10)
            .rename("Count")
            .to_frame(),
            width='content',
        )

    else:
        st.dataframe(
            series.describe().to_frame(name="Value"),
            width='content',
        )