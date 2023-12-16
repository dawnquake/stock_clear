# pages/product_page_en.py
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from pages.header import header_layout
from pages.footer import footer_layout

app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])





product_page_content = [

    dbc.Row([
        dbc.Col([ html.P("Here is the Carousel") ]),
        dbc.Col([ html.P("Here is the Product Descriptions") ]),
    ])
]

layout = html.Div(header_layout
                  + product_page_content
                  + footer_layout)
