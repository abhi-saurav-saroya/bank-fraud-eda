import plotly.express as px

from plots.theme import COLORS, PRIMARY, apply_theme


def create(df, column, bins=30):
    """
    Create a histogram for a numerical feature.
    """

    fig = px.histogram(
        df,
        x=column,
        nbins=bins,
        color_discrete_sequence=[PRIMARY],
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>",
        marker_line_width=0.5,
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000")
        )
    )

    fig.update_layout(
        title=f"Distribution of {column.replace('_', ' ').title()}",
        bargap=0.05,
    )

    return apply_theme(fig)