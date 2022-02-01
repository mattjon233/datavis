import dash_html_components as html
import callbacks
from app import app, server
from page import body
from sidebar import sidebar

# Command to create the layout of the app
app.layout = html.Div(className='row wrapper', children=[sidebar, body])

if __name__ == '__main__':

    # Necessary to run the Dash program
    app.run_server(debug=True)
