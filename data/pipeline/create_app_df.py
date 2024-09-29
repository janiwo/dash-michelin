from dataclasses import asdict

import pandas as pd
import geopandas as gpd
from data.objects.michelin_data.michelin import MichelinData, MichelinExtrasColumns
from data.objects.michelin_data.michelin_raw import MichelinDataRaw


class CreateAppDf:

    def __init__(self, raw_data: MichelinDataRaw) -> None:

        self.raw_data = raw_data

    def do(self) -> MichelinData:

        data = self._normalize_col_names(raw_data=self.raw_data)

        self._get_location_info(data=data)
        self._get_price_info(data=data)
        self._get_award_info(data=data)
        self._convert_cuisine_col(data=data)
        data.df = self._get_extras_cols(data=data)
        data.df = self._convert_to_geopandas(data=data)

        return data

    @staticmethod
    def _normalize_col_names(raw_data: MichelinDataRaw) -> MichelinData:

        col_mapping = {
            v: asdict(MichelinData.columns.norm).get(k)
            for k, v in asdict(MichelinDataRaw.columns).items()
        }

        return MichelinData(df=raw_data.df.rename(columns=col_mapping))

    @staticmethod
    def _get_location_info(data: MichelinData) -> None:
        df = data.df
        cols = data.columns

        df[[cols.code.location_city, cols.code.location_country]] = df[
            cols.norm.location
        ].str.split(", ", expand=True)

    @staticmethod
    def _get_price_info(data: MichelinData) -> None:
        df = data.df
        cols = data.columns

        df[cols.code.price_currency] = df[cols.norm.price].str[0]
        df[cols.code.price_amount] = df[cols.norm.price].str.len()

    @staticmethod
    def _get_award_info(data: MichelinData) -> None:
        df = data.df
        cols = data.columns

        df[cols.code.award_stars_count] = df[cols.norm.award].str.extract(r"(\d+)")
        df[cols.code.award_stars_count] = (
            pd.to_numeric(df[cols.code.award_stars_count]).fillna(0).astype(int)
        )

        df[cols.code.award_has_stars] = df[cols.code.award_stars_count] > 0

    @staticmethod
    def _convert_cuisine_col(data: MichelinData):
        df = data.df
        cols = data.columns

        df[cols.norm.cuisine] = df[cols.norm.cuisine].str.split(", ")
        # restaurants without any cuisine should have empty list rather then nan
        df[cols.norm.cuisine] = df[cols.norm.cuisine].fillna("").apply(list)

    @staticmethod
    def _get_extras_cols(data: MichelinData) -> pd.DataFrame:
        df = data.df
        cols = data.columns

        extras_dummies = df[cols.norm.facilities_and_services].str.get_dummies(sep=",")

        # ensure that all dummies are noted in MichelinExtrasColumns
        missing_vals = set(extras_dummies.columns) - (
            set(asdict(MichelinExtrasColumns()).values())
        )
        if len(missing_vals) > 0:
            print(
                f"{len(missing_vals)} values missing in extras col definition: {', '.join(missing_vals)}"
            )

        return pd.concat([df, extras_dummies], axis=1)

    @staticmethod
    def _convert_to_geopandas(data: MichelinData) -> gpd.GeoDataFrame:
        df = data.df
        cols = data.columns

        return gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(
                df[cols.norm.longitude], df[cols.norm.latitude]
            ),
            crs="EPSG:4326",
        )


if __name__ == "__main__":

    raw_data = MichelinDataRaw()
    data = CreateAppDf(raw_data=raw_data).do()
    data.save_data()
