from dash import dcc
from assets.data import all_restaurant_ids

variable_store = [
    dcc.Store(id="side-bar-visibility", data=False),
    dcc.Store(id="filter-bar-visibility", data=False),
    dcc.Store(id="store-restaurant-ids", data=all_restaurant_ids),
]
