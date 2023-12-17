# app.py

import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, dcc, clientside_callback
import dash_bootstrap_components as dbc
from pages import product_page, home_page, single_product, header, error_page
import copy, time



app = Dash(__name__, 
           external_stylesheets=[dbc.themes.JOURNAL], 
           suppress_callback_exceptions=True,                # Dynamic Pages needs this to be True to to work
           )
server = app.server

# Define app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

products_db = pd.read_csv("db/products_db.csv", dtype=str)
products_db['product_url'] = '/product/' + products_db['ProductID'].astype('string')

# Define callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'),
              prevent_initial_call='initial_duplicate')
def display_page(pathname):

    original_index = copy.deepcopy(app.index_string)

    if '/product_page' in pathname:

        app.title = 'Product Page'
        product_page_search_phrase = pathname.split('/')[-1]
        

        return product_page.gen_product_page_layout(product_page_search_phrase)

    elif '/product/' in pathname:

        ProductID_in_pathname = pathname.split('/')[2]
        products_db_single_product = products_db[products_db['ProductID'] == ProductID_in_pathname]
        layout_single_product = single_product.generate_single_product_layout(products_db_single_product)

        return layout_single_product

    elif pathname == '/header':

        return header.layout

    elif pathname == '/':

        app.title = 'HomePage'


        return home_page.layout

    else:


        return error_page.layout

@app.callback(
    Output('redirect-output', 'children'),
    [Input('redirect-button', 'n_clicks')],
    [State('redirect-input', 'value')]
)
def redirect_to_page(n_clicks, input_value):
    if n_clicks > 0 and input_value:
        return dcc.Location(pathname=f'/product_page/{input_value}', id='redirect-url')
    else:
        return ""







# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)