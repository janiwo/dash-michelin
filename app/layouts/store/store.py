from dash import html, dcc
from assets.data import all_restaurant_ids


store = html.Div(
    [
        dcc.Store(id="side-bar-visibility", data=True),
        dcc.Store(id="store-restaurant-ids", data=all_restaurant_ids),
    ]
)
