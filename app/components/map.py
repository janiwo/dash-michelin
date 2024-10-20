from typing import Dict, List

import plotly.express as px

from assets.colors import Colors
from assets.data import data

df = data.df
cols = data.columns


def create_map(
    restaurant_ids: List[int],
    zoom: int = 1,
    center: Dict[str, float] = dict(lat=20, lon=0),
) -> px.scatter_map:

    df_filtered = df[df[cols.code.restaurant_id].isin(restaurant_ids)]

    map_fig = px.scatter_map(
        df_filtered,
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
        custom_data=[
            cols.code.restaurant_id,
            cols.norm.name,
            cols.norm.location,
            cols.viz.award_stars_count_sign,
            cols.norm.price,
        ],
        zoom=zoom,
        center=center,
    )

    map_fig.update_traces(
        # setting the cluster seems to have a negative effect on updating the map
        # see: https://github.com/plotly/plotly.py/issues/3631#issuecomment-1408694360
        # cluster=dict(enabled=True, color=Colors.light_grey, maxzoom=3),
        hovertemplate="<b>%{customdata[1]} %{customdata[3]}</b><br>"
        + "<i>%{customdata[2]}</i><br>"
        + "%{customdata[4]}<br>"
        + "<extra></extra>",
    )
    map_fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_showscale=False,
        showlegend=False,
    )

    return map_fig
