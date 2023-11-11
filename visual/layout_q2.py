from dash import html, dcc

def create_Div(ext_data):
    options = ext_data

    Div_q2 = html.Div(
    [
         # Dropdown box and line select button
        html.Div('Question 2', style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Div(
            [
                html.Div("Choose Year: ", style={'font-size': '23px', 'font-weight': 'bold'}),
                dcc.Dropdown(
                    options=options,
                    value=options[0],
                    id='q2-year-dropdown-box',
                    optionHeight=40
                ),
                html.Div(
                    dcc.Graph(id='q2-year-vs-perct-bar-scatter',
                            responsive=True,
                        style={
                            "width": "100%",
                            "height": "100%"
                        }),
                    style={'width': '100%', "height": '100%'}
                ),            
            ],
            style={
                "width": "70%",
                "height": '80%',
                "margin": 'auto'}
        )
    ],
    style={"height": '600px'})

    return Div_q2


   