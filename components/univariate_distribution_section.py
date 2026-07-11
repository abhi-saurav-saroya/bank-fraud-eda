import streamlit as st

from plots.bar_chart import create as create_bar_chart
from plots.boxplot import create as create_boxplot
from plots.histogram import create as create_histogram
from plots.pie_chart import create as create_pie_chart


def render(df, feature_type, feature):
    """
    Render distribution charts for the selected feature.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Distribution Analysis </h2> <div class="section-subtitle"> Visualize the distribution of the selected feature. </div> </div>',
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    
    if feature_type == "Numerical":
        histogram = create_histogram(df=df, column=feature)
        boxplot = create_boxplot(df=df, column=feature)

        with left:
            st.plotly_chart(
                histogram,
                width='stretch',
            )

        with right:
            st.plotly_chart(
                boxplot,
                width='stretch',
            )


    elif feature_type == "Categorical" or feature_type == "Binary":
        bar = create_bar_chart(df=df, column=feature)
        pie = create_pie_chart(df=df, column=feature)

        with left:
            st.plotly_chart(
                bar,
                width='stretch',
            )

        with right:
            st.plotly_chart(
                pie,
                width='stretch',
            )