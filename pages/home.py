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
dash.register_page(__name__, path='/', title = 'Homepage')

# glob find the files for the homepage
homepage_product_bar_1_paths = glob.glob('static/homepage/homepage_product_bar_1/*')
homepage_product_bar_2_paths =  glob.glob('static/homepage/homepage_product_bar_2/*')
homepage_product_bar_3_paths =  glob.glob('static/homepage/homepage_product_bar_3/*')
homepage_carousel_paths = glob.glob('static/homepage/homepage_carousel/*')

# creating the homepage carousel
carousel = dbc.Carousel(
    items=[
        {'src': path} for path in homepage_carousel_paths
    ],
    controls=True,
    indicators=True,
    interval=1000,
)

# Header layout
header_layout = [
    html.Div([
        dbc.Row([
            dbc.Col(dbc.Input(id = 'search_phrase', type = 'text', size = 'lg'),
                    width = {'size' : 5, 'offset' : 3},
                    style = {'text-align':'right', 'padding': '0px'}),
            dbc.Col(dbc.Button(children=btn0_content, id='search_button', size = 'lg'), style = {'padding': '0px'}),
        ], justify = 'center'),
    ]
)]

# Callback for the search bar
@callback(
    Output('url-output', 'children', allow_duplicate=True),
    Input('search_phrase', 'n_submit'),
    Input('search_button', 'n_clicks'),
    State('search_phrase', 'value'),
    prevent_initial_call = True,
)
def redirect_url(n_clicks, search_button, search_phrase):

    # print(n_clicks, search_button, search_phrase)
    # print("{}/product_search?search_phrase={}".format(ROOT_URL, search_phrase))

    if (n_clicks is None) and (search_button is None):
        raise PreventUpdate

    return dcc.Location(href = "{}/product_search?search_phrase={}".format(ROOT_URL, search_phrase),
                        id = 'nope0')

# function for creating homepage product bar
def create_product_bar(product_bar_image_paths,
                       product_bar_title = ''):

    product_bar = dbc.Container([
        dbc.Row([html.H4(product_bar_title, style=center_style)]),
        dbc.Row([
            dbc.Col(html.Img(src=image, style={"width": "100%"}), width=2)  # Adjust width as needed
            for image in product_bar_image_paths
        ])
    ])

    return product_bar

# Content for the home page
main_content = [


    html.H1('This is our Home page'),


    ##########################################################

    html.Div(id='url-output'), 

    #########################################################

    dbc.Row([dbc.Col(carousel, width = 6)], justify = 'center'),
    create_product_bar(homepage_product_bar_1_paths, 'Product Bar 1'),
    create_product_bar(homepage_product_bar_2_paths, 'Product Bar 2'),
    create_product_bar(homepage_product_bar_3_paths, 'Product Bar 3'),

]

footer_content = footer_layout
layout = html.Div(header_layout + main_content + footer_content)


