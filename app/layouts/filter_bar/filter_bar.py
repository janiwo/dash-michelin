import dash_bootstrap_components as dbc
from dash import html
from components.filter_bar_list import FilterBarList
from assets.data import data
from components.side_bar import SideBar
from dataclasses import asdict

test_list = data.df.iloc[0:5, :].to_dict("records")
cols = data.columns
unique_countries = sorted(filter(None, data.df[cols.code.location_country].unique()))
filtered_out_rows = data.df[~data.df[cols.code.location_country].isin(unique_countries)]

filter_bar = SideBar(
    children=FilterBarList(
        # [
        #     cols.code.location_country,
        #     cols.norm.award,
        #     cols.norm.cuisine,
        #     cols.norm.facilities_and_services,
        #     cols.norm.has_green_star,
        #     cols.code.price_amount,
        # ],
        unique_countries,
        [v for v in asdict(cols.extras).values()],
        [],
    ).render(),
    id="filter-bar-list",
    action_button="Filter",
).render()
