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
dash.register_page(__name__, path = '/Archive', title = 'Archive')

layout = html.Div([
    html.H1('This is our Archive page'),
    html.Div('This is our Archive page content.'),
])