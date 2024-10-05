from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate


@callback(
    Output("restaurant-list", "class_name"),
    Output("side-bar-visibility", "data"),
    Input("btn-list", "n_clicks"),
    Input("side-bar-close-restaurant-list", "n_clicks"),
    State("side-bar-visibility", "data"),
)
def toggle_restaurant_list(list_button, close_button, visible):
    if list_button is None and close_button is None:
        raise PreventUpdate
    class_name = "side-bar slide slide-in" if visible else "side-bar slide slide-out"
    visible = not visible
    return class_name, visible
