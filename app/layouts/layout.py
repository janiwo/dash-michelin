from dash import html

from layouts.navbar.navbar import navbar
from layouts.buttons_overlay.buttons_overlay import buttons_overlay
from layouts.map_graph.map_graph import map_graph
from layouts.profile_modal.profile_modal import profile_modal

layout = html.Div(
    [
        navbar,
        buttons_overlay,
        map_graph,
        profile_modal,
    ]
)
