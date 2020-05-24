import Data as DB
import plotly.express as plot
import plotly.graph_objects as go
import setup
sorted_country = DB.Global_Countrys.sort_values('confirmed',ascending=False).head(15)


def plot_cases_for_country(country):
    labels = ['comfirmed','deaths']
    colors = ['yellow','red']
    mode_size = [6,8]
    line_size= [4,5]

    list_of_comfirmed_death = [DB.Global_C,DB.Global_D,]

    figu = go.Figure()
    for i, df in enumerate(list_of_comfirmed_death):
        if country == 'World' or country == 'world':
            x_data = DB.np.array(list(df.iloc[:,5:].columns))
            y_data = DB.np.sum(DB.np.asarray(df.iloc[:,5:]),axis=0,)
            
        else:
            x_data = DB.np.array(list(df.iloc[:,5:].columns))
            y_data = DB.np.sum(DB.np.asarray(df[df['country']==country].iloc[:,5:]),axis=0)
            
        figu.add_trace(go.Scatter(x=x_data,y=y_data,
                                  mode="lines+markers", 
                                  name=labels[i], 
                                  line=dict(color=colors[i],width=line_size[i]),
                                  connectgaps=True,
                                  text = "Total " + str(labels[i]) + ": " + str(y_data[-1]),
                                  ))
    return figu
   #####################################
def plot_cases_CR(country):
    labels = ['comfirmed','recovery']
    colors = ['yellow','green']
    mode_size = [6,8]
    line_size= [4,5]

    list_of_comfirmed_death = [DB.Global_C,DB.Global_R]

    figu = go.Figure()
    for i, df in enumerate(list_of_comfirmed_death):
        if country == 'World' or country == 'world':
            x_data = DB.np.array(list(df.iloc[:,5:].columns))
            y_data = DB.np.sum(DB.np.asarray(df.iloc[:,5:]),axis=0,)
            
        else:
            x_data = DB.np.array(list(df.iloc[:,5:].columns))
            y_data = DB.np.sum(DB.np.asarray(df[df['country']==country].iloc[:,5:]),axis=0)
            
        figu.add_trace(go.Scatter(x=x_data,y=y_data,
                                  mode="lines+markers", 
                                  name=labels[i], 
                                  line=dict(color=colors[i],width=line_size[i]),
                                  connectgaps=True,
                                  text = "Total " + str(labels[i]) + ": " + str(y_data[-1]),
                                  ))
    return figu

################################################

def plot_of_mortality(country):
    labels = ['mortality']
    colors = ['pink']
    mode_size = [6,8]
    line_size= [4,5]

    list_of_comfirmed_death = [DB.Global_C,DB.Global_D]
    sum_of_death = DB.Global_D.iloc[:,5:].sum()
    sum_of_confirmed = DB.Global_C.iloc[:,5:].sum()
    mortality_for_world= sum_of_death/sum_of_confirmed*100
    figu = go.Figure()

    #for i, df in enumerate(list_of_comfirmed_death):
    if country == 'World' or country == 'world':
        x_data = DB.np.array(list(DB.Global_C.iloc[:,5:].columns))
        y_data = DB.np.asarray(mortality_for_world)
            
    else:
        x_data = DB.np.array(list(DB.Global_C.iloc[:,5:].columns))
        y_data = DB.np.sum(DB.np.asarray(DB.Global_D[DB.Global_D['country']==country].iloc[:,5:]/DB.Global_C[DB.Global_C['country']==country].iloc[:,5:]*100),axis=0)
            
    figu.add_trace(go.Scatter(x=x_data,y=y_data,
                                mode="lines+markers", 
                                name=labels[0], 
                                line=dict(color=colors[0],width=line_size[0]),
                                connectgaps=True,
                                ))
    return figu
#################################################

def plot_of_recovering(country):
    labels = ['recovering']
    colors = ['lime']
    mode_size = [6,8]
    line_size= [4,5]

    sum_of_recovery = DB.Global_R.iloc[:,5:].sum()
    sum_of_confirmed = DB.Global_C.iloc[:,5:].sum()
    recovering_for_world= sum_of_recovery/sum_of_confirmed*100
    figu = go.Figure()

    #for i, df in enumerate(list_of_comfirmed_death):
    if country == 'World' or country == 'world':
        x_data = DB.np.array(list(DB.Global_C.iloc[:,5:].columns))
        y_data = DB.np.asarray(recovering_for_world)
            
    else:
        x_data = DB.np.array(list(DB.Global_C.iloc[:,5:].columns))
        y_data = DB.np.sum(DB.np.asarray(DB.Global_R[DB.Global_R['country']==country].iloc[:,5:]/DB.Global_C[DB.Global_C['country']==country].iloc[:,5:]*100),axis=0)
            
    figu.add_trace(go.Scatter(x=x_data,y=y_data,
                                mode="lines+markers", 
                                name=labels[0], 
                                line=dict(color=colors[0],width=line_size[0]),
                                connectgaps=True,
                                ))
    return figu

###############################################

list_of_country = ( DB.Global_Countrys['country'])

IHatePython = DB.pd.Series(["World"])

list_of_country=list_of_country.append(IHatePython)

sum_of_death = DB.Global_D.iloc[:,5:].sum()
sum_of_confirmed = DB.Global_C.iloc[:,5:].sum()
mortality_for_world= DB.pd.Series(round(sum_of_death/sum_of_confirmed*100,2))

temp = DB.Global_D.iloc[:,5:].sum()/DB.Global_C.iloc[:,5:].sum()*100

def convert_options():
        return [dict(label=x, value=x) for x in list_of_country]

import dash_table
Content = DB.html.Div(
    [
        DB.dbc.CardDeck(
            DB.dbc.Row([
                DB.dbc.Col([
                    DB.dcc.Dropdown(
                        id='country-dropdown',
                        options=convert_options(),
                        value = 'World'
                    ),
                ],className='col-6'),
                DB.dbc.Col([
                    DB.dbc.RadioItems(
                            options=[
                                {'label': 'Liniowy', 'value': 'lineW'},
                                {'label': 'Logarytmiczny', 'value': 'LogW'},
                            ],
                            value='MTL',
                            inline=True,
                            className='m-2'
                        )
                ],className='col-6'),
            ],className='w-100'),
            className='m-2'
        ),

        DB.dbc.CardDeck(
            DB.dbc.Row([
                DB.dbc.Card(
                    DB.dbc.CardBody(
                        [
                            DB.dcc.Loading(
                                id = "graf-CD",
                            ),
                        ]
                    ),
                    className="col-md-6"
                ),
                DB.dbc.Card(
                    DB.dbc.CardBody(
                        [
                            DB.dcc.Loading(
                                id = "graf-CR",
                            )
                        ]
                    ),
                    className="col-md-6",
                )
            ],
                className="w-100 m-2"
            )),
            DB.dbc.CardDeck(
                DB.dbc.Row([
                    DB.dbc.Card(
                        DB.dbc.CardBody(
                            [
                                DB.dcc.Loading(
                                    id = "graf-mortality",

                                ),
                            ]
                        ),
                        className="col-md-6"
                    ),
                    DB.dbc.Card(
                        DB.dbc.CardBody(
                            [
                                DB.dcc.Loading(
                                    id = "graf-recovering",
                                ),
                            ]
                        ),
                        className="col-md-6",
                    )
                ],
                    className="w-100 m-2"
            )),
    ]
)
