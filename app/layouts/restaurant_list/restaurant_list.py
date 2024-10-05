import dash_bootstrap_components as dbc
from dash import html
from components.side_bar_list import SideBarList
from assets.data import data
from components.side_bar import SideBar

test_list = data.df.iloc[0:5, :].to_dict("records")

restaurant_list = SideBar(
    children=SideBarList(
        data=data, restaurant_ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ).render(),
    id="restaurant-list",
).render()
