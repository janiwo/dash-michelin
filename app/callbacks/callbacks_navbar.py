from dash import Input, Output, State, callback
from dash.exceptions import PreventUpdate


@callback(
    Output("modal-navbar", "is_open"),
    Input("navbar-navlink", "n_clicks"),
    State("modal-navbar", "is_open"),
)
def toggle_modal_navbar(n_clicks, is_open):

    if n_clicks is None:
        raise PreventUpdate
    return not is_open
