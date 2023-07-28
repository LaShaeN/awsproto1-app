import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name='Home')


jumbotron = html.Div(
    dbc.Container(
        [
            html.H1("Alzheimer's Disease", className="display-3"),
            html.P("RNAseq Website", className="display-4"),
            # html.Img(src="/assets/AD_brain_versus_normal.jpg"),
            html.P(
                "This is an interactive website for the interactive exploration of AD transcriptomic data sets",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "This website is currently under development."
            ),
            html.P(
                dbc.Button("Learn more", color="success"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


layout = dbc.Container([

    jumbotron
], 
fluid=True,
style={'position': 'sticky', }
)
