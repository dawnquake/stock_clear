# Template page
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


header_layout = [


    html.Nav([
        
        dcc.Dropdown(options=['cat','dog'] ,id='pandas-dropdown-2')



    ]),


]


