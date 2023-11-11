import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output, callback
import plotly.graph_objects as go

def Plot_Q1(app, ext_data:pd.DataFrame):

    us_dise_ind1 = ext_data

    @app.callback(
        Output('q1-question-vs-y-line-scatter', 'figure'),
        Input('q1-question-dropdown-box', 'value'),
        )
    def update_graph(plot_question):
        nonlocal  us_dise_ind1
        
        fig = go.Figure()
        colors = px.colors.qualitative.Plotly


        for gender in ['Male', 'Female']:
            gender_data = us_dise_ind1.loc[(us_dise_ind1['question'] == plot_question) &
                                           (us_dise_ind1['stratification1'] == gender),
                                           ["yearstart", "datavalue"]].sort_values(
                                               by="yearstart", ascending=True
                                           )

            fig.add_trace(go.Scatter(
                x=gender_data['yearstart'],
                y=gender_data['datavalue'],
                name=gender,
                mode='lines+markers',
                line=dict(color=colors[['Male', 'Female'].index(gender)])  
            ))

        fig.update_layout(
            title="Crude Prevalence Over Time",
            title_x=0.5,
            xaxis_title="Year",
            yaxis_title="Crude Prevalence (percent)",
            showlegend=True,
            width=500,
            height=400,
            title_font=dict(size=24),
            xaxis_title_font=dict(size=18),
            yaxis_title_font=dict(size=18),
            legend_font=dict(size=16),
        )

        fig.update_xaxes(dtick=1, tickfont=dict(size=14))  
        fig.update_yaxes(nticks=12, tickfont=dict(size=14))
        return fig















# Question 2


# Question 3

# Question 4


