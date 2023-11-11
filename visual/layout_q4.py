from dash import html, dcc

def create_Div(ext_data):
    options = ext_data

    Div_q4 = html.Div(
    [
        #Dropdown box 
        html.Div('Question 4', style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Div(
            [
                html.Div("Choose Race/Ethnicity: ",  style={'font-weight': 'bold', 'font-size': '23px'}),
                dcc.Dropdown(
                    id='q4-race-dropdown',
                    options=list(options)+['Overall'],
                    value='Overall',  # Default value
                    optionHeight=50,
                    style={'marginBottom': '5px'}
                ),
                html.Div("Choose Gender: ",  style={'font-weight': 'bold', 'font-size': '23px'}),
                dcc.Dropdown(
                    id='q4-gender-dropdown',
                    options=['Male', 'Female', 'Overall'],
                    value='Overall',  # Default value
                    optionHeight=50,
                    style={'marginBottom': '5px'}
                ),

                html.Div(
                    dcc.Graph(id='q4-choropleth-map',
                            responsive=True,
                            style={
                                "width": "100%",
                                "height": "100%"
                            }),
                    style={'width': '100%', "height": '100%', 'marginTop': '0px'}
                ), 
            ],
            style={
                "width": "60%",
                "height": '80%',
                "margin": 'auto'}
        ),
    ],
    style={"height": '800px'})

    
    return Div_q4



