import dash
from dash import dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   name='Cell Chat',
                   order=[3])


layout = dbc.Container([])