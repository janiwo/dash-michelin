from dash import dcc

variable_store = [
    dcc.Store(id="side-bar-visibility", data=False),
    dcc.Store(id="filter-bar-visibility", data=False),
]
