import geopandas as gpd
import dash_bootstrap_components as dbc
from dash import html, get_asset_url
from data.objects.michelin_data.michelin import MichelinData


# TODO find a better location for this
class RestaurantProfileModal:

    def __init__(self, data: MichelinData, restaurant_id: int) -> None:

        self.restaurant_id = restaurant_id
        self.filtered_df = self._filter_df(df=data.df, restaurant_id=restaurant_id)
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
                                            src=get_asset_url("MichelinStar.svg"),
                                            # src="assets/MichelinStar.svg",
                                            height="50px",
                                        )
                                    ]
                                    + self.filtered_df[self.columns.norm.has_green_star]
                                    * [
                                        html.Img(
                                            src=get_asset_url("MichelinGreenStar.svg"),
                                            # src="assets/MichelinGreenStar.svg",
                                            height="50px",
                                        )
                                    ]
                                ),
                                html.H1(self.filtered_df[self.columns.norm.name]),
                                html.Div(
                                    [
                                        # html.I(className="bi bi-geo-alt-fill"),
                                        self.filtered_df[self.columns.norm.location],
                                    ]
                                ),
                                html.Div([self.filtered_df[self.columns.norm.address]]),
                                html.Div(
                                    [
                                        self.filtered_df[self.columns.norm.price]
                                        + " · "
                                        + ", ".join(
                                            self.filtered_df[self.columns.norm.cuisine]
                                        )
                                    ]
                                ),
                                html.Div(
                                    [
                                        dbc.Badge(i, pill=True, className="me-1")
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
    def _filter_df(df: gpd.GeoDataFrame, restaurant_id: int) -> gpd.GeoDataFrame:

        return df.iloc[restaurant_id, :]


if __name__ == "__main__":

    df = MichelinData().df

    RestaurantProfileModal(df=df, restaurant_id=5).create_modal_contents()
