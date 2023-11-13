from visual import layout_q1, layout_q2, layout_q3, layout_q4, layout_q5
from dash import html


def create_layout_all(data_ext_q1, data_ext_q2, data_ext_q3, data_ext_q4, data_ext_q5):
    layout = html.Div([

        html.Div('HW9 Dash Board', style={'font-weight': 'bold', 'font-size': '50px',
                                       'text-align': 'center', 
                                       'marginBottom': '30px'}),
        layout_q1.create_Div(data_ext_q1),
        layout_q2.create_Div(data_ext_q2),
        layout_q3.create_Div(data_ext_q3),
        layout_q4.create_Div(data_ext_q4),
        layout_q5.create_Div(data_ext_q5),
    ])

    return layout
