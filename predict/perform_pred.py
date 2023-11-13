from joblib import load
import pandas as pd
model = load('./predict/best_model.joblib')

def y_pred(future_year, locabbr, race, gender):
    global model
    newx = pd.DataFrame({'locationabbr': locabbr,
                         'yearstart': future_year,
                         'gender': gender,
                         'race': race}, index=[0])
    
    return model.predict(newx)