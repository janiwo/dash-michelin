# from app.assets.data import data
import plotly.express as px
from dash import dcc
from assets.data import data

df = data.df
cols = data.columns

map_fig = px.scatter_map(
    df,
    lat=cols.norm.latitude,
    lon=cols.norm.longitude,
    color=cols.code.award_stars_count,
    size=cols.code.award_stars_count,
    color_continuous_scale=px.colors.sequential.Viridis,
    size_max=15,
    zoom=10,
)
map_fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
map_fig.update_layout(coloraxis_showscale=False)


map_graph = dcc.Graph(
    id="graph-map",
    figure=map_fig,
    style={"height": "93vh", "position": "relative"},
)