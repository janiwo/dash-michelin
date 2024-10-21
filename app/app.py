from callbacks import (
    restaurant_profile,
    restaurant_list,
    callbacks_dashboard,
    callbacks_filter,
    callbacks_map,
    callbacks_navbar,
    filter_bar,
)  # This imports the callbacks to register them with the app
import dash_bootstrap_components as dbc
from dash import Dash
from decouple import config
from layouts.layout import layout

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
app.title = "Dash Michelin"
server = app.server

app.layout = layout

if __name__ == "__main__":
    if config("DEBUG", False, cast=bool):
        app.run(debug=True, host="0.0.0.0", port=8080)
    else:
        from waitress import serve

        serve(server, host="0.0.0.0", port=8080)
