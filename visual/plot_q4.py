from dash import Input, Output
import plotly.graph_objects as go
from data.preprocess import get_geojson

# we create the html div object
def Plot_Q4(app, ext_data):

    us_dise_ind4 = ext_data
    geojson = get_geojson()

    @app.callback(
        Output('q4-choropleth-map', 'figure'),
        Input('q4-race-dropdown', 'value'),
        Input('q4-gender-dropdown', 'value'),
        )
    def update_graph(race, gender):
        # Create a go.Figure instead of px.bar
        nonlocal us_dise_ind4, geojson

        fig = go.Figure()

        if 'Overall' not in [race, gender]:
            fig.add_annotation(
                text="Data For This Category Not Available",
                x=0.5,  # X-coordinate (0.5 is the center)
                y=0.5,  # Y-coordinate (0.5 is the center)
                showarrow=False,  # Hide the arrow
                font=dict(size=20),  
                xref='paper',
                yref='paper'# Set the font size
            )       
        else:
            if race == gender == 'Overall':
                df = us_dise_ind4.loc[
                    us_dise_ind4['stratificationcategoryid1'] == 'OVERALL'
                ]
                fig.add_trace(go.Choroplethmapbox(
                    locations=df['locationabbr'],
                    z=df['datavalue'],
                    geojson=geojson,
                    colorscale='plotly3_r',
                    colorbar_title='Obesity Rate (%)',
                    text=df['locationabbr'],
                    hovertemplate='%{text}<br>Obesity Rate: %{z:.2f}%',
                    marker=dict(opacity=0.7),
                    name="",
                ))

                fig.update_layout(
                    title='Heatmap of Obesity Rate among adults aged >= 18 years in 2021',
                    title_x=0.5,
                    title_font=dict(size=24),
                    mapbox=dict(
                                 center={"lat": 37.0902, "lon": -95.7129},  # Center of the USA
                                 zoom=3,
                                 accesstoken='pk.eyJ1IjoibmVoY214IiwiYSI6ImNsb2J4dDJjYTBrMHAya3BpNzNraHc5cnAifQ.7xTn6wD4ZjgvH4Zo0mG2CA'  # Adjust the initial zoom level
                    )
                )
            else:
                col = ('Gender', gender) if gender != 'Overall' else ('Race', race)
                df = us_dise_ind4.loc[
                    (us_dise_ind4['stratification1'] == col[1] )
                ]
                fig.add_trace(go.Choroplethmapbox(
                    locations=df['locationabbr'],
                    z=df['datavalue'],
                    geojson=geojson,
                    colorscale='plotly3_r',
                    colorbar_title='Obesity Rate (%)',
                    text=df['locationabbr'],
                    hovertemplate='%{text}<br>Obesity Rate: %{z:.2f}%',
                    marker=dict(opacity=0.7),
                    name="",
                ))

                fig.update_layout(
                    title=f'Heatmap of Obesity Rate among adults aged >= 18 years in 2021<br>{col[0]}: {col[1]}',
                    title_x=0.5,
                    title_font=dict(size=24),
                    mapbox=dict(
                                 center={"lat": 37.0902, "lon": -95.7129},  # Center of the USA
                                 zoom=3,
                                 accesstoken='pk.eyJ1IjoibmVoY214IiwiYSI6ImNsb2J4dDJjYTBrMHAya3BpNzNraHc5cnAifQ.7xTn6wD4ZjgvH4Zo0mG2CA'  # Adjust the initial zoom level
                    )
                )

        return fig















# Question 2


# Question 3

# Question 4


