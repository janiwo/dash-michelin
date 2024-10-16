import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html


class FilterBarList:
    def __init__(
        self, country_list: list, facilities_options: list, cuisine_options: list
    ) -> None:
        self.country_list = country_list
        self.facilities_options = facilities_options
        self.cuisine_options = cuisine_options

    def render(self) -> dbc.ListGroup:
        return dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                dbc.Label(
                                    "Countries:", html_for="input-location-country"
                                ),
                                dcc.Dropdown(
                                    self.country_list,
                                    id="input-location-country",
                                    multi=True,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label("Awards:", html_for="input-awards"),
                                dcc.Dropdown(
                                    [
                                        "Selected Restaurants",
                                        "Bib Gourmand",
                                        "1 Star",
                                        "2 Stars",
                                        "3 Stars",
                                    ],
                                    id="input-awards",
                                    multi=True,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label("Cuisine:", html_for="input-cuisine"),
                                dcc.Dropdown(
                                    [
                                        "Selected Restaurants",
                                        "Bib Gourmand",
                                        "1 Star",
                                        "2 Stars",
                                        "3 Stars",
                                    ],
                                    id="input-cuisine",
                                    multi=True,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label(
                                    "Facilities and Services:",
                                    html_for="input-facilities-and-services",
                                ),
                                dcc.Dropdown(
                                    self.facilities_options,
                                    id="input-facilities-and-services",
                                    multi=True,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label("Green Star:", html_for="input-green-star"),
                                dbc.Switch(
                                    id="input-green-star",
                                    value=False,
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                dbc.Label("Price:", html_for="input-price-amount"),
                                dcc.RangeSlider(
                                    1, 4, 1, value=[1, 4], id="input-price-amount"
                                ),
                            ]
                        ),
                    ]
                )
            ],
            flush=True,
        )
