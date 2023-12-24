import dash
from dash import html
from dash.dependencies import Input, Output
from dash_router import Router

from pages import page1, page2

app = dash.Dash(__name__)

# Use the dash_router library to handle routing
router = Router(app)

app.layout = html.Div([
    router,
])

# Define the routes and associate layouts with pages
router.routes([
    {'pathname': '/page1', 'layout': page1.layout},
    {'pathname': '/page2', 'layout': page2.layout},
])

if __name__ == '__main__':
    app.run_server(debug=True)






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


app = Dash(__name__, 
           external_stylesheets=[dbc.themes.JOURNAL], 
           suppress_callback_exceptions=True,                # Dynamic Pages needs this to be True to to work
           title = 'HomePage',
           )
server = app.server