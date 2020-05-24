import Data as DB
import plotly.express as px
import folium
import dash_table
import plotly.express as plot
import Icons
import base64
###############################


Confirmed_Cases = int(DB.Global_Countrys['confirmed'].sum())
Deaths_Count = int(DB.Global_Countrys['deaths'].sum())
Recovered_Count = int(DB.Global_Countrys['recovered'].sum())
Active_Count = int(DB.Global_Countrys['active'].sum())
Affected_Countries = len(DB.Global_Countrys)

sorted_countrys = DB.Global_Countrys[["country","confirmed","deaths","recovered"]].sort_values('confirmed',ascending=False).head(10)


DeathsDifference = (int((DB.Global_D.iloc[:, -1]).sum()) - int((DB.Global_D.iloc[:, -2]).sum()))
RecoveredDifference = (int((DB.Global_R.iloc[:, -1]).sum()) - int((DB.Global_R.iloc[:, -2]).sum()))
ConfirmedDifference = (int((DB.Global_C.iloc[:, -1]).sum()) - int((DB.Global_C.iloc[:, -2]).sum()))

ConfirmedPercent = (ConfirmedDifference/Confirmed_Cases)*100
DeathsPercent = (DeathsDifference/Deaths_Count)*100
RecoveredPercent = (RecoveredDifference/Recovered_Count)*100
###############################
death = 'Icons/devil.png'
deathBase64 = base64.b64encode(open(death, 'rb').read()).decode('ascii')

flag = 'Icons/flag.png'
flagBase64 = base64.b64encode(open(flag, 'rb').read()).decode('ascii')

heart = 'Icons/heart.png'
heartBase64 = base64.b64encode(open(heart, 'rb').read()).decode('ascii')

medicalP = 'Icons/medical-prescription.png'
medicalPBase64 = base64.b64encode(open(medicalP, 'rb').read()).decode('ascii')

jesus = 'Icons/1.png'
jesusPBase64 = base64.b64encode(open(jesus, 'rb').read()).decode('ascii')

########################
CardsTop = DB.dbc.CardDeck(
    [


        DB.dbc.Card(
            DB.dbc.CardBody([
                DB.html.H2('{:,}'.format(Confirmed_Cases).replace(',', ' '), className="card-text"),
                DB.html.P([
                    "(+",
                    '{:.2f}'.format(ConfirmedPercent),
                    "%)"],style={'color': '#fff300'}),
                DB.html.P("Przypadki"),
                DB.html.Div(DB.html.Img(src='data:image/png;base64,{}'.format(medicalPBase64),width=100,height=100,
                                        style={'position':'absolute','top':'auto','bottom': 5,'right':5}),className='icon-large')
            ]),
            className="m-2", style={'color': '#0c5460','background-color': '#d1ecf1','border-color': '#bee5eb;'  }
        ),
        DB.dbc.Card(
            DB.dbc.CardBody([
                DB.html.H2('{:,}'.format(Deaths_Count).replace(',', ' '), className="card-text"),
                DB.html.P(["(+",'{:.2f}'.format(DeathsPercent), "%)"],style={'color': '#ff0400'}),
                DB.html.P("Zgony"),
                DB.html.Div(DB.html.Img(src='data:image/png;base64,{}'.format(deathBase64),width=100,height=100,
                                        style={'position':'absolute','top':'auto','bottom': 5,'right':5}),className='icon-large')
            ]),
            className="m-2", style={'color': '#0c5460','background-color': '#d1ecf1','border-color': '#bee5eb;'  }
        ),
        DB.dbc.Card(
            DB.dbc.CardBody([
                DB.html.H2('{:,}'.format(Recovered_Count).replace(',', ' '), className="card-text"),
                DB.html.P(["(+", '{:.2f}'.format(RecoveredPercent), "%)"], style={'color': '#73ff00'}),
                DB.html.P("Uzdrowienia"),
                DB.html.Div(DB.html.Img(src='data:image/png;base64,{}'.format(heartBase64),width=100,height=100,
                                        style={'position':'absolute','top':'auto','bottom': 5,'right':5}),className='icon-large')
            ]),
            className="m-2", style={'color': '#0c5460','background-color': '#d1ecf1','border-color': '#bee5eb;'  }
        ),
        DB.dbc.Card(
            DB.dbc.CardBody([
                DB.html.H2([Affected_Countries, "/195"], className="card-text"),
                DB.html.P("Dotknięte kraje"),
                DB.html.Div(DB.html.Img(src='data:image/png;base64,{}'.format(flagBase64),width=100,height=100,
                                        style={'position':'absolute','top':'auto','bottom': 5,'right':5}),className='icon-large')
            ]),
            className="m-2", style={'color': '#0c5460','background-color': '#d1ecf1','border-color': '#bee5eb;'  }
        ),
    ],className='m-2'
)



