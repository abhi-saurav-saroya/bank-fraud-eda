import streamlit as st


def render(raw_df, clean_df):
    """
    Render an interactive dataset preview.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Dataset Preview </h2> <div class="section-subtitle" color="white"> Explore the raw and cleaned datasets with interactive controls. </div> </div>',
        unsafe_allow_html=True,
    )

    # Controls
    c1, c2, c3 = st.columns([1.2, 1, 1.8])

    with c1:
        dataset_choice = st.radio(
            "Dataset",
            ["Cleaned", "Raw"],
            horizontal=True,
        )

    with c2:
        rows = st.selectbox(
            "Rows to Display",
            [10, 25, 50, 100],
            index=1,
        )

    if dataset_choice == "Cleaned":
        df = clean_df
    else:
        df = raw_df


    with c3:
        column = st.selectbox(
            "Search Column",
            df.columns,
        )

    search = st.text_input(
        "Search Value",
        placeholder="Type to filter rows...",
    )

    preview = df.copy()

    if search:
        preview = preview[
            preview[column]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    st.dataframe(
        preview.head(rows),
        width='stretch',
        hide_index=True,
    )

    csv = preview.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Displayed Data",
        data=csv,
        file_name=f"{dataset_choice.lower()}_dataset.csv",
        mime="text/csv",
        width='stretch',
    )