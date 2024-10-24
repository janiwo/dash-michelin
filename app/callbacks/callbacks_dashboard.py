from typing import Dict, List
from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate

from assets.data import data
from components.dashboard_graph import (
    cuisine_chart,
    location_chart,
    stars_price_chart,
    veggie_ratio_chart,
    view_ratio_chart,
    wheelchair_ratio_chart,
    wine_ratio_chart,
)
from utilities.map_helpers import ViewPortHandler


@callback(
    Output("modal-dashboard", "is_open"),
    Output("fig-veggie", "figure"),
    Output("fig-wheelchair", "figure"),
    Output("fig-view", "figure"),
    Output("fig-wine", "figure"),
    Output("fig-location", "figure"),
    Output("fig-cuisine", "figure"),
    Output("fig-stars-price", "figure"),
    Input("btn-dashboard", "n_clicks"),
    State("graph-map", "relayoutData"),
    State("store-restaurant-ids", "data"),
)
def open_dashboard(n_clicks: int, viewport: Dict, restaurant_ids: List[int]):

    if n_clicks is None:
        raise PreventUpdate

    df = data.df
    cols = data.columns

    df_filtered = df[df[cols.code.restaurant_id].isin(restaurant_ids)]

    restaurant_ids_in_view = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df_filtered.geometry, ids_only=True
    )

    df_dashboard = df_filtered[
        df_filtered[cols.code.restaurant_id].isin(restaurant_ids_in_view)
    ]

    fig_veggie = veggie_ratio_chart(df=df_dashboard)
    fig_wheelchair = wheelchair_ratio_chart(df=df_dashboard)
    fig_view = view_ratio_chart(df=df_dashboard)
    fig_wine = wine_ratio_chart(df=df_dashboard)

    fig_locations = location_chart(df=df_dashboard)
    fig_cuisine = cuisine_chart(df=df_dashboard)
    fig_stars_price = stars_price_chart(df=df_dashboard)

    return (
        True,
        fig_veggie,
        fig_wheelchair,
        fig_view,
        fig_wine,
        fig_locations,
        fig_cuisine,
        fig_stars_price,
    )
