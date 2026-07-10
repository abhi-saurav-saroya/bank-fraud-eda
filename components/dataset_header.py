import streamlit as st

from utils.icons import get_svg

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
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {paper_icon} </div> <div class="metric-value"> {raw_rows:,} </div> <div class="metric-label"> Total Records </div> </div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {puzzle_icon} </div> <div class="metric-value"> {raw_columns} </div> <div class="metric-label"> Total Features </div> </div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {memory_icon} </div> <div class="metric-value"> {raw_memory:.2f} MB </div> <div class="metric-label"> Memory Usage </div> </div>',
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {null_icon} </div> <div class="metric-value"> {raw_null_count} </div> <div class="metric-label"> Null Values </div> </div>',
            unsafe_allow_html=True,
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
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {paper_icon} </div> <div class="metric-value"> {rows:,} </div> <div class="metric-label"> Total Records </div> </div>',
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {puzzle_icon} </div> <div class="metric-value"> {columns} </div> <div class="metric-label"> Total Features </div> </div>',
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {memory_icon} </div> <div class="metric-value"> {memory:.2f} MB </div> <div class="metric-label"> Memory Usage </div> </div>',
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f'<div class="metric-card"> <div class="metric-icon"> {null_icon} </div> <div class="metric-value"> {null_count} </div> <div class="metric-label"> Null Values </div> </div>',
            unsafe_allow_html=True,
        )