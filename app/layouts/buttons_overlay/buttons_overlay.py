from dash import html

from components.button import ButtonComponent


buttons_overlay = html.Div(
    children=[
        ButtonComponent("Filter").render(),
        ButtonComponent("Dashboard").render(),
        ButtonComponent("List").render(),
    ],
    className="buttons-overlay",
)
