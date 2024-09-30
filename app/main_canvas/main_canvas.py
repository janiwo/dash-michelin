import plotly.express as px

import sys

sys.path.append(sys.path[0] + "/..")
from data.objects.michelin_data.michelin import MichelinData


def main_canvas():
    michelin_data = MichelinData()
    df = michelin_data.df
    cols = michelin_data.columns
    df = df[df[cols.code.award_has_stars]]
    fig = px.scatter_map(
        df,
        lat=cols.norm.latitude,
        lon=cols.norm.longitude,
        color=cols.code.award_stars_count,
        size=cols.code.award_stars_count,
        color_continuous_scale=px.colors.sequential.Viridis,
        size_max=15,
        zoom=10,
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_layout(coloraxis_showscale=False)
    return fig
