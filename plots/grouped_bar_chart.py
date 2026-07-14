import plotly.express as px

from plots.theme import COLORS, apply_theme


def create(df, x, y, value=None, agg="count"):
    """
    Create a grouped bar chart.

    Parameters
    ----------
    x : str
        X-axis feature.

    y : str
        Grouping (colour) feature.

    value : str | None
        Numerical column to aggregate.
        If None, displays counts.

    agg : str
        Aggregation function.
        Supported: "count", "mean", "median", "sum"
    """

    if value is None or agg == "count":

        plot_df = (
            df.groupby([x, y])
            .size()
            .reset_index(name="Value")
        )

        y_axis_title = "Count"

    else:

        if agg == "mean":
            plot_df = (
                df.groupby([x, y])[value]
                .mean()
                .reset_index(name="Value")
            )

        elif agg == "median":
            plot_df = (
                df.groupby([x, y])[value]
                .median()
                .reset_index(name="Value")
            )

        elif agg == "sum":
            plot_df = (
                df.groupby([x, y])[value]
                .sum()
                .reset_index(name="Value")
            )

        else:
            raise ValueError(
                "agg must be one of: count, mean, median, sum"
            )

        y_axis_title = f"{agg.title()} {value.replace('_', ' ').title()}"

    plot_df[x] = plot_df[x].astype(str)
    plot_df[y] = plot_df[y].astype(str)

    fig = px.bar(
        plot_df,
        x=x,
        y="Value",
        color=y,
        barmode="group",
        color_discrete_sequence=COLORS,
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b>"
            "<br>Value: %{y}"
            "<extra></extra>"
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="#000000"),
        ),
    )

    if value is None or agg == "count":
        title = (
            f"{x.replace('_', ' ').title()} vs "
            f"{y.replace('_', ' ').title()}"
        )
    else:
        title = (
            f"{agg.title()} {value.replace('_', ' ').title()} "
            f"by {x.replace('_', ' ').title()} "
            f"and {y.replace('_', ' ').title()}"
        )

    fig.update_layout(
        title=title,
        yaxis_title=y_axis_title,
        xaxis_title=x.replace("_", " ").title(),
        legend_title=y.replace("_", " ").title(),
    )

    return apply_theme(fig)