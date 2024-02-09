# std imports
import copy
import glob

# data analytics imports
import pandas as pd

# dash imports
import flask
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback, dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from pages.styles import btn0_content

#local imports
from pages.styles import *

# import local settings for running server local
# if import fail then on remote server
ROOT_URL = 'https://www.alibabaro.com'
try:
    from pages.local_settings import LOCAL_URL
    ROOT_URL = copy.deepcopy(LOCAL_URL)
except:
    pass


# Header layout
header_layout = [
    html.Div([
        # navbar,
        dbc.Row([
            dbc.Col(html.A(
                href=ROOT_URL,
                children=[
                    html.Img(
                        src='/assets/ALIBABARO_LOGO_SVG.svg',   # Remember to add / in front of image here please
                    )
                ]
            )),
            dbc.Col(dbc.Input(id = 'search_phrase', type = 'text', size = 'lg'),
                    width = {'size' : 5,},
                    style = {'text-align':'right', 'padding': '0px'}),
            dbc.Col(dbc.Button(children=btn0_content, id='search_button', size = 'lg'), style = {'padding': '0px'}),
        ], justify = 'center'),
        html.Hr(),
    ]
)]



