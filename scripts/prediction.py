#!/usr/bin/env python3

# Import packages
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("scripts/mtcars.csv")

# Remove non-continuous and outcome variable
xtrain = data.drop(['model', 'vs', 'am', 'carb', 'mpg'], axis=1)
ytrain = data['mpg']

# Predictors
col_imp = ["cyl", "disp", "hp", "drat", "wt", "qsec", "gear"]

# Fit model
mod = LinearRegression().fit(xtrain,ytrain)


def predict(dict_values, col_imp = col_imp):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = mod.predict(x)[0]
    return y_pred
