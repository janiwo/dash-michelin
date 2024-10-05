from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate


@callback(
    Output("side-bar", "class_name"),
    Output("side-bar-visibility", "data"),
    Input("btn-list", "n_clicks"),
    State("side-bar-visibility", "data"),
)
def toggle_restaurant_list(n_clicks, visible):
    if n_clicks is None:
        raise PreventUpdate
    class_name = "side-bar slide slide-in" if visible else "side-bar slide slide-out"
    visible = not visible
    return class_name, visible
