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
                   path_template='/product/<product_id>', 
                   title = 'Single Product')

products_db = pd.read_csv("db/products_db.csv", dtype=str)
products_db['product_url'] = '/product/' + products_db['ProductID'].astype('string')

def layout(product_id=None):

    single_product_df = products_db[products_db['ProductID'] == product_id]

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
                    dbc.Row([html.P('Product ID : ' + ProductID, )]),
                    dbc.Row([html.P('Product Name : ' + ProductName, )]),
                    dbc.Row([html.P('Product Price : ' + ProductPrice, )]),
                    dbc.Row([html.P('Product Desc : ' + ProductDesc, )]),
                ]),
            ]),


            html.Hr()        
        ]


        layout = html.Div(single_product_content  
                          + footer_layout)

        return layout
