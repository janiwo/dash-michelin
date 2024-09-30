from dash_bootstrap_components import Button
from dash import html


def button(label: str) -> Button:
    return Button(
        label,
        color="light",
        className="me-1",
        style={"boxShadow": "2px 2px 5px rgba(0, 0, 0, 0.3)"},
    )


buttons_overlay = html.Div(
    children=[button("Filter")],
    style={
        "position": "absolute",
        "top": "9vh",
        "left": "10px",
        "zIndex": "1000",
    },
)
