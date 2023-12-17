import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State,ctx
import dash_bootstrap_components as dbc
from pages.footer import footer_layout
from pages.styles import center_style



layout = html.Div([
html.P('SORRIES')
] + footer_layout)