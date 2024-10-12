from dash_bootstrap_components import Button
from dash import html


class ButtonComponent:
    def __init__(
        self,
        label: str,
        icon: str = None,
        id: str = None,
        color: str = "light",
        className: str = "me-1",
    ):
        self.label = label
        self.icon = icon
        self.id = id if id else "btn-" + self.clean_string(label)
        self.color = color
        self.className = f"button-component {className}"

    def render(self) -> Button:
        return Button(
            html.I(className=self.icon) if self.icon else self.label,
            id=self.id,
            color=self.color,
            className=self.className,
            style={"margin": "0.75vh"},
        )

    @staticmethod
    def clean_string(string: str) -> str:
        return string.lower().replace(" ", "-")
