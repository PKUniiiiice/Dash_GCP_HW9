from dash import html, dcc

def create_Div(ext_data):
    options = ext_data

    Div_q3 = html.Div(
    [
        #Dropdown box 
        html.Div('Question 3', style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Div(
            [
                html.Div("Choose Question: ",  style={'font-weight': 'bold', 'font-size': '23px'}),
                dcc.Dropdown(
                    options=options,
                    value=options[0],
                    id='q3-question-dropdown-box',
                    optionHeight=50,
                    style={'marginBottom': '10px'}
                ),
                dcc.RadioItems(
                    options=['Overall', 'Gender', 'Race/Ethnicity'],
                    value='Overall',
                    id='q3-yaxis-line-displayed',
                    labelStyle={'fontSize': '18px'}
                ),
                html.Div(
                    dcc.Graph(id='q3-year-vs-crude-rate-line',
                            responsive=True,
                        style={
                            "width": "100%",
                            "height": "100%"
                        }),
                    style={'width': '100%', "height": '100%', 'marginTop': '0px'}
                ), 
                html.P([
                    html.Strong('Note:', style={'font-weight': 'bold', 'font-size': '18px'}),
                " Some figures may appear identical, as certain diseases only occur in specific groups of people (e.g., cervical cancer)."
                ], style={'marginTop': '0px'}),
            ],
            style={
                "width": "60%",
                "height": '80%',
                "margin": 'auto'}
        ),
    ],
    style={"height": '800px'})

    return Div_q3
