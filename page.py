import dash_html_components as html
from styles import MAIN_STYLE
# import dash_bootstrap_components as dbc

body = html.Div(
    children=[
        # # Will contain all the pages contents
        # dbc.Container(
        #     children=[

        #         html.P(),

        #         dbc.Col(id='div-main',
        #             children=[
                        html.Iframe(src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+dashboard',
                                    style={"height": "435px", "width": "100%"}),

                        html.Iframe(src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=spiMapGeoJson',
                                    style={"height": "700px", "width": "100%"})
        #             ]
        #         )
        #     ]
        # )
    ],
    style = MAIN_STYLE
)