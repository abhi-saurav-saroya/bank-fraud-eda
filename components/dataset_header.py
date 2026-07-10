import streamlit as st

from utils.icons import get_svg

from components.metric_card import render as render_metric_card

paper_icon = get_svg("notepad-text")
puzzle_icon = get_svg("puzzle")
memory_icon = get_svg("card-sim")
null_icon = get_svg("ban")



def render(raw_df, df):
    """
    Render dataset overview section.
    """

    raw_rows = len(raw_df)
    raw_columns = raw_df.shape[1]
    raw_memory = raw_df.memory_usage(deep=True).sum() / (1024 ** 2)
    raw_null_count = raw_df.isnull().sum().sum()
    rows = len(df)
    columns = df.shape[1]
    memory = df.memory_usage(deep=True).sum() / (1024 ** 2)
    null_count = df.isnull().sum().sum()

    st.markdown(
        '<div class="hero"> <div class="hero-title"> Dataset Explorer </div> <div class="hero-subtitle"> Explore the cleaned banking transaction dataset used for exploratory data analysis. This section provides a quick overview of the dataset\'s size, structure and quality. <br> <br> </div> </div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<br>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2>Before Data Preprocessing</h2>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card(
            icon=paper_icon,
            value=raw_rows,
            label="Total Records"
        )

    with c2:
        render_metric_card(
            icon=puzzle_icon,
            value=raw_columns,
            label="Total Features"
        )

    with c3:
        render_metric_card(
            icon=memory_icon,
            value=f"{raw_memory:.2f} MB",
            label="Memory Usage"
        )

    with c4:
        render_metric_card(
            icon=null_icon,
            value=raw_null_count,
            label="Null Values"
        )


    st.markdown(
        '<br>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2>After Data Preprocessing</h2>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_metric_card(
            icon=paper_icon,
            value=rows,
            label="Total Records"
        )

    with c2:
        render_metric_card(
            icon=puzzle_icon,
            value=columns,
            label="Total Features"
        )

    with c3:
        render_metric_card(
            icon=memory_icon,
            value=f"{memory:.2f} MB",
            label="Memory Usage"
        )

    with c4:
        render_metric_card(
            icon=null_icon,
            value=null_count,
            label="Null Values"
        )