import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html


class FilterBarList:
    def __init__(
        self,
    ) -> None:
        pass

    def render(self) -> dbc.ListGroup:
        return dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                dbc.Label("RangeSlider", html_for="range-slider"),
                                dcc.RangeSlider(
                                    id="range-slider", min=0, max=3, value=[0, 3]
                                ),
                            ]
                        )
                    ]
                )
            ]
        )
