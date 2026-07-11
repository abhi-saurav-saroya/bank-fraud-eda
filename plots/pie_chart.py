import plotly.express as px

from plots.theme import COLORS, apply_theme


def create(df, column):
    """
    Create a pie chart.
    """

    counts = (
        df[column]
        .value_counts()
        .reset_index()
    )

    counts.columns = [column, "Count"]

    fig = px.pie(
        counts,
        names=column,
        values="Count",
        hole=0.55,
        color_discrete_sequence=COLORS,
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>%{percent}<br>Count: %{value}<extra></extra>",
    )

    fig.update_layout(
        title=f"{column} Distribution",
    )

    return apply_theme(fig)