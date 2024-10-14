import dash_bootstrap_components as dbc
from dash import html
from components.filter_bar_list import FilterBarList
from assets.data import data
from components.side_bar import SideBar

test_list = data.df.iloc[0:5, :].to_dict("records")

filter_bar = SideBar(
    children=FilterBarList().render(),
    id="filter-bar-list",
    action_button="Filter",
).render()
