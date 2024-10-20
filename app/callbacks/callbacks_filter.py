from typing import List
from dash import callback, Input, State, Output
from dash.exceptions import PreventUpdate

from app.assets.data import data
from utilities.filter_data import FilterData


@callback(
    Output("store-restaurant-ids", "data"),
    Input("btn-id", "n_clicks"),
    State("location-filter", "values"),
    State("price-filter", "values"),
    State("awards-filter", "values"),
    State("green-star-filter", "values"),
    State("cuisine-filter", "values"),
    State("facility-filter", "values"),
)
def apply_filters(
    n_clicks: bool,
    location_values: List[str],
    price_values: List[str],
    award_values: List[str],
    has_green_star_value: bool,
    cuisine_values: List[str],
    facility_values: List[str],
) -> List[int]:

    if n_clicks is None:
        raise PreventUpdate

    return FilterData(
        data=data,
        location_values=location_values,
        price_values=price_values,
        award_values=award_values,
        has_green_star_value=has_green_star_value,
        cuisine_values=cuisine_values,
        facility_values=facility_values,
    )._get_filtered_ids()
