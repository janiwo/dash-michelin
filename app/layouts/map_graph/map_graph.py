# from app.assets.data import data
import plotly.express as px
from dash import dcc
from assets.colors import Colors
from assets.data import data


map_graph = dcc.Graph(
    id="graph-map",
    figure=map_fig,
    style={"height": "93vh", "position": "relative"},
)
