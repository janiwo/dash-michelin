from typing import Dict, List
from dash import Input, Output, State, callback
import plotly.express as px

from components.map import create_map
from utilities.map_helpers import ViewPortHandler


@callback(
    Output("graph-map", "figure", allow_duplicate=True),
    Input("store-restaurant-ids", "data"),
    State("graph-map", "relayoutData"),
    prevent_initial_call=True,
)
def update_map_markers(restaurant_ids: List[int], viewport: Dict) -> px.scatter_map:

    viewport_handler = ViewPortHandler(viewport=viewport)

    new_map = create_map(
        restaurant_ids=restaurant_ids,
        zoom=viewport_handler.zoom,
        center=viewport_handler.center,
    )

    return new_map
