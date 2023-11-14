# STATS 507 HW9 -- Dash Board

Repo: <https://github.com/PKUniiiiice/Dash_GCP_HW9>

Url: <https://project-4-stats-507.uc.r.appspot.com>

## Overview

This repository contains code for visualizations of U.S. Chronic Disease Indicators and predictive modeling. The project is organized into two main modules: `visual` and `predict`. The `visual` module handles plotting and related code, while the `predict` module is responsible for prediction tasks.

### `visual` Module

All plotting functionalities and associated code can be found in the `visual` module. This includes scripts for generating various visualizations to aid in data exploration and understanding.

### `predict` Module

The `predict` module is dedicated to predictive modeling, and it employs two distinct models: Support Vector Regression and Random Forest Regression.

#### Model Evaluation

We conducted an evaluation of both models, and here are our findings:

1. **Support Vector Regression:**
   - Achieved a lower training error (MSE).
   - However, prone to overfitting, particularly when extrapolating far from the training set.

2. **Random Forest Regression:**
   - Demonstrated stability across a wide range of input values.
   - Showed less variability and tended to produce similar or identical values compared to the training set.

#### Challenges and Potential Improvements

We believe the core reason for the observed performance issues lies in the one-hot encoding of categorical variables, particularly for location abbreviations. The feature matrix becomes excessively sparse, and given the relatively small sample size (~3000), it may be contributing to the model's suboptimal performance.

**Future Considerations:**
- Exploring embedding methods for categorical variables, especially for location abbreviations, to potentially improve model performance.
- Investigating alternative feature engineering techniques to address the sparsity issue.
