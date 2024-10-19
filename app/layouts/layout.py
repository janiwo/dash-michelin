from dash import html, dcc

from layouts.navbar.navbar import navbar
from layouts.buttons_overlay.buttons_overlay import buttons_overlay
from layouts.map_graph.map_graph import map_graph
from layouts.profile_modal.profile_modal import profile_modal
from layouts.restaurant_bar.restaurant_bar import restaurant_bar
from layouts.filter_bar.filter_bar import filter_bar
from layouts.dashboard.dashboard import dashboard
from layouts.variable_store.variable_store import variable_store

layout = html.Div(
    [
        *variable_store,
        navbar,
        buttons_overlay,
        filter_bar,
        restaurant_bar,
        map_graph,
        profile_modal,
        dashboard,
    ]
)
