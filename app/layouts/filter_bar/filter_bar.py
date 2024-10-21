import dash_bootstrap_components as dbc
from dash import html
from components.filter_bar_list import FilterBarList
from assets.data import data
from assets.filter_lists import countries_list, facilities_and_services, stars_hierarchy
from components.side_bar import SideBar
from dataclasses import asdict


filter_bar = SideBar(
    children=FilterBarList(
        countries_list,
        facilities_and_services,
        stars_hierarchy,
    ).render(),
    id="filter-bar-list",
    action_button="Reset",
).render()
