from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    michelin_red: str = "#BB2631"
    michelin_red_rgb: str = "rgb(187, 38, 49)"

    light_red: str = "#FEE2E2"
    light_red_rgb: str = "rgb(254, 226, 226)"

    white: str = "#FFFFFF"
    white_rgb: str = "rgb(255, 255, 255)"

    black: str = "#000000"
    back_rgb: str = "rgb(0, 0, 0)"

    light_grey: str = "#D3D3D3"

    transparent: str = "rgba(0,0,0,0)"
