import Data as DB
import operator
import dash_table


Global_C = DB.Global_Countrys.rename(columns = {"incident_rate":"incident rate", "mortality_rate":"mortality rate"})


df = Global_C[["country","confirmed","deaths","recovered","active","incident rate","mortality rate"]]



Content = DB.html.Div(
        DB.dbc.CardDeck(
                DB.dbc.CardBody(
                        dash_table.DataTable(
                                id='table',
                                columns=[{'name': col, 'id': col} for col in df.columns],
                                data = df.to_dict('records'),
                                sort_action='native',
                                filter_action='native'
                )

        ),className='m-2'), className='col-12'


)
