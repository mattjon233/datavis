import dash_html_components as html
from styles import MAIN_STYLE

body = html.Div(
    children=[
        html.P(),

        html.Div(id='initial-page', className='col-lg-10',
            children=[
                html.H4(
                    children=[
                        'ANÁLISES GRÁFICAS DO ÍNDICE DE PRECIPITAÇÃO PADRONIZADA (SPI) \
                        E DA PRECIPITAÇÃO DO CEARÁ NO PERÍODO DE 2001 A 2020'
                    ]
                ),

                html.H6(
                    children=
                        [
                            'O objetivo do SPI é associar um valor numérico único à variável precipitação, que possa ser comparado entre regiões \
                            e períodos do ano de climas bastante diferenciados. Tecnicamente, o SPI corresponde ao número de desvios padrão de que a \
                            precipitação cumulativa observada se afasta da média climatológica, para uma variável aleatória com distribuição normal. \
                            Como a precipitação não segue uma distribuição normal, aplica-se inicialmente uma transformação tal que os valores transformados \
                            têm distribuição gaussiana. Para isso, é necessário que se disponha de séries de dados suficientemente longas (30 ou mais anos). \
                            O SPI é calculado para diferentes escalas de tempo, significando o período durante o qual se acumula o valor de precipitação: o SPI1 \
                            corresponde à precipitação mensal, o SPI3 corresponde à precipitação acumulada em períodos de 3 meses etc. \
                            É usual utilizar-se uma associação entre faixas de valores do SPI e categorias qualitativas de clima. A interface deste produto é \
                            análoga à do Desvio de Chuva Mensal'
                    ],
                ),

                html.H6(
                    children=
                    [
                        'fonte: https://clima.inmet.gov.br/'
                    ]
                )
            ]
        ),

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