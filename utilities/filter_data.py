from typing import List

import pandas as pd

from data.objects.michelin_data.michelin import MichelinData


class FilterData:

    def __init__(
        self,
        data: MichelinData,
        location_values: List[str],
        price_values: List[str],
        award_values: List[str],
        has_green_star_value: bool,
        cuisine_values: List[str],
        facility_values: List[str],
    ) -> None:

        self.data = data
        self.location_values = location_values
        self.price_values = price_values
        self.award_values = award_values
        self.has_green_star_value = has_green_star_value
        self.cuisine_values = cuisine_values
        self.facility_values = facility_values

        self.filtered_df = self.__filter_df()

    def __filter_df(self) -> pd.DataFrame:

        df = self.data.df
        cols = self.data.columns

        df_filtered = df.copy()

        if self.has_green_star_value:

            df_filtered = df_filtered[df_filtered[cols.norm.has_green_star] == 1]

        if self.location_values:

            df_filtered = df_filtered[
                df_filtered[cols.code.location_country].isin(self.location_values)
            ]

        if self.price_values:

            df_filtered = df_filtered[
                (df_filtered[cols.code.price_amount] >= self.price_values[0])
                & (df_filtered[cols.code.price_amount] <= self.price_values[1])
            ]

        if self.award_values:

            df_filtered = df_filtered[
                df_filtered[cols.norm.award].isin(self.award_values)
            ]

        if self.facility_values:

            for value in self.facility_values:

                df_filtered = df_filtered[df_filtered[value] == 1]

        if self.cuisine_values:

            df_filtered = df_filtered[
                df_filtered[cols.norm.cuisine].apply(
                    lambda x: any(i in self.cuisine_values for i in x)
                )
            ]

        return df_filtered

    def _get_filtered_ids(self) -> List[int]:

        return self.filtered_df[self.data.columns.code.restaurant_id].to_list()
