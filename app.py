# app.py

# std imports
import copy

# data analytics imports
import pandas as pd

# dash imports
import flask
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

# Setting up the app and the server
app = Dash(__name__,
           external_stylesheets=[dbc.themes.JOURNAL],
           suppress_callback_exceptions=True, 
           use_pages=True)

server = app.server
app._favicon = 'box-fill.svg'

# layout generation through a function
# Define callback to update page content based on URL
# Initial layout
# Define app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

products_db = pd.read_csv("db/products_db.csv", dtype=str)
products_db['product_url'] = '/product/' + products_db['ProductID'].astype('string')

app.layout = html.Div([
    dash.page_container,
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)