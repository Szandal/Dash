
import Data as DB
import TabOne
import TabTwo
import TabThree
import TabFour




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DB.dash.Dash(__name__, external_stylesheets=[DB.dbc.themes.LUX],suppress_callback_exceptions=True)




card = DB.dbc.Card(
    [
        DB.dbc.CardHeader(
            DB.dbc.Row(
                [
                    DB.dbc.Col(DB.html.Div("DashBoard - COVID-19, Wszystko winna kontynentalnego taiwanu (\"chin\")")),
                    DB.dbc.Tabs(
                        [
                            DB.dbc.Tab(label="Ogól", tab_id="tab-1"),
                            DB.dbc.Tab(label="Tabele", tab_id="tab-2"),
                            DB.dbc.Tab(label="Wykresy", tab_id="tab-3"),
                            DB.dbc.Tab(label="Kokpit info.", tab_id="tab-4")
                        ],
                        id="card-tabs",
                        card=True,
                        active_tab="tab-1",
                    )
                ])
        ),
        DB.html.P(id="card-content", className="card-text")
    ]
)


@app.callback(
    DB.Output("card-content", "children"), [DB.Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == "tab-1":
        return TabOne.Content
    elif active_tab == "tab-2":
        return TabTwo.Content
    elif active_tab == "tab-3":
        return TabThree.Content
    elif active_tab == "tab-4":
        return TabFour.Content
    return DB.html.P("404 not found, don't do this to us, pls don't break it more <3")



app.layout = DB.html.Div(children=[
    card
])



@app.callback(
    DB.dash.dependencies.Output('graf-CD','children'),
    [DB.dash.dependencies.Input('country-dropdown', 'value')])
def update_output(value):
    return DB.dcc.Graph(
            figure=TabThree.plot_cases_for_country(value))



@app.callback(
    DB.dash.dependencies.Output('graf-CR','children'),
    [DB.dash.dependencies.Input('country-dropdown', 'value')])
def update_output(value):
    return DB.dcc.Graph(
            figure=TabThree.plot_cases_CR(value))

@app.callback(
    DB.dash.dependencies.Output('graf-mortality','children'),
    [DB.dash.dependencies.Input('country-dropdown', 'value')])
def update_output(value):
    return DB.dcc.Graph(
            figure=TabThree.plot_of_mortality(value))


@app.callback(
    DB.dash.dependencies.Output('graf-recovering','children'),
    [DB.dash.dependencies.Input('country-dropdown', 'value')])
def update_output(value):
    return DB.dcc.Graph(
            figure=TabThree.plot_of_recovering(value))


if __name__ == '__main__':
    app.run_server(debug=True)