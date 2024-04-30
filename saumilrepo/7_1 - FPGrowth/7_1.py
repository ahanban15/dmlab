# -*- coding: utf-8 -*-
"""DataMining_Lab7_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lI3j6Gu0mmFwernMlnbhRhnmYtCe25wA
"""

import pandas as pd
from mlxtend.frequent_patterns import association_rules, fpgrowth

df = pd.read_csv('/content/Market_Basket_Optimisation.csv',sep=',',header=None)
df.fillna("", inplace=True)
df.head()

items = set()
for col in df:
    unique_values = df[col].unique()
    for val in unique_values:
        if val != "":
            items.add(val)

print(items)

itemset = set(items)
encoded_vals = []
for index, row in df.iterrows():
    rowset = set(row)
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_df = pd.DataFrame(encoded_vals)

fp = fpgrowth(ohe_df, min_support=0.02, use_colnames=True)
fp

association_rules(fp,metric="confidence",min_threshold=0.1)