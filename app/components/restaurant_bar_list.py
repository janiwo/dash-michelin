import dash_bootstrap_components as dbc
from dash import html
from data.objects.michelin_data.michelin import MichelinData
import geopandas as gpd
from assets.img_links import img_link_michelin_star, img_link_michelin_green_star


class RestaurantBarList:
    def __init__(
        self,
        data: MichelinData,
        restaurant_ids: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ) -> None:
        self.df = self._filter_df(df=data.df, restaurant_ids=restaurant_ids)
        self.restaurant_ids = restaurant_ids
        self.columns = data.columns

    def render(self) -> dbc.ListGroup:
        return dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        html.Div(
                            [
                                html.H5(
                                    item["name"],
                                    className="mb-1",
                                    style={
                                        "display": "inline-block",
                                        "paddingRight": 20,
                                    },
                                ),
                                html.Div(
                                    item["award_stars_count"]
                                    * [
                                        html.Img(
                                            src=img_link_michelin_star,
                                            height="15px",
                                        )
                                    ]
                                    + item["green_star"]
                                    * [
                                        html.Img(
                                            src=img_link_michelin_green_star,
                                            height="15px",
                                        )
                                    ],
                                    style={"display": "inline-block", "float": "right"},
                                ),
                            ],
                            className="clearfix",
                        ),
                    ]
                    + [
                        html.Small(
                            " - ".join(item["cuisine"]), className="mb-1 text-muted"
                        ),
                        html.Br(),
                        html.Small(item["price"], className="mb-1 text-muted"),
                    ],
                    id={
                        "type": "restaurant",
                        "index": f"{item['restaurant_id']}",
                    },
                    action=True,
                )
                for index, item in enumerate(self.df.to_dict("records"))
            ]
            + [
                html.Div(
                    [
                        dbc.Button(
                            "Previous",
                            id="restaurant-list-previous",
                            color="light",
                            disabled=True,
                            style={"float": "left"},
                        ),
                        dbc.Button(
                            "Next",
                            id="restaurant-list-next",
                            color="light",
                            style={"float": "right"},
                        ),
                    ],
                )
            ],
            flush=True,
        )

    @staticmethod
    def _filter_df(df: gpd.GeoDataFrame, restaurant_ids: list[int]) -> gpd.GeoDataFrame:

        return df[df["restaurant_id"].isin(restaurant_ids)]

    @staticmethod
    def clean_string(string: str) -> str:
        return string.lower().replace(" ", "-")
