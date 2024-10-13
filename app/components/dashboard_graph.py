from typing import Union
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.colors import n_colors

from assets.colors import Colors
from data.objects.michelin_data.michelin import MichelinColumns


def dashboard_card(header: str, graph_id: str, graph_vh: int) -> dbc.Card:

    return dbc.Card(
        [
            dbc.CardHeader(header, class_name="bg-primary text-white"),
            dbc.CardBody(
                [
                    dcc.Graph(id=graph_id, style={"height": f"{graph_vh}vh"}),
                ]
            ),
        ],
        class_name="shadow",
    )


###############################################################################################
###############################################################################################
################################## Donut Charts ###############################################
###############################################################################################
###############################################################################################


def donut_chart_with_kpi(df: pd.DataFrame, col_name: str, label: str) -> px.sunburst:

    cat_count = df[col_name].value_counts()
    cat_count_veggie = cat_count.get(1, 0)
    cat_ratio = cat_count_veggie / cat_count.sum()
    cat_ratio_str = f"{cat_ratio * 100:.1f}%"

    df_cat = pd.DataFrame(
        data={
            "ratio": 2 * [cat_ratio_str],
            "category": [label, ""],
            "value": [cat_ratio, 1 - cat_ratio],
        }
    )

    fig = px.sunburst(
        df_cat,
        path=["ratio", "category"],
        values="value",
        color="category",
        color_discrete_map={
            label: Colors.michelin_red,
            "": Colors.light_grey,
            "(?)": Colors.white,
        },
    )

    fig.update_layout(margin={"t": 0, "l": 0, "b": 0, "r": 0}, hovermode=False)

    return fig


def veggie_ratio_chart(df: pd.DataFrame) -> px.sunburst:

    return donut_chart_with_kpi(
        df=df,
        col_name=MichelinColumns.extras.has_vegetarian_menus,
        label="Veggie-Friendly",
    )


def wheelchair_ratio_chart(df: pd.DataFrame) -> px.sunburst:

    return donut_chart_with_kpi(
        df=df,
        col_name=MichelinColumns.extras.has_wheelchair_access,
        label="Wheelchair Access",
    )


def view_ratio_chart(df: pd.DataFrame) -> px.sunburst:

    return donut_chart_with_kpi(
        df=df,
        col_name=MichelinColumns.extras.has_great_view,
        label="Great View",
    )


def wine_ratio_chart(df: pd.DataFrame) -> px.sunburst:

    return donut_chart_with_kpi(
        df=df,
        col_name=MichelinColumns.extras.has_interesting_wine_list,
        label="Interesting Wine",
    )


###############################################################################################
###############################################################################################
################################## Location Charts ############################################
###############################################################################################
###############################################################################################


def create_location_sunburst(df: pd.DataFrame) -> px.sunburst:

    cols = MichelinColumns()

    sunburst_cols = [
        cols.code.location_country,
        cols.code.location_city,
        cols.norm.award,
        cols.norm.name,
    ]

    df_locations_grouped = df.groupby(by=sunburst_cols).size().reset_index(name="count")

    n_countries = len(df[sunburst_cols[0]].unique())
    if n_countries > 1:
        # n-colors only works if requested scale has more than one colour
        color_scale = n_colors(
            Colors.michelin_red_rgb,
            Colors.light_red_rgb,
            n_countries,
            colortype="rgb",
        )
    else:
        color_scale = [Colors.michelin_red_rgb, Colors.light_red_rgb]

    fig = px.sunburst(
        df_locations_grouped,
        path=sunburst_cols,
        values="count",
        maxdepth=2,
        color=sunburst_cols[0],
        color_discrete_sequence=color_scale,
    )

    fig.update_traces(
        hovertemplate="<b>%{id}</b><br>Restaurants: <b>%{value}</b>",
    )

    fig.update_layout({"margin": {"t": 0, "l": 0, "b": 0, "r": 0}})

    return fig


def create_location_bar(df: pd.DataFrame) -> px.bar:
    cols = MichelinColumns()

    df_grouped = df.groupby(by=cols.norm.location).size().reset_index(name="count")
    df_top_n = df_grouped.sort_values(by="count", ascending=False).head(20)
    fig = px.bar(df_top_n, x="count", y=cols.norm.location)
    fig.update_layout(
        {
            "xaxis_title": None,
            "yaxis_title": None,
            "yaxis_categoryorder": "total ascending",
            "plot_bgcolor": Colors.transparent,
            "paper_bgcolor": Colors.transparent,
            "margin": {"t": 0, "l": 0, "b": 0, "r": 0},
        }
    )
    fig.update_traces(
        marker_color=Colors.michelin_red,
        hovertemplate="<b>%{y}</b><br>Resturants: <b>%{x}</b>",
    )
    fig.update_xaxes(
        showgrid=True, gridwidth=1, gridcolor=Colors.light_grey, griddash="dash"
    )
    return fig


