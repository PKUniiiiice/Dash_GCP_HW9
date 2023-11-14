#from .data.preprocess import data4q5_4train

import pandas as pd
import optuna
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from joblib import dump

# read data
us_dise_ind = pd.read_csv('../data/us_chronic_disease_indicators.csv')

def data4q5_4train():
    us_dise_ind5 = us_dise_ind[(us_dise_ind["question"] == 'Mortality from heart failure') &
                (us_dise_ind["datavaluetypeid"] == 'NMBR')]

    us_dise_ind5 = us_dise_ind5[['datavalue','stratificationcategory1', 'stratification1',
                         'locationabbr','yearstart']]

    us_dise_ind5[['gender', 'race']] = us_dise_ind5[['stratificationcategory1', 'stratification1']].pivot(columns='stratificationcategory1', values='stratification1').drop('Overall', axis=1)

    us_dise_ind5.drop(labels=['stratificationcategory1', 'stratification1'], axis=1 ,inplace=True)

    return us_dise_ind5.fillna(value='Unknown').reset_index(drop=True)

training_set = data4q5_4train()

training_set = training_set.dropna(subset=['datavalue'])

# Define features and target variable
X = training_set[['locationabbr', 'yearstart', 'gender', 'race']]
y = training_set['datavalue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

categorical_features = ['locationabbr', 'gender', 'race']
numerical_features = ['yearstart']
target = ['datavalue']

# Create transformers for categorical and numerical features
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore')),
])

numerical_transformer = Pipeline(steps=[
    ('norm', StandardScaler()),
])

# Combine transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features),
    ])

print(preprocessor.fit_transform(X_train).shape)


# Define the objective function for Optuna
def objective(trial):
    # why we choose the max_depth as 20?
    # After one-hot encoding, the feature dimension will become 62, according to this value, we choose 20 as the limit
    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('regressor', RandomForestRegressor(
                                n_estimators=trial.suggest_int('n_estimators', 10,200),
                                max_depth=trial.suggest_int('max_depth', 2, 20),)
                                )
                            ])
                   
    # Use cross-validation for evaluation
    kf = KFold(n_splits=5, shuffle=True, random_state=24)
    mse = -cross_val_score(model, X_train, y_train, cv=kf, scoring='neg_mean_squared_error').mean()

    return mse

# Run Optuna optimization
sampler = optuna.samplers.TPESampler(seed=10)  # Make the sampler behave in a deterministic way.
study = optuna.create_study(direction='minimize', sampler=sampler)
study.optimize(objective, n_trials=100)

# Print the best mean cross-validated score and corresponding hyperparameters
best_score = study.best_value
best_params = study.best_params
print(f'Best Mean Cross-validated MSE: {best_score}')
print(f'Best Hyperparameters: {best_params}')


# Access the best model from the Optuna study
best_model = Pipeline(steps=[('preprocessor', preprocessor),
                             ('regressor', RandomForestRegressor(
                                n_estimators=best_params['n_estimators'],
                                max_depth=best_params['max_depth'],)
                                )            
                            ])
# Train the best model on the full training set
best_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error on Test Set1: {mse}')

#save best model
dump(best_model, 'best_model.joblib')