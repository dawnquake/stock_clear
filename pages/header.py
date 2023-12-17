# Template page
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, register_page
import dash_bootstrap_components as dbc


layout = html.Div([
    dcc.Input(id='redirect-input', type='text', placeholder='Enter anything and press button'),
    html.Button('Submit', id='redirect-button', n_clicks=0),
    html.Div(id='redirect-output'),
])

