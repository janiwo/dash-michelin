from dash_bootstrap_components import Button


class Button:
    def __init__(
        self, label: str, id: str = None, color: str = "light", className: str = "me-1"
    ):
        self.label = label
        self.id = id if id else "btn-" + self.clean_string(label)
        self.color = color
        self.className = className
        self.style = {"boxShadow": "2px 2px 5px rgba(0, 0, 0, 0.3)"}

    def render(self) -> Button:
        return Button(
            self.label,
            id=self.id,
            color=self.color,
            className=self.className,
            style=self.style,
        )

    def clean_string(string: str) -> str:
        return string.lower().replace(" ", "-")
