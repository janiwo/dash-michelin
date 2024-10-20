from dash import Input, Output, State, callback, ALL, ctx, no_update
from dash.exceptions import PreventUpdate
from assets.data import data
from utilities.map_helpers import ViewPortHandler
from components.restaurant_bar_list import RestaurantBarList

restaurant_bar_list_length = 7


@callback(
    Output("restaurant-list", "class_name"),
    Output("side-bar-visibility", "data"),
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Output("page-number", "data", allow_duplicate=True),
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
    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry,
        ids_only=True,
        page_index=0,
        page_length=restaurant_bar_list_length,
    )
    side_bar_list = RestaurantBarList(data, restaurant_ids_in_view)
    class_name = (
        "side-bar slide slide-in" if not visible else "side-bar slide slide-out"
    )
    visible = not visible
    if not visible and (
        ctx.triggered_id == "btn-list"
        or ctx.triggered_id == "side-bar-close-restaurant-list"
    ):
        return class_name, visible, no_update, no_update
    return class_name, visible, side_bar_list.render(), 0


@callback(
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Output("page-number", "data", allow_duplicate=True),
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

    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry,
        ids_only=True,
        page_index=0,
        page_length=restaurant_bar_list_length,
    )

    side_bar_list = RestaurantBarList(data, restaurant_ids)
    return side_bar_list.render(), 0


@callback(
    Output("graph-map", "figure"),
    Input({"type": "restaurant", "index": ALL}, "n_clicks"),
    State("graph-map", "figure"),
)
def fly_to_restaurant(n_clicks, figure):
    trigger_id = ctx.triggered_id
    if all(click is None for click in n_clicks) or trigger_id is None:
        raise PreventUpdate
    coords = data.df.iloc[int(trigger_id["index"])].geometry.coords[0]
    figure["layout"]["map"]["center"] = dict(lat=float(coords[1]), lon=float(coords[0]))
    figure["layout"]["map"]["zoom"] = 13.5
    return figure


@callback(
    Output("page-number", "data"),
    Input("restaurant-list-next", "n_clicks"),
    Input("restaurant-list-previous", "n_clicks"),
    State("page-number", "data"),
)
def update_page_number(next_button, prev_button, page_number):
    if next_button is None and prev_button is None:
        raise PreventUpdate
    trigger_id = ctx.triggered_id
    if trigger_id == "restaurant-list-next":
        page_number += 1
    else:
        page_number -= 1
    return page_number


@callback(
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Output("restaurant-list-next", "disabled"),
    Output("restaurant-list-previous", "disabled"),
    Input("page-number", "data"),
    State("graph-map", "relayoutData"),
    prevent_initial_call=True,
)
def update_restaurant_list(page_number, viewport):
    df = data.df
    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry,
        ids_only=True,
        page_index=page_number,
        page_length=restaurant_bar_list_length,
    )
    side_bar_list = RestaurantBarList(data, restaurant_ids)
    next_button_disable = len(restaurant_ids) < restaurant_bar_list_length
    prev_button_disable = not page_number > 0
    return side_bar_list.render(), next_button_disable, prev_button_disable
