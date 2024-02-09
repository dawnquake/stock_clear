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
                   path='/contact', 
                   title = 'Contact',
                   redirect_from=["/contact", "/contact/"])



# Creates the layout
def layout():

    ##########################################################
    # Hidden dev for search bar redirect
    search_redirect_hidden_dev = [html.Div(id='url-output'), ]
    #########################################################

    contact_layout = [

        html.H4('Numar Telefon : +40722630273'),
        html.H4('Adresa Email  : alibabaro@outlook.com')

    ]

    layout = html.Div(header_layout 
                      + contact_layout
                      + search_redirect_hidden_dev
                      + footer_layout)

    return layout