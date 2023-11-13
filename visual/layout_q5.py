from dash import html, dcc

def create_Div(ext_data):
    
    locabbr, race, gender = ext_data
    locabbr = sorted(locabbr)
    race = sorted(race)
    del race[-2]
    race = ['Unknown']+race

    Div_q5 = html.Div(
    [
         # Dropdown box and line select button
        html.Div('Question 5', style={'font-size': '30px', 'font-weight': 'bold'}),
        html.Div(
                [
                    html.Div('Prediction: Future Counts of `Mortality from heart failure` Disease',
                               style={'font-weight': 'bold', 'font-size': '30px',
                                       'text-align': 'center', 'marginTop': '10px',
                                       'marginBottom': '20px'}),
                    html.Div([
                            dcc.Input(
                                id='input-future-year',
                                type='text',
                                placeholder='Enter Future Year (YYYY)',
                                style={'width': '100%', 'margin': 'auto', 'height': '30px', 'font-size': '18px',}
                            ),
                        ], style={'width': '80%', 'display': 'flex', 'margin': 'auto',
                                   'font-size': '25px'}),

                # Second line with input text windows
                    html.Div([

                        dcc.Dropdown(id='input-locationabbr',
                                     options=locabbr,
                                     placeholder='Select option for Location (State)',
                                     style={'marginTop': '5px','marginBottom': '5px', 'flex': 1}),
                        dcc.Dropdown(id='input-race',
                                     options=race,
                                     placeholder='Select option for Race/Ethnicity',
                                     style={'marginTop': '5px','marginBottom': '5px', 'flex': 1}),
                        dcc.Dropdown(id='input-gender',
                                     options=gender,
                                     placeholder='Select option for Gender',
                                     style={'marginTop': '5px','marginBottom': '5px', 'flex': 1}),
                        ], style={'width': '80%', 'display': 'flex', 'margin': 'auto'}),

                    # Third click button
                    html.Div([
                        html.Button('Submit', id='submit-button', style={'width': '150px', 'height': '90px',
                                                                          'margin': 'auto',
                                                                          'font-weight': 'bold', 'font-size': '25px',
                                                                          'borderRadius': '15px'}), 
                    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center',
                               'marginTop': '15px', 'marginBottom': '10px'}),

                    # 4th line, output
                    html.Div([
                        html.Div('Result',
                               style={'font-weight': 'bold', 'font-size': '30px',
                                       'text-align': 'center', 'marginTop': '10px',
                                       'marginBottom': '5px', 'width': '100%'}),
                        dcc.Textarea(id='output-prediction', value='', readOnly=True,
                                     style={'width': '100%', 'margin': 'auto',
                                             'font-size': '25px', 'font-weight': 'bold', 'borderRadius': '15px',
                                             'marginTop': '5px', 'height': '200px', 'textAlign': 'center',
                                             'lineHeight': '200px',}) 
                    ],style={'width': '50%', 'margin': 'auto', 'align-items': 'center'}),

            ],
            style={
                "width": "70%",
                "height": '80%',
                "margin": 'auto',}
        ),


        dcc.ConfirmDialog(
            id='popup',
            message='Invalid input. Please ensure all input fields are completed, and check the format for the year (e.g., Year: YYYY).',
            displayed=False,
    )

    ],
    style={"height": '600px'},
    )

    return Div_q5


   