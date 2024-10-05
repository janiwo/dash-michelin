from dash import html

from components.button import Button


buttons_overlay = html.Div(
    children=[
        Button("Filter").render(),
        Button("Dashboard").render(),
        Button("List").render(),
    ],
    className="buttons-overlay",
)
