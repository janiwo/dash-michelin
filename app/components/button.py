from dash_bootstrap_components import Button


def clean_string(string: str) -> str:
    return string.lower().replace(" ", "-")


def button(label: str) -> Button:
    return Button(
        label,
        id="btn-" + clean_string(label),
        color="light",
        className="me-1",
        style={"boxShadow": "2px 2px 5px rgba(0, 0, 0, 0.3)"},
    )
