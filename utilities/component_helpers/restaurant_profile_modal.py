import geopandas as gpd
import dash_bootstrap_components as dbc
from dash import html, get_asset_url
from data.objects.michelin_data.michelin import MichelinData
from assets.img_links import img_link_michelin_star, img_link_michelin_green_star


# TODO find a better location for this
class RestaurantProfileModal:

    def __init__(self, data: MichelinData, restaurant_id: int) -> None:

        self.restaurant_id = restaurant_id
        self.filtered_df = self._filter_df(data=data, restaurant_id=restaurant_id)
        self.columns = data.columns

    def create_modal_contents(self) -> html.Div:
        # https://guide.michelin.com/de/de/capital-region/copenhagen/restaurant/alchemist
        return html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    self.filtered_df[
                                        self.columns.code.award_stars_count
                                    ]
                                    * [
                                        html.Img(
                                            src=img_link_michelin_star,
                                            height="50px",
                                        )
                                    ]
                                    + self.filtered_df[self.columns.norm.has_green_star]
                                    * [
                                        html.Img(
                                            src=img_link_michelin_green_star,
                                            height="50px",
                                        )
                                    ]
                                ),
                                html.H1(self.filtered_df[self.columns.norm.name]),
                                html.Div(
                                    [
                                        html.B(
                                            self.filtered_df[self.columns.norm.location]
                                        ),
                                    ]
                                ),
                                html.Div(
                                    [
                                        self.filtered_df[self.columns.norm.address],
                                    ],
                                ),
                                html.Div(
                                    [
                                        self.filtered_df[self.columns.norm.price]
                                        + " · "
                                        + ", ".join(
                                            self.filtered_df[self.columns.norm.cuisine]
                                        )
                                    ],
                                    className="mb-2",
                                ),
                                html.Div(
                                    [
                                        dbc.Badge(
                                            i,
                                            pill=True,
                                            color="primary",
                                            text_color="white",
                                            class_name="me-1 mb-2 mt-1",
                                        )
                                        for i in self.filtered_df[
                                            self.columns.norm.facilities_and_services
                                        ]
                                    ]
                                ),
                                html.Div(
                                    [self.filtered_df[self.columns.norm.description]]
                                ),
                            ],
                        ),
                    ],
                    class_name="mb-2",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.A(
                                    dbc.Button(
                                        "Restaurant Website",
                                        className="btn-block",
                                    ),
                                    href=self.filtered_df[
                                        self.columns.norm.website_url
                                    ],
                                    target="_blank",
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                html.A(
                                    dbc.Button(
                                        "Michelin Website",
                                        className="btn-block",
                                    ),
                                    href=self.filtered_df[
                                        self.columns.norm.michelin_url
                                    ],
                                    target="_blank",
                                )
                            ],
                            width=4,
                        ),
                    ],
                    justify="center",
                ),
            ]
        )

    @staticmethod
    def _filter_df(data: MichelinData, restaurant_id: int) -> gpd.GeoDataFrame:
        df = data.df
        cols = data.columns

        return df.loc[restaurant_id, :]


if __name__ == "__main__":

    df = MichelinData().df

    RestaurantProfileModal(df=df, restaurant_id=5).create_modal_contents()
