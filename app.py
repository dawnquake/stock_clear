# Have not figured out how to 
# app.py

import copy

import pandas as pd

import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback
import dash_bootstrap_components as dbc

app = Dash(__name__,
           external_stylesheets=[dbc.themes.JOURNAL], 
           use_pages=True)

server = app.server
app._favicon = 'box-fill.svg'

def gen_app_layout(pages = dash.page_registry.values()):

    layout =  html.Div([
                html.H1('Multi-page app with Dash Pages'),
                html.Div([
                    html.Div(
                        dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
                    ) for page in pages
                ]),
                
                dash.page_container
            ])

    return layout

app.layout = gen_app_layout(pages = dash.page_registry.values())

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)