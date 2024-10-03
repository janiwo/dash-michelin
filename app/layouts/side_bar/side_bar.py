import dash_bootstrap_components as dbc
from dash import html

side_bar = dbc.Card(
    dbc.CardBody(
        dbc.ListGroup(
            [dbc.ListGroupItem(item) for item in ["Dashboard", "List", "Filter"]],
            flush=True,
        )
    ),
    id="side-bar",
    class_name="side-bar slide",
)
