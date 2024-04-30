# -*- coding: utf-8 -*-
"""DataMining_Lab8_WithPreprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gN--dxF5DPoAiR9GUQgZaiiym4I2Lgbr
"""

import pandas as pd
df = pd.read_csv('/content/diabetes.csv')
df.head()

df['SkinThickness'].replace(0,df['SkinThickness'].mean(), inplace=True)
df['Insulin'].replace(0,df['Insulin'].mean(), inplace=True)
df['BMI'].replace(0,df['BMI'].mean(), inplace=True)
df.head()

from sklearn.model_selection import train_test_split

df1 = df.loc[:, df.columns != "Outcome"]

x_train, x_test,\
    y_train, y_test = train_test_split(df1, df.Outcome ,test_size=0.20,random_state=0)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

clf = LogisticRegression(random_state=0)
clf.fit(x_train, y_train)

# Prediction
y_pred = clf.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print("Logistic Regression model accuracy (in %):", acc*100)

# evaluation matrix
from sklearn import metrics

cm = metrics.ConfusionMatrixDisplay(metrics.confusion_matrix(y_test, y_pred), display_labels = [True, True])
cm.plot()

accuracy = metrics.accuracy_score(y_test, y_pred)*100
precision = metrics.precision_score(y_test, y_pred)*100
recall = metrics.recall_score(y_test, y_pred)*100
F1_score = metrics.f1_score(y_test, y_pred)*100

print("Accuracy : ",accuracy)
print("Precision : ",precision)
print("Recall : ",recall)
print("F1_score : ",F1_score)