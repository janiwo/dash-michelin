import dash_bootstrap_components as dbc

from layouts.navbar.modal_about import modal_about


navbar = dbc.NavbarSimple(
    children=[dbc.NavItem(dbc.NavLink("About", id="navbar-navlink")), modal_about],
    brand="Dash Michelin",
    brand_href="#",
    color="primary",
    dark=True,
    class_name="navbar",
)
