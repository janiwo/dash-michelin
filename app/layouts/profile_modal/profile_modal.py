import dash_bootstrap_components as dbc


header = dbc.ModalHeader(
    "Restaurant Profile",
    id="modal-restaurant-profile-header",
    class_name="bg-primary text-white",
)

body = dbc.ModalBody(
    id="modal-restaurant-profile-body",
)

profile_modal = dbc.Modal(
    id="modal-restaurant-profile",
    is_open=False,
    size="lg",
    children=[
        header,
        body,
    ],
)
