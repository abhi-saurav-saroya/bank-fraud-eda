import plotly.express as px

from plots.theme import PRIMARY, apply_theme


def create(df, column):
    """
    Create a box plot.
    """

    fig = px.box(
        df,
        y=column,
        color_discrete_sequence=[PRIMARY],
        points="outliers",
    )

    fig.update_traces(
        hovertemplate="<b>%{y}</b><extra></extra>",
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000")
        )
    )

    fig.update_layout(
        title=f"Box Plot of {column.replace('_', ' ').title()}",
    )

    return apply_theme(fig)