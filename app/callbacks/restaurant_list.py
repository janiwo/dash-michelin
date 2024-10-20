from dash import Input, Output, State, callback, ALL, ctx
from dash.exceptions import PreventUpdate
from assets.data import data
from utilities.map_helpers import ViewPortHandler
from components.restaurant_bar_list import RestaurantBarList


@callback(
    Output("restaurant-list", "class_name"),
    Output("side-bar-visibility", "data"),
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Input("btn-list", "n_clicks"),
    Input("side-bar-close-restaurant-list", "n_clicks"),
    State("side-bar-visibility", "data"),
    State("graph-map", "relayoutData"),
    State("store-restaurant-ids", "data"),
    prevent_initial_call="initial_duplicate",
)
def toggle_restaurant_list(
    list_button, close_button, visible, viewport, restaurant_ids
):
    if list_button is None and close_button is None:
        raise PreventUpdate

    df = data.df
    cols = data.columns

    df_filtered = df[df[cols.code.restaurant_id].isin(restaurant_ids)]

    restaurant_ids_in_view = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df_filtered.geometry, ids_only=True
    )
    side_bar_list = RestaurantBarList(data, restaurant_ids_in_view)
    class_name = (
        "side-bar slide slide-in" if not visible else "side-bar slide slide-out"
    )
    visible = not visible
    return class_name, visible, side_bar_list.render()


@callback(
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Input("side-bar-refresh-restaurant-list", "n_clicks"),
    State("graph-map", "relayoutData"),
    State("store-restaurant-ids", "data"),
    prevent_initial_call="initial_duplicate",
)
def refresh_restaurant_list(n_clicks, viewport, restaurant_ids):
    if n_clicks is None and viewport is None:
        raise PreventUpdate
    df = data.df
    cols = data.columns

    df_filtered = df[df[cols.code.restaurant_id].isin(restaurant_ids)]

    restaurant_ids_in_view = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df_filtered.geometry, ids_only=True
    )
    side_bar_list = RestaurantBarList(data, restaurant_ids_in_view)
    return side_bar_list.render()


@callback(
    Output("graph-map", "figure"),
    Input({"type": "restaurant", "index": ALL}, "n_clicks"),
    State("graph-map", "figure"),
)
def fly_to_restaurant(n_clicks, figure):
    trigger_id = ctx.triggered_id
    if all(click is None for click in n_clicks) or trigger_id is None:
        raise PreventUpdate
    coords = trigger_id["index"].split("-")
    figure["layout"]["map"]["center"] = dict(lat=float(coords[0]), lon=float(coords[1]))
    figure["layout"]["map"]["zoom"] = 13.5
    return figure
