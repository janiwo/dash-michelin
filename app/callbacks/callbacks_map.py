from typing import List
from dash import Input, Output, State, callback
import plotly.express as px
from shapely import Point

from app.components.map import create_map

callback(
    Output("graph-map", "figure", allow_duplicate=True),
    Input("store-restaurant-ids", "data"),
    State("graph-map", "figure"),
    prevent_initial_call=True,
)


def update_map_markers(restaurant_ids: List[int], fig) -> px.scatter_map:

    # zoom default = 1
    # center_default = dict(lat=20, lon=0)

    return create_map(restaurant_ids=restaurant_ids, zoom=1, center=Point(0, 20))
