# pages/home.py
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from pages.footer import footer_layout

center_style ={
    "text-align": "center"
}

carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/homepage/homepage_carousel/slide1.jpg"},
        {"key": "1", "src": "/static/homepage/homepage_carousel/slide2.jpg"},
        {"key": "1", "src": "/static/homepage/homepage_carousel/slide3.jpg"},
        {"key": "1", "src": "/static/homepage/homepage_carousel/slide1.jpg"},
        {"key": "1", "src": "/static/homepage/homepage_carousel/slide2.jpg"},
    ],
    controls=True,
    indicators=True,
    interval=1000,
)

product_bar_image_paths = [
    "/static/homepage/homepage_carousel/slide1.jpg",
    "/static/homepage/homepage_carousel/slide2.jpg",
    "/static/homepage/homepage_carousel/slide3.jpg",
    "/static/homepage/homepage_carousel/slide1.jpg",
    "/static/homepage/homepage_carousel/slide2.jpg",
    "/static/homepage/homepage_carousel/slide3.jpg",
]

def create_product_bar(product_bar_image_paths):

    product_bar = dbc.Container([
        dbc.Row([html.H4('This is the product bar 1', style=center_style)]),
        dbc.Row([
            dbc.Col(html.Img(src=image, style={"width": "100%"}), width=2)  # Adjust width as needed
            for image in product_bar_image_paths
        ])
    ])

    return product_bar






product_bar = dbc.Container([
    dbc.Row([html.H4('This is the product bar 1', style=center_style)]),
    dbc.Row([
        dbc.Col(html.Img(src=image, style={"width": "100%"}), width=2)  # Adjust width as needed
        for image in product_bar_image_paths
    ])
])



layout = html.Div(
    
    [html.H1('This is the home page'),
    dbc.Row(dbc.Col(carousel)),
    create_product_bar(product_bar_image_paths),
    create_product_bar(product_bar_image_paths),
    create_product_bar(product_bar_image_paths),] 
    + footer_layout
    
)