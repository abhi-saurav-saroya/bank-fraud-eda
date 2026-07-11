import plotly.graph_objects as go


PRIMARY = "#2563EB"
PRIMARY_LIGHT = "#DBEAFE"

SUCCESS = "#10B981"
WARNING = "#F59E0B"
DANGER = "#EF4444"

BACKGROUND = "#FFFFFF"
PLOT_BACKGROUND = "#FFFFFF"

TEXT = "#1E293B"
TEXT_SECONDARY = "#64748B"

GRID = "#E2E8F0"
BORDER = "#CBD5E1"

COLORS = [
    "#2563EB",
    "#3B82F6",
    "#60A5FA",
    "#93C5FD",
    "#BFDBFE",
    "#10B981",
    "#F59E0B",
    "#EF4444",
]


def apply_theme(fig: go.Figure) -> go.Figure:
    """
    Apply a consistent Plotly theme across the dashboard.
    """

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor=BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,

        font=dict(
            family="Inter",
            size=14,
            color=TEXT,
        ),

        title=dict(
            x=0,
            xanchor="left",
            font=dict(
                size=22,
                color=TEXT,
            ),
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),

        hoverlabel=dict(
            bgcolor="white",
            font_size=13,
            font_family="Inter",
        ),

        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
        ),

        transition=dict(
            duration=400,
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        showline=True,
        linecolor=BORDER,
        tickfont=dict(
            size=12,
            color=TEXT_SECONDARY,
        ),
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor=GRID,
        gridwidth=1,
        zeroline=False,
        showline=False,
        tickfont=dict(
            size=12,
            color=TEXT_SECONDARY,
        ),
    )

    return fig