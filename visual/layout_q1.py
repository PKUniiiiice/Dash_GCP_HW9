from dash import html, dcc

def create_Div(ext_data):
    options = ext_data
    Div_q1 = html.Div(
    [
    # Dropdown box and line select button
        html.Div('Question 1', style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Div(
            [
                html.Div("Choose Question:", style={'font-weight': 'bold', 'font-size': '23px'}),
                dcc.Dropdown(
                    options=options,
                    value='Awareness of high blood pressure among adults aged >= 18 years',
                    id='q1-question-dropdown-box',
                    optionHeight=50
                ),
                # dcc.RadioItems(
                #     options=['All', 'Male', 'Female',],
                #     value='All',
                #     id='q1-yaxis-line-displayed',
                #     labelStyle={'display': 'inline-block', 'marginTop': '5px'
                html.Div(
                    dcc.Graph(id='q1-question-vs-y-line-scatter',
                            responsive=True,
                        style={
                            "width": "100%",
                            "height": "100%"
                        }),
                    style={'width': '100%', "height": '100%'}
                ),            
            ],
            style={
                "width": "60%",
                "height": '80%',
                "margin": 'auto'}
        )
    ],
    style={"height": '800px'})

    return Div_q1