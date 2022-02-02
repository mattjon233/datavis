import dash_core_components as dcc
import dash_html_components as html
from styles import SIDEBAR_STYLE

sidebar = html.Div(
    id='sidebar',
    children=[
        html.Div(
            children=[
                # Main Title
                html.H3(children='VISUALIZAÇÃO DE DADOS DE SPI E PRECIPITAÇÃO DO ESTADO DO CEARÁ', style={'text-align': 'center'}),

                html.Hr(),

                html.P(),
                html.P(),
            
                html.Button('Página Inicial', id='initial-page-button'),

                html.P(),

                html.H6(children='VISUALIZAÇÃO', id='title-vis'),
                dcc.Dropdown(
                    id='dd-vis',
                    options=[
                        {'label': 'Precipitação', 'value': 'prec'},
                        {'label': 'SPI', 'value': 'spi'},
                    ],
                    # value='prec',
                    style={'display': '', 'width':'12rem'},
                    clearable=False
                ),

                html.P(),

                # CASO : PRECIPITAÇÃO
                html.H6(children='TIPO', id='title-type', style={'display':'none'}),
                dcc.RadioItems(
                    id='radio-type-prec',
                    options=[
                        {'label': ' Mapa', 'value': 'map'},
                        {'label': ' Por IDH', 'value': 'idh'},
                    ],
                    # value='map',
                    labelStyle={'display': 'block'},
                    style={'display':'none'}
                ),

                # CASO : SPI
                dcc.RadioItems(
                    id='radio-type-spi',
                    options=[
                        {'label': ' Linhas', 'value': 'lines'},
                        {'label': ' Mapa', 'value': 'map'},
                    ],
                    # value='lines',
                    labelStyle={'display': 'block'},
                    style={'display':'none'}
                )
            ]
        )
    ],

    # Style settings
    style=SIDEBAR_STYLE
)