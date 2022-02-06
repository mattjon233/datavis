import dash_html_components as html
from styles import MAIN_STYLE
import base64

body = html.Div(
    children=[
        html.P(),

        html.Div(id='initial-page', className='col-lg-10',
            children=[
                html.Br(),
                
                html.Img(src='data:image/png;base64,{}'.format(base64.b64encode(open('./assets/ufc-logo.png', 'rb').read()).decode()), 
                         height=100),

                html.Br(),
                html.Br(),

                html.H4(
                    children=[
                        'ANÁLISES GRÁFICAS DO ÍNDICE DE PRECIPITAÇÃO PADRONIZADA (SPI) \
                        E DA PRECIPITAÇÃO DO CEARÁ NO PERÍODO DE 2001 A 2020'
                    ]
                ),

                html.H6(
                    children=
                        [
                            'O tema abordado foi o da análise de dados meteorológicos no Ceará no período de 2001 a 2020. Utilizando primariamente as medidas de precipitação \
                            e SPI (Índice de Precipitação Padronizada, um valor numérico associado a precipitação calculado de forma que possa ser comparado para regiões de \
                            climas diferentes), além de dados auxiliares, o objetivo era criar visualizações que permitissem uma análise mais clara desses dados ao longo do \
                            período em questão não só de uma forma geral mas também em períodos específicos e com visões espaciais, além de observá-los junto de indicadores sociais.'
                    ],
                ),

                html.Br(),

                html.H5(children=
                    [
                        "Definição de SPI"
                    ],
                    style={'font-weight':'bold'}
                ),

                html.H6(
                    children=
                        [
                            '"O objetivo do SPI é associar um valor numérico único à variável precipitação, que possa ser comparado entre regiões \
                            e períodos do ano de climas bastante diferenciados. Tecnicamente, o SPI corresponde ao número de desvios padrão de que a \
                            precipitação cumulativa observada se afasta da média climatológica, para uma variável aleatória com distribuição normal. \
                            Como a precipitação não segue uma distribuição normal, aplica-se inicialmente uma transformação tal que os valores transformados \
                            têm distribuição gaussiana. Para isso, é necessário que se disponha de séries de dados suficientemente longas (30 ou mais anos). \
                            O SPI é calculado para diferentes escalas de tempo, significando o período durante o qual se acumula o valor de precipitação: o SPI1 \
                            corresponde à precipitação mensal, o SPI3 corresponde à precipitação acumulada em períodos de 3 meses etc. \
                            É usual utilizar-se uma associação entre faixas de valores do SPI e categorias qualitativas de clima. A interface deste produto é \
                            análoga à do Desvio de Chuva Mensal"'
                    ],
                    style={'font-family': 'Helvetica Neue', 'text-align':'left'}
                ),

                html.A(
                    children=
                    [
                        'Fonte: INMET'
                    ],
                    style={'font-family': 'Helvetica Neue'},
                    href='https://clima.inmet.gov.br'
                )
            ],
            style={'padding-left':'100px'}
        ),

        html.Iframe(id='precip-map',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+selectprecip%2Cviewof+selectcolorprecip%2CprecipMapGeoJson',
                    style={'display':'none'}),

        html.Iframe(id='precip-lines',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+dashboard2',
                    style={'display':'none'}),

        html.Iframe(id='idh',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=precip',
                    style={'display':'none'}),

        html.Iframe(id='municipios',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=precipBar',
                    style={'display':'none'}),

        html.Iframe(id='spi-lines',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+dashboard',
                    style={'display':'none'}),

        html.Iframe(id='spi-map',
                    src='https://observablehq.com/embed/@mattjon233/projeto-final-datavis?cells=viewof+selectspi%2Cviewof+selectcolorspi%2CspiMapGeoJson',
                    style={'display':'none'})

    ],
    style = MAIN_STYLE
)