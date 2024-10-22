import dash_bootstrap_components as dbc
from dash import html, dcc


class FilterBarList:
    def __init__(
        self, country_list: list, facilities_options: list, awards_options: list
    ) -> None:
        self.country_list = country_list
        self.facilities_options = facilities_options
        self.awards_options = awards_options

    def render(self) -> dbc.ListGroup:
        return dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        dbc.Row(
                            dbc.Col(
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
                            )
                        ),
                        dbc.Row(
                            dbc.Col(
                                [
                                    dbc.Label("Awards:", html_for="input-awards"),
                                    dcc.Dropdown(
                                        self.awards_options,
                                        id="input-awards",
                                        multi=True,
                                    ),
                                ]
                            )
                        ),
                        dbc.Row(
                            dbc.Col(
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
                            )
                        ),
                        dbc.Row(
                            dbc.Col(
                                [
                                    # dbc.Label(
                                    #     "Green Star:",
                                    #     html_for="input-green-star",
                                    # ),
                                    # dbc.Switch(
                                    #     id="input-green-star",
                                    #     value=False,
                                    # ),
                                    dcc.Checklist(
                                        options=[
                                            {
                                                "label": "Green Star only",
                                                "value": 1,
                                            }
                                        ],
                                        id="input-green-star",
                                    ),
                                ],
                            )
                        ),
                        dbc.Row(
                            dbc.Col(
                                [
                                    dbc.Label("Price:", html_for="input-price-amount"),
                                    dcc.RangeSlider(
                                        1, 4, 1, value=[1, 4], id="input-price-amount"
                                    ),
                                ]
                            )
                        ),
                    ]
                    + [
                        html.Div(
                            dbc.ButtonGroup(
                                [
                                    dbc.Button(
                                        "Filter",
                                        id="side-bar-filter-filter-bar-list",
                                        color="danger",
                                    )
                                ],
                                style={"justifyContent": "right"},
                            ),
                            style={"textAlign": "right"},
                        ),
                    ]
                )
            ],
            flush=True,
        )
