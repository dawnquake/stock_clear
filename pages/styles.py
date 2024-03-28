from dash import html

# Dump for the styles
center_style = {"text-align": "center"}

# Define styles for the navigation bar
nav_bar_style = {
    'background-color': '#4CAF50',  # Green background color
    'padding': '10px',  # Padding for better spacing
    'color': 'white',  # Text color
    'text-align': 'center'  # Center-align text
}

# Define styles for the logo
logo_style = {
    'width': '50px',  # Adjust the width as needed
    'height': '50px',  # Adjust the height as needed
    'margin-right': '10px'  # Margin to separate the logo from other elements
}

# Define styles for the search bar
search_bar_style = {
    'width': '300px',  # Adjust the width as needed
    'margin-right': '10px'  # Margin to separate the search bar from other elements
}

# html for Icon only 
btn0_content = html.Span([html.Div('', style = dict(paddingRight = '0.5vw', display = 'inline-block')),
                          html.I(className = 'bi bi-search' , style=dict(display='inline-block'))])

# image style
# Style all images to be 600 width and 800 height
# Autoscale image if not 600 width and 800 height
desktop_product_search_image_style = {
'width': '300px',
'height': '400px',
# 'object-fit': 'contain'  # This property prevents the image from being cropped
}