df = px.data.gapminder()
fig1 = px.scatter_geo(df, locations="iso_alpha", color="continent",
                      hover_name="country", size="pop",
                      animation_frame="year",
                      projection="natural earth")

World_Map = folium.Map(location=[11,0], tiles="cartodbpositron" , zoom_start=2, max_zoom = 10, min_zoom = 2)
for i in range(len(DB.Global_D)):
    folium.Circle(
        location=[DB.Global_D.iloc[i]['lat'],DB.Global_D.iloc[i]['long']],
        fill = True,
        radius = (int((DB.np.log(DB.Global_D.iloc[i,-1]+1.00001)))+0.2)*50000,
        fill_color = 'red',
        color = 'pink',
        tooltip = "<div style='margin: 0; background-color: black; color: white;'>"+
                  "<h4 style='text-align:center;font-weight: bold'>"+DB.Global_C.iloc[i]['country'] + "</h4>"
                                                                                                      "<hr style='margin:10px;color: Blue;'>"+
                  "<ul style='color: white;;list-style-type:circle;align-item:left;padding-left:20px;padding-right:20px'>"+
                  "<li style='color: Yellow;'>Zarazeni: "+str(DB.Global_C.iloc[i,-1])+"</li>"+
                  "<li style='color: Red;'>Zgony:   "+str(DB.Global_D.iloc[i,-1])+"</li>"+
                  "<li style='color: Pink;' >Umieralnosc: "+ str(DB.np.round(DB.Global_D.iloc[i,-1]/(DB.Global_C.iloc[i,-1]+1.00001)*100,2))+ "</li>"+
                  "</ul></div>",
    ).add_to(World_Map)

World_Map.save("CovMap.html")

CardsMid = DB.dbc.CardDeck(
    DB.dbc.Row([
        DB.dbc.Card(
            DB.dbc.CardBody(
                [
                    DB.html.Iframe(srcDoc=open("CovMap.html","r").read(), width="100%", height="100%")

                ]
            ),
            className="col-md-8"
        ),
        DB.dbc.Card(
            DB.dbc.CardBody(
                [
                    DB.dbc.Row( DB.dbc.Alert("10 Najbardziej dotknietych państw", className='w-100'),className='w-130'),
                    dash_table.DataTable(
                        columns=[{'name': i, 'id': i} for i in sorted_countrys],
                        data=sorted_countrys.to_dict('records'),
                        )
                ]
            ),
            className="col-md-4",
        )
    ],
        className="w-100 m-2"
    )
)
###############################
fig = plot.scatter(sorted_countrys.head(10), x='country', y='confirmed',size='confirmed', color='country',
                   hover_name='country', size_max=60)
fig.update_layout(width = 1000)
fig.update_layout(
    title="",
    xaxis_title="Kraje",
    yaxis_title="Zakazenia"
)
#############################
fig2 =  px.bar(
    sorted_countrys.head(10),
    x = "country",
    y = "confirmed",
    color_discrete_sequence=["pink"],
    )
#############################
CardsBot = DB.dbc.CardDeck(
    DB.dbc.Row([
        DB.dbc.Card(
            DB.dbc.CardBody(
                [
                    DB.dcc.Loading(children=DB.html.Div(
                        children=DB.dcc.Graph(
                            figure=fig)
                    )
                    )
                ]
            ),
            className="col-md-6"
        ),
        DB.dbc.Card(
            DB.dbc.CardBody(
                [
                    DB.dcc.Loading(children=DB.html.Div(
                        children=DB.dcc.Graph(
                            figure=fig2)
                    )
                    )
                ]
            ),
            className="col-md-6",
        )
    ],
        className="w-100 m-2"
    )
)
Content = DB.html.Div([
    CardsTop,
    CardsMid,
    CardsBot
]
)