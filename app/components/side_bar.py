import dash_bootstrap_components as dbc


class SideBar:
    def __init__(self, children: dbc.ListGroupItem, id: str):
        self.children = children
        self.id = id

    def render(self):
        return dbc.Card(
            dbc.CardBody(children=self.children),
            id=self.id,
            class_name="side-bar slide",
        )
