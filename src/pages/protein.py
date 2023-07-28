import dash
from dash import dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   name='Protein Interactions', 
                   order=[4])


layout = dbc.Container([])