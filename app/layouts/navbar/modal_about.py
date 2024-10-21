from dash import html
import dash_bootstrap_components as dbc

modal_about = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("About")),
        dbc.ModalBody(
            [
                html.P(
                    [
                        "This is a submission for the ",
                        html.A(
                            "Ploty Autumn App Challange",
                            href="https://community.plotly.com/t/autumn-app-challenge/87373",
                            target="_blank",
                        ),
                        " created by Felipe Forero Meola (",
                        html.A(
                            "Github",
                            href="https://github.com/Felipeforerome",
                            target="_blank",
                        ),
                        ", ",
                        html.A(
                            "LinkedIn",
                            href="https://www.linkedin.com/in/felipe-forero-meola/",
                            target="_blank",
                        ),
                        ") and Jan-Niklas Wolters (",
                        html.A(
                            "Github",
                            href="https://github.com/janiwo",
                            target="_blank",
                        ),
                        ", ",
                        html.A(
                            "LinkedIn",
                            href="https://www.linkedin.com/in/jan-niklas-wolters-189333179/",
                            target="_blank",
                        ),
                        ").",
                    ]
                ),
                html.P(
                    [
                        "Please reach out to us if you have anything to share about the app.\n",
                        "You can view the source code on ",
                        html.A(
                            "Github",
                            href="https://github.com/janiwo/dash-michelin",
                            target="_blank",
                        ),
                    ]
                ),
            ]
        ),
    ],
    id="modal-navbar",
)
