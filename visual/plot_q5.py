from dash import Input, Output, State
from predict.perform_pred import y_pred

def Plot_Q5(app):

    @app.callback(
        [Output('output-prediction', 'value'),
         Output('popup', 'displayed')],
        [Input('submit-button', 'n_clicks')],
        [State('input-future-year', 'value'),
         State('input-locationabbr', 'value'),
         State('input-race', 'value'),
         State('input-gender', 'value'),])
    def validate_input_and_update_prediction(n_clicks, future_year, locabbr, race, gender):
        #print(n_clicks)
        if n_clicks is None:
            # No button click yet
            return '', False

        # Check if all input parameters have values
        if all(param is not None and param != '' for param in [future_year, locabbr, race, gender]):
            # Check if future_year is a valid numeric value with a length of 4
            if future_year.isnumeric() and len(future_year) == 4:
                # If valid, update the prediction (this is just a placeholder)
                prediction = round(y_pred(future_year, locabbr, race, gender)[0])  # Replace with your actual prediction logic
                return str(prediction), False
            else:
                # If not valid, display the pop-up window
                return '', True

        else:
            return '' , True



















# Question 2


# Question 3

# Question 4


