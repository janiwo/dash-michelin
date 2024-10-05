import dash_bootstrap_components as dbc
from components.dashboard_graph import dashboard_card


graph_veggie = dashboard_card(header="Veggie Ratio", graph_id="fig-veggie", graph_vh=20)
graph_wheelchair = dashboard_card(
    header="Wheelchair Access Ratio", graph_id="fig-wheelchair", graph_vh=20
)
graph_view = dashboard_card(header="Great View Ratio", graph_id="fig-view", graph_vh=20)
graph_wine = dashboard_card(
    header="Interesting Wine Ratio", graph_id="fig-wine", graph_vh=20
)
graph_locations = dashboard_card(
    header="Locations", graph_id="fig-location", graph_vh=50
)
graph_cuisines = dashboard_card(header="Cuisines", graph_id="fig-cuisine", graph_vh=50)
graph_stars_price = dashboard_card(
    header="Price-Awards", graph_id="fig-stars-price", graph_vh=50
)


dashboard = dbc.Modal(
    [
        dbc.ModalHeader("Dashboard", class_name="bg-primary text-white"),
        dbc.ModalBody(
            [
                dbc.Row(
                    [
                        dbc.Col(graph_veggie, width=3),
                        dbc.Col(graph_wheelchair, width=3),
                        dbc.Col(graph_view, width=3),
                        dbc.Col(graph_wine, width=3),
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            graph_locations,
                            width=4,
                        ),
                        dbc.Col(
                            graph_cuisines,
                            width=4,
                        ),
                        dbc.Col(
                            graph_stars_price,
                            width=4,
                        ),
                    ],
                    class_name="mt-4",
                ),
            ],
            class_name="bg-light",
        ),
    ],
    is_open=False,
    className="mw-100 p-5",
    id="modal-dashboard",
)
