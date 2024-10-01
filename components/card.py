from dash import html
import dash_bootstrap_components as dbc


class CustomCard:

    def __init__(self, title: str, body: html.Div) -> None:

        self.title = title
        self.body = body

    def render(self):

        return dbc.Card(
            [dbc.CardHeader(self.title), dbc.CardBody(self.body)],
        )
