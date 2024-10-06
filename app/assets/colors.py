from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    michelin_red: str = "#BB2631"
    michelin_red_rgb: str = "rgb(187, 38, 49)"

    light_red: str = "#FEE2E2"
    light_red_rgb: str = "rgb(254, 226, 226)"

    white: str = "#FFFFFF"
    black: str = "#000000"

    light_grey: str = "#D3D3D3"

    gold: str = "#FFD700"
    silver: str = "#C0C0C0"
    bronze: str = "#CD7F32"

    transparent: str = "rgba(0,0,0,0)"
