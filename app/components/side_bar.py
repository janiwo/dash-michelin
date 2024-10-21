import dash_bootstrap_components as dbc


class SideBar:
    def __init__(self, children: dbc.ListGroupItem, id: str, action_button: str):
        self.children = children
        self.id = id
        self.action_button = action_button

    def render(self):
        return dbc.Card(
            [
                dbc.CardHeader(
                    children=[
                        dbc.Button(
                            self.action_button,
                            id=f"side-bar-{self.action_button.lower()}-{self.id}",
                            color="danger",
                            outline=True,
                            style={"float": "left"},
                        ),
                        dbc.Button(
                            "X",
                            id=f"side-bar-close-{self.id}",
                            color="light",
                            style={"float": "right"},
                        ),
                    ]
                ),
                dbc.CardBody(children=self.children, id=f"side-bar-body-{self.id}"),
            ],
            id=self.id,
            class_name="side-bar slide",
        )
