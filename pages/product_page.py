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

#local imports
from pages.footer import footer_layout
from pages.styles import center_style

# dash register page
# Set the page title and path here
dash.register_page(__name__,
                   path='/product_search', 
                   title = 'Product Page',
                   redirect_from=["/product", "/product/"])

products_db = pd.read_csv("db/products_db.csv", dtype=str)

def layout(search_phrase = None, products_db = products_db):

    if search_phrase == None:
        search_phrase = ''
    if search_phrase != None:
        products_db = products_db[products_db['ProductName'].str.contains(search_phrase, case = False)]

    print(products_db)

    product_page_content = [
        html.H3(f'This is the search phrase {search_phrase}'),
        dbc.Row([
            dbc.Col([ html.P("Here are the filter elements") ]),
            dbc.Col([ html.P("Here are the results of the filter") ]),
        ]),

    dash_table.DataTable(products_db.to_dict('records'),
                         [{"name": i, "id": i} for i in products_db.columns])

    ]

    layout = html.Div(
                    product_page_content
                    + footer_layout)

    return layout





