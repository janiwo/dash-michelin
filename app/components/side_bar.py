import dash_bootstrap_components as dbc


class SideBar:
    def __init__(self, children: dbc.ListGroupItem, id: str):
        self.children = children
        self.id = id

    def render(self):
        return dbc.Card(
            [
                dbc.CardHeader(
                    dbc.Button(
                        "X",
                        id=f"side-bar-close-{self.id}",
                        color="light",
                        style={"float": "right"},
                    )
                ),
                dbc.CardBody(children=self.children),
            ],
            id=self.id,
            class_name="side-bar slide",
        )
