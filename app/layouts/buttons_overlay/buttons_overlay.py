from dash import html

from components.button import button


buttons_overlay = html.Div(
    children=[button("Filter"), button("Dashbard"), button("List")],
    style={
        "position": "absolute",
        "top": "9vh",
        "left": "10px",
        "zIndex": "1000",
    },
)
