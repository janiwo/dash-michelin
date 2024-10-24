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
        self._get_id_col(data=data)
        self._get_location_info(data=data)
        self._get_price_info(data=data)
        self._get_award_info(data=data)
        self._convert_cuisine_col(data=data)
        self._get_visualizations_cols(data=data)
        data.df = self._get_extras_cols(data=data)
        data.df = self._convert_to_geopandas(data=data)
        self._sort_df(data=data)

        return data

    @staticmethod
    def _normalize_col_names(raw_data: MichelinDataRaw) -> MichelinData:

        col_mapping = {
            v: asdict(MichelinData.columns.norm).get(k)
            for k, v in asdict(MichelinDataRaw.columns).items()
        }

        return MichelinData(df=raw_data.df.rename(columns=col_mapping))

    @staticmethod
    def _get_id_col(data: MichelinDataRaw) -> None:
        df = data.df
        cols = data.columns

        df[cols.code.restaurant_id] = df.index

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
        # heuristic in the absence of info
        df[cols.code.price_amount] = df[cols.code.price_amount].fillna(1)
        df[cols.code.price_amount] = df[cols.code.price_amount].astype(int)

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
    def _convert_cuisine_col(data: MichelinData) -> None:
        df = data.df
        cols = data.columns

        # remove ' Cuisine' from cuisine names, such as Modern Cuisine, Traditional Cuisine, etc.
        # this gives more space in the chart
        df[cols.norm.cuisine] = df[cols.norm.cuisine].str.replace(" Cuisine", "")

        df[cols.norm.cuisine] = df[cols.norm.cuisine].str.split(", ")
        # restaurants without any cuisine should have empty list rather then nan
        df[cols.norm.cuisine] = df[cols.norm.cuisine].fillna("").apply(list)

    @staticmethod
    def _get_visualizations_cols(data: MichelinData) -> None:
        # add helper columns that are useful for visualisations
        df = data.df
        cols = data.columns

        df[cols.viz.award_stars_count_str] = df[cols.code.award_stars_count].astype(str)
        marker_size_dict = {
            0: 1,
            1: 3,
            2: 6,
            3: 10,
        }
        df[cols.viz.marker_size_map] = df[cols.code.award_stars_count].apply(
            lambda x: marker_size_dict[x]
        )

        df[cols.viz.award_stars_count_sign] = df[cols.code.award_stars_count].apply(
            lambda x: f"({x*'☆'})" if x else ""
        )

        df[cols.viz.award_stars_count_total] = (
            df[cols.code.award_stars_count] + df[cols.norm.has_green_star]
        )

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

        df = pd.concat([df, extras_dummies], axis=1)
        df[cols.norm.facilities_and_services] = df[
            cols.norm.facilities_and_services
        ].str.split(",")
        # restaurants without any facilities and services should have empty list rather then nan
        df[cols.norm.facilities_and_services] = (
            df[cols.norm.facilities_and_services].fillna("").apply(list)
        )

        return df

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

    @staticmethod
    def _sort_df(data: MichelinData) -> None:
        df = data.df
        cols = data.columns

        df.sort_values(
            by=[cols.viz.award_stars_count_total, cols.code.award_stars_count],
            ascending=[False, False],
            inplace=True,
        )


if __name__ == "__main__":

    raw_data = MichelinDataRaw()
    data = CreateAppDf(raw_data=raw_data).do()
    data.save_data()
