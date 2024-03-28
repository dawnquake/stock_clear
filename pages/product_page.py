# std imports
import copy
import glob
from urllib.parse import urlparse, parse_qs

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

# Creates the layout
def layout(search_phrase, products_db = products_db):

    ##########################################################
    # Hidden div for search bar redirect
    # Hidden div for getting current URL
    search_redirect_hidden_dev = [html.Div(id='url-output'),  dcc.Location(id='current-page', refresh=False),]
    #########################################################

    product_page_content = [
        html.P(f'Dumneavoastra ati cautat {search_phrase}'),
        dbc.Row([
            dbc.Col(filter_element, width = 2),
            dbc.Col(html.Div(id ='filter_results'), width = 10),
        ]),

    ]

    layout = html.Div(header_layout 
                      + product_page_content
                      + search_redirect_hidden_dev
                      + footer_layout)

    return layout


filter_element = [
    html.H4('Filtre'),
    html.P("Pret Minim"),
    dbc.Input(type='number', step=1, id = 'min_price'),
    html.P("Pret Maxim"),
    dbc.Input(type='number', step=1, id = 'max_price'),
]

@callback(
    Output(component_id='filter_results', component_property='children'),
    Input(component_id='min_price', component_property='value'),
    Input(component_id='max_price', component_property='value'),
    Input('current-page', 'href'),
)
def gen_filter_results(min_price, max_price, URL):

    search_phrase = parse_qs(urlparse(URL).query)['search_phrase'][0]
    min_price = 0 if min_price == None else min_price
    max_price = 99999 if max_price == None else max_price

    filtered_df = products_db[products_db.apply(lambda row: row.astype(str).str.contains(search_phrase, case=False).any(), axis=1)]
    filtered_df = filtered_df.astype({'ProductPrice' : float})
    filtered_df = filtered_df[(filtered_df['ProductPrice'] > min_price) & (filtered_df['ProductPrice'] < max_price)]
    filtered_df['ProductLink'] = ROOT_URL + '/product/' + filtered_df['ProductID']
    filtered_df['ProductImageLink'] = '#'
    for index,row in filtered_df.iterrows():
        try:
            filtered_df.loc[index, 'ProductImageLink'] = glob.glob('static/product/{}/*'.format(filtered_df.loc[index, 'ProductID']))[0]
        except:
            pass

    filtered_df.reset_index(inplace = True)



    filter_results = [html.H4('Rezultate'), html.Hr()]

    for index, row in filtered_df.iterrows():

        filter_results.extend([
            html.A(href = row['ProductLink'],
                   children = [dbc.Row([
                        dbc.Col([html.Img(src=row['ProductImageLink'], style = desktop_product_search_image_style)]),
                        dbc.Col([html.H4(row['ProductName']),
                                 html.P('Codul Produsului        : {}'.format(row['ProductID'])), 
                                 html.P('Pretul Produsului       : {}'.format(row['ProductPrice'])), 
                                 html.P('Descrierea Produsului   : {}'.format(row['ProductDesc']))]
                                 , style={'text-align':'left'}, width = 9),
                        ])
                   ]
            ),
            html.Br(),
        ])



    return filter_results
















