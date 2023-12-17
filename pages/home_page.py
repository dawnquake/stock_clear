# pages/home.py
import glob
import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from pages.footer import footer_layout
from pages.styles import center_style
# from pages.header import header_layout

homepage_product_bar_1_paths = glob.glob('static/homepage/homepage_product_bar_1/*')
homepage_product_bar_2_paths =  glob.glob('static/homepage/homepage_product_bar_2/*')
homepage_product_bar_3_paths =  glob.glob('static/homepage/homepage_product_bar_3/*')
homepage_carousel_paths = glob.glob('static/homepage/homepage_carousel/*')



carousel = dbc.Carousel(
    items=[
        {'src': path} for path in homepage_carousel_paths
    ],
    controls=True,
    indicators=True,
    interval=1000,
)

def create_product_bar(product_bar_image_paths,
                       product_bar_title = ''):

    product_bar = dbc.Container([
        dbc.Row([html.H4(product_bar_title, style=center_style)]),
        dbc.Row([
            dbc.Col(html.Img(src=image, style={"width": "100%"}), width=2)  # Adjust width as needed
            for image in product_bar_image_paths
        ])
    ])

    return product_bar

layout = html.Div(
    

    [

    html.Link(rel='icon',href='/static/box-fill.svg',type='image/x-icon'),    
        
    html.H1('This is the home page'),
    dbc.Row(dbc.Col(carousel)),
    create_product_bar(homepage_product_bar_1_paths, 'Product Bar 1'),
    create_product_bar(homepage_product_bar_2_paths, 'Product Bar 2'),
    create_product_bar(homepage_product_bar_3_paths, 'Product Bar 3'),]



    + footer_layout
    
)