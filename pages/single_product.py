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
from pages.header import *
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
dash.register_page(__name__,
                   path_template='/product/<product_id>', 
                   title = 'Single Product')

products_db = pd.read_csv("db/products_db.csv", dtype=str)
products_db['product_url'] = '/product/' + products_db['ProductID'].astype('string')

def layout(product_id = None):

    single_product_df = products_db[products_db['ProductID'] == product_id]

    ##########################################################
    # Hidden dev for search bar redirect
    search_redirect_hidden_dev = [html.Div(id='url-output'), ]
    #########################################################

    if single_product_df.empty == True:
        
        single_product_content = [

            html.H3('Sorry this product is not found'),
            html.Hr(),
        ]

        layout = html.Div(single_product_content  
                        + footer_layout)
        
        return layout

    elif single_product_df.empty == False:

        (ProductID,
        ProductName,
        ProductPrice, 
        ProductDesc) = ((single_product_df.loc[:,'ProductID'].values[0]),
                        (single_product_df.loc[:,'ProductName'].values[0]),
                        (single_product_df.loc[:,'ProductPrice'].values[0]),
                        (single_product_df.loc[:,'ProductDesc'].values[0]),)

        product_carousel = dbc.Carousel(
            items=[
                {'src': '/' + path} for path in glob.glob('static/product/{}/*'.format(ProductID))
            ],
            controls=True,
            indicators=True,
            interval=1000,
        )

        single_product_content = [

            dbc.Row([
                dbc.Col([product_carousel]),
                dbc.Col([
                    dbc.Row([html.P('Nume Produs      : ' + ProductName, )]),
                    dbc.Row([html.P('Pret Produs      : ' + ProductPrice, )]),
                    dbc.Row([html.P('Descriere Produs : ' + ProductDesc, )]),
                ]),
            ]),


        ]

    layout = html.Div(header_layout
                      + search_redirect_hidden_dev
                      + single_product_content
                      + footer_layout)
    
    return layout
