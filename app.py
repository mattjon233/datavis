import dash
from flask_caching import Cache
import dash_html_components as html
from page import body
from sidebar import sidebar
from dash.dependencies import Input, Output, State

# Commands to create Dash app

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

# Callbacks

@app.callback(
   [Output('dd-vis', 'value'),
   Output('radio-type-prec', 'value'),
   Output('radio-type-spi', 'value')],
   [Input('initial-page-button', 'n_clicks_timestamp')]
)
def initial_page(click):
   if click:
      return [None, None, None]

@app.callback(
   # page styles
   [Output('initial-page', 'style'),
   Output('precip-map', 'style'),
   Output('precip-lines', 'style'),
   Output('idh', 'style'),
   Output('pib','style'),
   Output('spi-lines', 'style'),
   Output('spi-map', 'style'),
   # sidebar styles
   Output('radio-type-prec', 'style'),
   Output('radio-type-spi', 'style'),
   Output('title-type', 'style')],
   # inputs
   [Input('initial-page-button', 'n_clicks_timestamp'),
   Input('dd-vis', 'value'),
   Input('radio-type-prec', 'value'),
   Input('radio-type-spi', 'value')]
)
def page_type_style(click, vis, type_prec, type_spi):
   none = {'display':'none'}
   initial_dict = {'display':''}
   block = {'display':'block'}
   default = {'display':''}

   if vis == 'prec':
      if type_prec == 'map':
         map_dict = {'height': '850px', 'width': '65%'}
         return [none,map_dict,none,none,none,none,none,
                 block, none, default]
      elif type_prec == 'lines':
         lines_dict = {'height': '550px', 'width': '80%'}
         return [none,none,lines_dict,none,none,none,none,
                 block, none, default]         
      elif type_prec == 'idh':
         idh_dict = {'height': '550px', 'width': '40%'}
         return [none,none,none,idh_dict,none,none,none,
                 block, none, default]
      elif type_prec == 'pib':
         idh_dict = {'height': '550px', 'width': '50%'}
         return [none,none,none,none,idh_dict,none,none,
                 block, none, default]
      else:
         return [none,none,none,none,none,none,none,
                 block, none, default]

   elif vis == 'spi':
      if type_spi == 'lines':
         lines_dict = {'height': '550px', 'width': '80%'}
         return [none,none,none,none,none,lines_dict,none,
                 none, block, default]
      elif type_spi == 'map':
         map_dict = {'height': '850px', 'width': '65%'}
         return [none,none,none,none,none,none,map_dict,
                  none, block, default]
      else:
         return [none,none,none,none,none,none,none,
                  none, block, default]

   else:
      return [initial_dict,none,none,none,none,none,none,
               none,none,none]

# Main

if __name__ == '__main__':

    # Necessary to run the Dash program
    app.run_server(debug=True)
