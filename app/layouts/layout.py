from dash import html, dcc
from main_canvas.main_canvas import main_canvas
from components.navbar import navbar


layout = html.Div(
    [
        navbar,
        dcc.Graph(id="graph", figure=main_canvas(), style={"height": "93vh"}),
    ]
)
