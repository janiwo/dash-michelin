from dash import html

from components.button import button


buttons_overlay = html.Div(
    children=[button("Filter"), button("Dashboard"), button("List")],
    className="buttons-overlay",
)
