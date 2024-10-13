from dash import Input, Output, callback
from dash.exceptions import PreventUpdate

from assets.data import data
from utilities.component_helpers.restaurant_profile_modal import RestaurantProfileModal


@callback(
    Output("modal-restaurant-profile", "is_open"),
    Output("modal-restaurant-profile-body", "children"),
    Input("graph-map", "clickData"),
)
def open_restaurant_profile(clickData):
    if clickData is None:
        raise PreventUpdate
    restaurant_id = clickData["points"][0]["customdata"][0]
    modal_body_children = RestaurantProfileModal(
        data=data, restaurant_id=restaurant_id
    ).create_modal_contents()
    return True, modal_body_children
