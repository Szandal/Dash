import Data as DB
import numpy as np
import setup
import plotly.graph_objects as go

Content = DB.html.Div([
    DB.dbc.Card(
        DB.dbc.CardBody([
            DB.html.H2("Informacje ogólne"),
            DB.html.P("Ten pulpit nawigacyjny pokazuje najświeższe informacje o postępie COVID-19. "
                      "Najnowsze dane dotyczące wirusa COVID-19 są regularnie pobierane i wyświetlane na mapie,"
                      " tabelach podsumowujących, najważniejszych danych i wykresach. "),
            DB.html.H2("Dane"),
            DB.html.P("Dane pochodzą z repozytorium Johns Hopkins whiting school of engineering, które jest na bierząco aktualizowane"),
            DB.html.A('Johns Hopkins CSSE',href='https://github.com/CSSEGISandData/COVID-19'),
            DB.html.H2("Autorzy"),
            DB.html.P("Jarosław Galus, Łukasz Żak"),
            DB.html.A('GitHub',href='https://github.com/luki356/SIwB'),

        ]),
        className="m-3",
    ),
]
)
