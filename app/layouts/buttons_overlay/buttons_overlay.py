from dash import html

from components.button_popover import ButtonPopover
from components.button import ButtonComponent


buttons_overlay = html.Div(
    children=[
        ButtonComponent("Filter", icon="bi bi-funnel").render(),
        ButtonComponent("Dashboard", icon="bi bi-bar-chart-line-fill").render(),
        ButtonComponent("List", icon="bi bi-card-list").render(),
        ButtonPopover("Open filters", target="btn-filter").render(),
        ButtonPopover(
            "Open dashboard of all restaurants in view", target="btn-dashboard"
        ).render(),
        ButtonPopover(
            "Open list of all restaurants in view", target="btn-list"
        ).render(),
    ],
    className="buttons-overlay",
    style={"display": "flex", "flexDirection": "column"},
)
