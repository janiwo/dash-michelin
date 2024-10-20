from typing import List
from dash import Input, Output, callback
import plotly.express as px

from app.components.map import create_map

callback(
    Output("graph-map", "figure"),
    Input("store-restaurant-ids", "data"),
)


def update_map_markers(restaurant_ids: List[int]) -> px.scatter_map:

    # zoom default = 1
    # center_default = dict(lat=20, lon=0)

    return create_map(restaurant_ids=restaurant_ids, zoom=None, center=None)
