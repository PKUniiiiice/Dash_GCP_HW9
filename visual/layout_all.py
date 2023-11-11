from visual import layout_q1, layout_q2, layout_q3, layout_q4
from dash import html


def create_layout_all(data_ext_q1, data_ext_q2, data_ext_q3, data_ext_q4):
    layout = html.Div([
        layout_q1.create_Div(data_ext_q1),
        layout_q2.create_Div(data_ext_q2),
        layout_q3.create_Div(data_ext_q3),
        layout_q4.create_Div(data_ext_q4),
    ])

    return layout
