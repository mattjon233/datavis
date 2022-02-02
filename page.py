import dash_html_components as html
from styles import MAIN_STYLE

body = html.Div(
    children=[
        html.P(),

        html.H6(children='Apenas.', id='initial-page'),

        html.Iframe(id='precip-map',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=precipMapGeoJson',
                    style={'display':'none'}),

        html.Iframe(id='idh',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=precip',
                    style={'display':'none'}),

        html.Iframe(id='spi-lines',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+dashboard',
                    style={'display':'none'}),

        html.Iframe(id='spi-map',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=spiMapGeoJson',
                    style={'display':'none'})

    ],
    style = MAIN_STYLE
)