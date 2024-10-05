from dash_bootstrap_components import Button


class ButtonComponent:
    def __init__(
        self, label: str, id: str = None, color: str = "light", className: str = "me-1"
    ):
        self.label = label
        self.id = id if id else "btn-" + self.clean_string(label)
        self.color = color
        self.className = f"button-component {className}"

    def render(self) -> Button:
        return Button(
            self.label, id=self.id, color=self.color, className=self.className
        )

    @staticmethod
    def clean_string(string: str) -> str:
        return string.lower().replace(" ", "-")
