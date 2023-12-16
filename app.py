# app.py
import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
from pages import product_page_en, home_page_en

app = dash.Dash(__name__)
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
        return product_page_en.layout
    else:
        return home_page_en.layout

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)