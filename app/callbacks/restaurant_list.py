from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate
from assets.data import data
from utilities.map_helpers import ViewPortHandler
from components.side_bar_list import SideBarList


@callback(
    Output("restaurant-list", "class_name"),
    Output("side-bar-visibility", "data"),
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Input("btn-list", "n_clicks"),
    Input("side-bar-close-restaurant-list", "n_clicks"),
    State("side-bar-visibility", "data"),
    State("graph-map", "relayoutData"),
    prevent_initial_call="initial_duplicate",
)
def toggle_restaurant_list(list_button, close_button, visible, viewport):
    if list_button is None and close_button is None:
        raise PreventUpdate

    df = data.df

    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry, ids_only=True
    )
    side_bar_list = SideBarList(data, restaurant_ids)
    class_name = "side-bar slide slide-in" if visible else "side-bar slide slide-out"
    visible = not visible
    return class_name, visible, side_bar_list.render()


@callback(
    Output("side-bar-body-restaurant-list", "children", allow_duplicate=True),
    Input("side-bar-refresh-restaurant-list", "n_clicks"),
    State("graph-map", "relayoutData"),
    prevent_initial_call="initial_duplicate",
)
def refresh_restaurant_list(n_clicks, viewport):
    df = data.df

    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry, ids_only=True
    )
    side_bar_list = SideBarList(data, restaurant_ids)
    return side_bar_list.render()


@callback(
    Output("graph-map", "figure"),
    Input("btn-filter", "n_clicks"),
    State("graph-map", "figure"),
    State("graph-map", "relayoutData"),
)
def refresh_map(n_clicks, figure, viewport):
    if n_clicks is None:
        raise PreventUpdate
    figure["layout"]["map"]["center"] = dict(lat=52.52, lon=13.405)
    return figure
