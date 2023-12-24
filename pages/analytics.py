# std imports
import copy

# data analytics imports
import pandas as pd

# dash imports
import flask
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback, dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

# dash register page
# Set the page title and path here
dash.register_page(__name__, title = 'Analytics')

layout = html.Div([
    html.H1('This is our Analytics page'),
    html.Div([
        "Select a city: ",
        dcc.RadioItems(
            options=['New York City', 'Montreal', 'San Francisco'],
            value='Montreal',
            id='analytics-input'
        )
    ]),
    html.Br(),
    html.Div(id='analytics-output'),
])


