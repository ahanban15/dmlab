# -*- coding: utf-8 -*-
"""Lab9_DataMining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kfG5thX34mYusQzMHq8eG4LpQMf55ld4
"""

# Types of Boosting
# Gradient Boosting
# XG Boosting
# ADA Boosting
# Cat Boosting

import pandas as pd

df = pd.read_csv("/content/For_modeling.csv")
df

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['agg.path.chunksize'] = 1024
from xgboost import XGBRegressor
from catboost import CatBoostRegressor, Pool
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

df.drop("Unnamed: 0", axis = 1, inplace=True)
df

df.isna().sum()

x, y = df.drop("Duration", axis = 1), df.Duration

fig, axes = plt.subplots(nrows = 1, ncols = 1,figsize = (15, 15), dpi=80)
sns.heatmap(x.corr(), annot  = True, fmt = ".2f")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

df = df.dropna(axis=1)
x_train = x_train.fillna(x_train.mean())
x_test = x_test.fillna(x_train.mean())

"""**GRADIENT BOOSTING**"""

GBR = GradientBoostingRegressor(n_estimators = 50, learning_rate = 0.1, max_depth = 8, subsample = 0.8)

GBR.fit(x_train, y_train)
gbr_pred = GBR.predict(x_test)
mse_gbr = mean_squared_error(y_test, gbr_pred)
print("Mean squared error of Gradient Boost: ",mse_gbr)

"""**XG Boosting**"""

XGB = XGBRegressor(n_estimators = 50, learning_rate = 0.1, max_depth = 8, subsample = 0.8)

XGB.fit(x_train, y_train)
xgb_pred = XGB.predict(x_test)
mse_xgb = mean_squared_error(y_test, xgb_pred)
print("Mean squared error of Xtreme Gradient Boost: ",mse_xgb)

"""**ADA Boosting**"""

ada_boost = AdaBoostClassifier(n_estimators=50, learning_rate=0.1, random_state=23)

ada_boost.fit(x_train, y_train)
ada_pred = ada_boost.predict(x_test)
mse_ada = mean_squared_error(y_test, ada_pred)
print("Mean squared error of AdaBoostRegressor:", mse_ada)

"""**Cat Boosting**"""

# Convert categorical features to strings
cat_features = ['Pmonth', 'Pday', 'Phour', 'PDweek', 'Dmonth', 'Dday', 'Dhour', 'DDweek']
x_train[cat_features] = x_train[cat_features].astype(str)
x_test[cat_features] = x_test[cat_features].astype(str)

CatB = CatBoostRegressor(n_estimators = 50, learning_rate = 0.1, max_depth = 8, subsample = 0.8)

p_train = Pool(x_train, y_train, cat_features)
p_test = Pool(x_test, y_test, cat_features)
CatB.fit(p_train)
catb_pred = CatB.predict(p_test)
mse_cat1 = mean_squared_error(y_test, catb_pred)
print("Mean squared error of Cat Boost with pool: ",mse_cat1)