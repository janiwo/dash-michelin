from dash import Input, Output, State, callback, ALL, ctx
from dash.exceptions import PreventUpdate


@callback(
    Output("filter-bar-list", "class_name"),
    Output("filter-bar-visibility", "data"),
    Input("btn-filter", "n_clicks"),
    Input("side-bar-close-filter-bar-list", "n_clicks"),
    State("filter-bar-visibility", "data"),
    Input("side-bar-visibility", "data"),
)
def toggle_filter_bar_list(filter_button, close_button, visible, side_bar_visible):
    if filter_button is None and close_button is None:
        raise PreventUpdate

    if ctx.triggered_id == "btn-filter":
        visible = not visible
    elif ctx.triggered_id == "side-bar-close-filter-bar-list":
        visible = False

    slide_suffix = "in2" if side_bar_visible else "in"
    if ctx.triggered_id in ["btn-filter", "side-bar-visibility"]:
        class_name = f"side-bar slide slide-{slide_suffix if visible else 'out'}"
    else:
        class_name = "side-bar slide slide-out"

    return class_name, visible
