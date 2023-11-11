from dash import Input, Output
import plotly.graph_objects as go

# we create the html div object
def Plot_Q3(app, ext_data):

    us_dise_ind3 = ext_data

    @app.callback(
        Output('q3-year-vs-crude-rate-line', 'figure'),
        Input('q3-question-dropdown-box', 'value'),
        Input('q3-yaxis-line-displayed', 'value'),
        )
    def update_graph(question_title, category):
        # Create a go.Figure instead of px.bar
        nonlocal us_dise_ind3
        
        df = us_dise_ind3.loc[
            (us_dise_ind3['stratificationcategory1'] == category) & 
            (us_dise_ind3['question'] == question_title)
        ]

        pivot_df = df.pivot(index='yearstart', columns='stratification1', values='datavalue')
        
        fig = go.Figure(data=[
            go.Scatter(x=pivot_df.index,
                       y=pivot_df[column],
                       mode='lines+markers', name=column)
                    for column in pivot_df.columns
        ])

        fig.update_layout(
            title=f'{question_title}',
            title_x=0.5,
            xaxis_title='Year',
            yaxis_title='Average Annual Crude Rate',
            showlegend=True,
            title_font=dict(size=24),
            xaxis_title_font=dict(size=18),
            yaxis_title_font=dict(size=18),  
            legend_font=dict(size=16),
        )

        fig.update_xaxes(dtick=1, tickfont=dict(size=14))  
        fig.update_yaxes(nticks=15, tickfont=dict(size=14))

        return fig















# Question 2


# Question 3

# Question 4


