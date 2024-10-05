import dash_bootstrap_components as dbc
from dash import html
from data.objects.michelin_data.michelin import MichelinData
import geopandas as gpd


class SideBarList:
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
                                html.H5(item["name"], className="mb-1"),
                                html.Small("Yay!", className="text-success"),
                            ],
                            className="d-flex w-100 justify-content-between",
                        ),
                        html.P(item["description"], className="mb-1"),
                        # html.Small("Plus some small print.", className="text-muted"),
                    ],
                    id=str(index),
                )
                for index, item in enumerate(self.df.to_dict("records"))
            ],
            flush=True,
        )

    @staticmethod
    def _filter_df(df: gpd.GeoDataFrame, restaurant_ids: list[int]) -> gpd.GeoDataFrame:

        return df.iloc[restaurant_ids, :]

    @staticmethod
    def clean_string(string: str) -> str:
        return string.lower().replace(" ", "-")