def location_chart(df: pd.DataFrame) -> Union[px.bar, px.sunburst]:

    cols = MichelinColumns()
    unique_locations = df[cols.norm.location].unique()

    if len(unique_locations) <= 120:

        fig = create_location_sunburst(df=df)

    else:
        fig = create_location_bar(df=df)

    return fig


###############################################################################################
###############################################################################################
######################################### Heatmaps ############################################
###############################################################################################
###############################################################################################


def create_heatmap(df: pd.DataFrame) -> px.imshow:

    df = df.fillna(0)

    # note: can't use px.imshow due to sizing issues
    fig = go.Figure(
        data=go.Heatmap(
            x=df.columns,
            y=df.index,
            z=df.values,
            text=df.values,
            texttemplate="%{text}",
            colorscale=[(0, Colors.light_red), (1, Colors.michelin_red)],
            hovertemplate="<b>%{y} x %{x}</b><br>Restaurants: <b>%{z}</b><extra></extra>",
        )
    )

    fig.update_layout(
        {
            "xaxis_title": None,
            "yaxis_title": None,
            "plot_bgcolor": Colors.transparent,
            "paper_bgcolor": Colors.transparent,
            "margin": {"t": 0, "l": 0, "b": 0, "r": 0},
        }
    )

    fig.update_traces(showscale=False)

    return fig


def cuisine_chart(df: pd.DataFrame) -> px.imshow:
    cols = MichelinColumns()

    top_n = 10

    # get countries with the most restaurants
    top_n_countries = df[cols.code.location_country].value_counts().keys()[:top_n]

    if len(top_n_countries) > 2:
        top_n_locations = top_n_countries
        location_col = cols.code.location_country
    else:
        top_n_locations = df[cols.norm.location].value_counts().keys()[:top_n]
        location_col = cols.norm.location

    df_locations = df[df[location_col].isin(top_n_locations)][
        [location_col, cols.norm.cuisine]
    ]

    # explode cuisines
    df_exploded = df_locations.explode(cols.norm.cuisine)

    # get cuisines with the most restaurants (of the countries with the most restaurants)
    top_n_cuisines = df_exploded[cols.norm.cuisine].value_counts().keys()[:top_n]
    df_locations_cuisines = df_exploded[
        df_exploded[cols.norm.cuisine].isin(top_n_cuisines)
    ].copy()
    df_locations_cuisines.loc[:, "count"] = 1

    # pivot data to prepare for fig
    df_pivot = df_locations_cuisines.pivot_table(
        index=location_col,
        columns=cols.norm.cuisine,
        values="count",
        aggfunc="count",
    )

    # sort rows and columns in descending order for fig
    df_pivot = df_pivot[top_n_cuisines]
    df_pivot = df_pivot.reindex(
        top_n_locations[::-1]
    )  # reverse for correct order in graph

    return create_heatmap(df=df_pivot)


def stars_price_chart(df: pd.DataFrame) -> px.imshow:
    cols = MichelinColumns()

    cols_price_stars = [cols.code.price_amount, cols.norm.award]
    df_price_stars = df[cols_price_stars].copy()

    df_price_stars["count"] = 1

    df_price_stars_pivot = df_price_stars.pivot_table(
        index=cols.code.price_amount,
        columns=cols.norm.award,
        values="count",
        aggfunc="count",
    )

    # define hierarchy of stars to show them in correct order
    stars_hierarchy = [
        "Selected Restaurants",
        "Bib Gourmand",
        "1 Star",
        "2 Stars",
        "3 Stars",
    ]

    # add missing columns and sort
    missing_cols = list(set(stars_hierarchy) - set(df_price_stars_pivot.columns))
    for c in missing_cols:
        df_price_stars_pivot[c] = np.nan
    df_price_stars_pivot = df_price_stars_pivot[stars_hierarchy]

    # add missing rows and sort
    df_price_stars_pivot = df_price_stars_pivot.reindex(list(range(1, 5)))

    # convert index to categorical by defining it as star_count * €
    df_price_stars_pivot = df_price_stars_pivot.set_index(
        pd.Index(["€" * i for i in df_price_stars_pivot.index])
    )

    return create_heatmap(df=df_price_stars_pivot)
