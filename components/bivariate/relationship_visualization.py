import streamlit as st

from plots.boxplot import create as create_boxplot
from plots.grouped_bar_chart import create as create_grouped_bar_chart
from plots.heatmap import create as create_heatmap
from plots.scatter_plot import create as create_scatter_plot


def render(df, x_feature, y_feature, x_type, y_type):
    """
    Render relationship visualization between two features.
    """

    st.markdown(
        f'<div class="section"> <h2 class="section-title"> Relationship Visualization </h2> <div class="section-subtitle"> Explore the relationship between the selected variables using automatically selected visualizations. </div> </div>',
        unsafe_allow_html=True,
    )

    
    if x_type == "Numerical" and y_type == "Numerical":
        fig = create_scatter_plot(
            df=df,
            x=x_feature,
            y=y_feature,
        )

        st.plotly_chart(
            fig,
            width='stretch',
        )

    
    elif (x_type == "Numerical" and y_type in ["Categorical", "Binary", "Discrete Numerical"]):
        fig = create_boxplot(
            df=df,
            x=y_feature,
            y=x_feature,
        )

        st.plotly_chart(
            fig,
            width='stretch',
        )

    
    elif (x_type in ["Categorical", "Binary", "Discrete Numerical"] and y_type == "Numerical"):
        fig = create_boxplot(
            df=df,
            x=x_feature,
            y=y_feature,
            column=1
        )

        st.plotly_chart(
            fig,
            width='stretch',
        )


    else:
        left, right = st.columns(2)

        grouped = create_grouped_bar_chart(
            df=df,
            x=x_feature,
            y=y_feature,
        )

        heatmap = create_heatmap(
            df=df,
            x=x_feature,
            y=y_feature,
        )

        with left:
            st.plotly_chart(
                grouped,
                width='stretch',
            )

        with right:
            st.plotly_chart(
                heatmap,
                width='stretch',
            )