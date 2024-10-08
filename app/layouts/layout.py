from dash import html, dcc

from layouts.navbar.navbar import navbar
from layouts.buttons_overlay.buttons_overlay import buttons_overlay
from layouts.map_graph.map_graph import map_graph
from layouts.profile_modal.profile_modal import profile_modal
from layouts.restaurant_list.restaurant_list import restaurant_list
from layouts.dashboard.dashboard import dashboard

layout = html.Div(
    [
        dcc.Store(id="side-bar-visibility", data=True),
        navbar,
        buttons_overlay,
        restaurant_list,
        map_graph,
        profile_modal,
        dashboard,
    ]
)
