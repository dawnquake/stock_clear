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
from pages.styles import *

# import local settings for running server local
# if import fail then on remote server
ROOT_URL = 'https://www.alibabaro.com'
try:
    from pages.local_settings import LOCAL_URL
    ROOT_URL = copy.deepcopy(LOCAL_URL)
except:
    pass

# footer layout
# Just some page redirection tbh
footer_layout = [html.Footer([
        dbc.Row([
            dbc.Col([
                html.H6("Explore Alibabaro.com"),
                html.Br(),
                html.A("About Us"),
                html.Br(),
                html.A("Careers"),
                html.Br(),
                html.A("Investor Relations"),
                html.Br(),
                html.A("JD Advertising"),
                html.Br(),
            ], className="footer-column"),

            dbc.Col([
                html.H6("Customer Service"),
                html.Br(),
                html.A("Help Center"),
                html.Br(),
                html.A("Customer Service"),
                html.Br(),
                html.A("Returns"),
                html.Br(),
                html.A("Product Recalls"),
                html.Br(),
            ], className="footer-column"),

            dbc.Col([
                html.H6("Contact Us"),
                html.Br(),
                html.A("Online Service"),
                html.Br(),
                html.A("Phone Service"),
                html.Br(),
                html.A("Email Service"),
                html.Br(),
                html.A("Business Cooperation"),
                html.Br(),
            ], className="footer-column"),

            dbc.Col([
                html.H6("Follow Us"),
                html.Br(),
                html.A("WeChat"),
                html.Br(),
                html.A("Weibo"),
                html.Br(),
                html.A("Facebook"),
                html.Br(),
                html.A("Twitter"),
                html.Br(),
            ], className="footer-column"),

        ], className="footer-content")
    ], className="footer"),
    
    html.H4('', style={"text-align": "center"})]