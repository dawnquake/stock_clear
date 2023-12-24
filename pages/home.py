import copy

import pandas as pd

import flask
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

dash.register_page(__name__, path='/', title = 'Homepage')

layout = html.Div([


    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),

    ##########################################################

    dcc.Input(id='url-input', type='text', value=''),
    html.Button('Go', id='url-button'),
    html.Div(id='url-output')

    #########################################################
])


@callback(
    Output('url-output', 'children'),
    [Input('url-button', 'n_clicks')],
    [State('url-input', 'value')]
)
def redirect_url(n_clicks, url_input):

    if n_clicks is None:
        raise PreventUpdate



    if not url_input.startswith('http://') and not url_input.startswith('https://'):
        url_input = 'http://' + url_input



    print(url_input)


    redirect_url = 'https://www.duckduckgo.com'

    return dcc.Location(pathname="/archive", id="someid_doesnt_matter")

if __name__ == '__main__':
    app.run_server(debug=True)