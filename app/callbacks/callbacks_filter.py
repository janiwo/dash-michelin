from typing import List
from dash import callback, Input, State, Output
from dash.exceptions import PreventUpdate

from assets.data import data
from utilities.filter_data import FilterData


@callback(
    Output("store-restaurant-ids", "data"),
    Input("side-bar-filter-filter-bar-list", "n_clicks"),
    State("input-location-country", "value"),
    State("input-awards", "value"),
    State("input-facilities-and-services", "value"),
    State("input-green-star", "value"),
    State("input-price-amount", "value"),
)
def apply_filters(
    n_clicks: bool,
    location_country_values: List[str],
    award_values: List[str],
    facility_values: List[str],
    has_green_star_value: bool,
    price_values: List[int],
) -> List[int]:

    if n_clicks is None:
        raise PreventUpdate

    return FilterData(
        data=data,
        location_values=location_country_values,
        price_values=price_values,
        award_values=award_values,
        has_green_star_value=has_green_star_value,
        cuisine_values=None,
        facility_values=facility_values,
    )._get_filtered_ids()
