from joblib import load
import pandas as pd

model_forest = load('./predict/best_model.joblib')
model_svr = load('./predict/best_model_exp_v1_23049.joblib')
def y_pred(model_name, future_year, locabbr, race, gender):
    if model_name == 'Random Forest Regression':
        model = model_forest
    else:
        model = model_svr

    newx = pd.DataFrame({'locationabbr': locabbr,
                         'yearstart': future_year,
                         'gender': gender,
                         'race': race}, index=[0])
    
    return model.predict(newx)