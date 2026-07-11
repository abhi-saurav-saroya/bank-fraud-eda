import plotly.express as px

from plots.theme import COLORS, apply_theme


def create(df, column, top_n=None):
    """
    Create a frequency bar chart.
    """

    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = [column, "Count"]

    if top_n:
        counts = counts.head(top_n)

    fig = px.bar(
        counts,
        x=column,
        y="Count",
        color=column,
        color_discrete_sequence=COLORS,
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Count: %{y}<extra></extra>",
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000")
        )
    )

    fig.update_layout(
        title=f"{column.replace('_', ' ').title()} Frequency",
        showlegend=False,
    )

    return apply_theme(fig)