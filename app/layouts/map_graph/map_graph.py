# from app.assets.data import data
import plotly.express as px
from dash import dcc
from components.map import create_map
from assets.colors import Colors
from assets.data import data, all_restaurant_ids

df = data.df


map_graph = dcc.Graph(
    id="graph-map",
    figure=create_map(
        restaurant_ids=all_restaurant_ids, zoom=1, center=dict(lat=20.0, lon=0.0)
    ),
    style={"height": "93vh", "position": "relative"},
)
