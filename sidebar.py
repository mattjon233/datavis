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

                # Categories and options

                html.H6(children='TIPO DE GRÁFICO:', id='title-type'),
                dcc.Dropdown(
                    id='dd-type',
                    options=[{'label': i, 'value': i} for i in ['SPI', 'PRECIPITAÇÃO']],
                    value='SPI',
                    style={'display': '', 'width':'12rem'},
                    clearable=False
                )
            ]
        )
    ],

    # Style settings
    style=SIDEBAR_STYLE
)