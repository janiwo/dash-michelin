from dataclasses import dataclass
from typing import Dict
import dash_bootstrap_components as dbc


@dataclass
class ButtonPopover:

    children: str
    target: str
    trigger: str = "hover"

    def render(self) -> dbc.Popover:

        return dbc.Popover(
            children=self.children,
            target=self.target,
            body=True,
            trigger=self.trigger,
            delay=dict(show=500, hide=50),
        )
