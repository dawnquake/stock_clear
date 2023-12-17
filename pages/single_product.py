import glob
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from pages.footer import footer_layout
from pages.styles import center_style



def generate_single_product_layout(single_product_df):

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