from dash import html

import dash_html_components as html
from components.button import ButtonComponent


buttons_overlay = html.Div(
    children=[
        ButtonComponent("Filter", icon="bi bi-funnel").render(),
        ButtonComponent("Dashboard", icon="bi bi-bar-chart-line-fill").render(),
        ButtonComponent("List", icon="bi bi-card-list").render(),
    ],
    className="buttons-overlay",
    style={"display": "flex", "flexDirection": "column"},
)
