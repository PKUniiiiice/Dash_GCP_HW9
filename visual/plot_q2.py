from dash import Input, Output
import plotly.graph_objects as go

# we create the html div object
def Plot_Q2(app, ext_data):

    us_dise_ind2 = ext_data

    @app.callback(
        Output('q2-year-vs-perct-bar-scatter', 'figure'),
        Input('q2-year-dropdown-box', 'value'),
        )
    def update_graph(year):
        # Create a go.Figure instead of px.bar
        nonlocal us_dise_ind2
        
        fig = go.Figure()
        df = us_dise_ind2[us_dise_ind2['yearstart'] == int(year)]
        df = df.sort_values(by='datavalue', ascending=False)

        fig.add_trace(go.Bar(
            x=df['locationabbr'],
            y=df['datavalue'],
            marker=dict(color=df['datavalue'], colorscale='plotly3',
                        reversescale=True,
                        colorbar=dict(title='%')),
            showlegend=False
        ))

        fig.update_layout(
            title=f'Alcohol Use Rate in Youth by State in {int(year)}',
            title_x=0.5,
            xaxis_title='Location',
            yaxis_title='Percentage',
            showlegend=True,
            width=1200,
            height=500,
            title_font=dict(size=24),
            xaxis=dict(tickangle=0),
            xaxis_title_font=dict(size=18),
            yaxis_title_font=dict(size=18),  # Adjust the angle as needed
        )

        return fig















# Question 2


# Question 3

# Question 4


