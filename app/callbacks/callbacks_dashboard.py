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
    # TODO link this to the dashboard btn once it has an id
    Input("btn-test", "n_clicks"),
    State("graph-map", "relayoutData"),
)
def open_dashboard(n_clicks, viewport):

    if n_clicks is None:
        raise PreventUpdate

    df = data.df

    restaurant_ids = ViewPortHandler(viewport=viewport).get_coordinates_in_view(
        gs=df.geometry, ids_only=True
    )

    df_filtered = df[df.index.isin(restaurant_ids)]

    fig_veggie = veggie_ratio_chart(df=df_filtered)
    fig_wheelchair = wheelchair_ratio_chart(df=df_filtered)
    fig_view = view_ratio_chart(df=df_filtered)
    fig_wine = wine_ratio_chart(df=df_filtered)

    fig_locations = location_chart(df=df_filtered)
    fig_cuisine = cuisine_chart(df=df_filtered)
    fig_stars_price = stars_price_chart(df=df_filtered)

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
