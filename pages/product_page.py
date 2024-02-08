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
from pages.header import *
from pages.footer import footer_layout
from pages.styles import *

# import local settings for running server local
# if import fail then on remote server
ROOT_URL = 'https://www.alibabaro.com'
try:
    from pages.local_settings import LOCAL_URL
    ROOT_URL = copy.deepcopy(LOCAL_URL)
except:
    pass


# dash register page
# Set the page title and path here
# Read the db for the products
dash.register_page(__name__,
                   path='/product_search', 
                   title = 'Product Page',
                   redirect_from=["/product", "/product/"])

products_db = pd.read_csv("db/products_db.csv", dtype=str)

filter_element = [html.P("Here are the filter elements"),]

filter_results = [html.P("Here are the results of the filter"),]

# Creates the layout
def layout(search_phrase = None, products_db = products_db):

    ##########################################################
    # Hidden dev for search bar redirect
    search_redirect_hidden_dev = [html.Div(id='url-output'), ]
    #########################################################
    

    if search_phrase == None:
        search_phrase = ''
    if search_phrase != None:
        products_db = products_db[products_db['ProductName'].str.contains(search_phrase, case = False)]

    print(products_db)

    product_page_content = [
        html.Div(id='url-output'), 
        html.H3(f'You have searched for {search_phrase}'),
        dbc.Row([
            dbc.Col(filter_element),
            dbc.Col(filter_results),
        ]),

    dash_table.DataTable(products_db.to_dict('records'),
                         [{"name": i, "id": i} for i in products_db.columns])

    ]

    layout = html.Div(header_layout 
                      + product_page_content
                      + search_redirect_hidden_dev
                      + footer_layout)

    return layout





