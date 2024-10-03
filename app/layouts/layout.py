from dash import html, dcc

from layouts.navbar.navbar import navbar
from layouts.buttons_overlay.buttons_overlay import buttons_overlay
from layouts.map_graph.map_graph import map_graph
from layouts.profile_modal.profile_modal import profile_modal
from layouts.side_bar.side_bar import side_bar

layout = html.Div(
    [
        dcc.Store(id="side-bar-visibility", data=True),
        navbar,
        buttons_overlay,
        side_bar,
        map_graph,
        profile_modal,
    ]
)
