# pages/product_page_en.py
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from pages.footer import footer_layout

def gen_product_page_layout(search_phrase):

    product_page_content = [
        html.H3(f'This is the search phrase {search_phrase}'),
        dbc.Row([
            dbc.Col([ html.P("Here are the filter elements") ]),
            dbc.Col([ html.P("Here are the results of the filter") ]),
        ])
    ]

    layout = html.Div(
                    product_page_content
                    + footer_layout)

    return layout



