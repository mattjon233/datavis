import dash
from flask_caching import Cache
import dash_html_components as html
from page import body
from sidebar import sidebar

# Command to create Dash app
app = dash.Dash(__name__, prevent_initial_callbacks=True)
server = app.server

app.title = 'Visualização de Dados'
app.config.suppress_callback_exceptions = True
app.config.update({
'assets_folder': 'assets',
'include_asset_files': True,
'assets_external_path': '',
})
cache = Cache(server, config=
   {
   'CACHE_TYPE': 'filesystem',
   'CACHE_DIR': 'cache-directory',
   }
)

# Command to create the layout of the app
app.layout = html.Div(className='row wrapper', children=[sidebar, body])

if __name__ == '__main__':

    # Necessary to run the Dash program
    app.run_server(debug=True)
