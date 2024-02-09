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
lines = open('db/homepage_carousel_links.txt', 'r').read().splitlines()[1:]
homepage_carousel_links = [ROOT_URL + '/{}'.format(line) for line in lines]
carousel = dbc.Carousel(
    items=
    [{'src': path,'href': link} for path, link in zip(homepage_carousel_paths, homepage_carousel_links)],
    controls=True,
    indicators=True,
    interval=1000,
)

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
def create_productbar(productbar_image_paths,
                       productbar_link_paths,
                       productbar_title = ''):

    lines = open(productbar_link_paths, 'r').read().splitlines()[1:]

    productbar_links = [ROOT_URL + '/{}'.format(line) for line in lines]
    productbar_title = dbc.Row([html.H4(productbar_title, style=center_style)])

    productbar_content = []
    for link, image in zip(productbar_links, productbar_image_paths):
        productbar_content.append(dbc.Col([html.A(href=link, children=[html.Img(src=image, style = {'width':'100%'})])]))
    productbar_content = dbc.Row(productbar_content)

    productbar = dbc.Container([
        productbar_title, productbar_content
    ])


    return productbar

# Content for the home page
main_content = [


    # html.H1('This is our Home page'),


    ##########################################################

    html.Div(id='url-output'), 

    #########################################################

    dbc.Row([dbc.Col(carousel, width = 6)], justify = 'center'),
    create_productbar(homepage_product_bar_1_paths,'db/homepage_productbar1.txt', 'Produse Noi'),
    create_productbar(homepage_product_bar_2_paths,'db/homepage_productbar2.txt', 'Produse Reduse'),
    create_productbar(homepage_product_bar_3_paths,'db/homepage_productbar3.txt', 'Produse Remarkabile'),

]

footer_content = footer_layout
layout = html.Div(header_layout + main_content + footer_content)


