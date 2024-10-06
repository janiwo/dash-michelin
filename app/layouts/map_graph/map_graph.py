# from app.assets.data import data
import plotly.express as px
from dash import dcc
from assets.colors import Colors
from assets.data import data

df = data.df
cols = data.columns

map_fig = px.scatter_map(
    df,
    lat=cols.norm.latitude,
    lon=cols.norm.longitude,
    size=cols.viz.marker_size_map,
    color=cols.viz.award_stars_count_str,
    color_discrete_map={
        "0": Colors.michelin_red,
        "1": Colors.bronze,
        "2": Colors.silver,
        "3": Colors.gold,
    },
    size_max=15,
    zoom=1,
    center=dict(lat=20, lon=0),
)
map_fig.update_traces(
    cluster=dict(enabled=True, color=Colors.light_grey, maxzoom=3),
)
map_fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0}, coloraxis_showscale=False, showlegend=False
)


map_graph = dcc.Graph(
    id="graph-map",
    figure=map_fig,
    style={"height": "93vh", "position": "relative"},
)
