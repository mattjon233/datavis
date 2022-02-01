import dash
from flask_caching import Cache

# Command to create Dash app
app = dash.Dash(__name__, prevent_initial_callbacks=True)
app.title = 'Visualização de Dados'
app.config.suppress_callback_exceptions = True
app.config.update({
'assets_folder': 'assets',
'include_asset_files': True,
'assets_external_path': '',
})
server = app.server
cache = Cache(server, config=
   {
   'CACHE_TYPE': 'filesystem',
   'CACHE_DIR': 'cache-directory',
   }
)
