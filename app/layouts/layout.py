from dash import html
from components.profile_modal import profile_modal
from main_canvas.main_canvas import map_graph
from components.navbar import navbar
from components.buttons_overlay import buttons_overlay

layout = html.Div(
    [
        navbar,
        buttons_overlay,
        map_graph,
        profile_modal,
    ]
)
