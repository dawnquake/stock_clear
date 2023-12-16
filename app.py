# app.py
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


from pages import product_page, home_page


app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server

# Define app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Define callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/product_page':
        return product_page.layout
    
    else:
        return home_page.layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)