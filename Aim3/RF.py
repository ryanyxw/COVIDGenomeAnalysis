#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:46:10 2020

@author: guanhuali
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import sklearn.metrics as sm
import matplotlib.pyplot as plt

features = pd.read_csv('../../Downloads/data1.csv')

features= features.drop('Participant', axis = 1)
features = features.drop('ID',axis = 1)
features = features.drop('Date', axis = 1)
labels = np.array(features['label'])
y = []
for x in range(len(labels)):
    if labels[x] == 'Yes':
        y.append(1)
    else:
        y.append(0)
y = np.array(y)

#labels = pd.get_dummies(labels)
#features = pd.get_dummies(features)
features= features.drop('label', axis = 1)
features = np.array(features)

modified = []

for col in features:
    temp = []
    for x in range(len(col)):
        if col[x] == 'Yes':
            temp.append(1)
        elif col[x] == 'No':
            temp.append(0)
        else:
            temp.append(0)
    modified.append(temp)

x = np.array(modified)
#print(x.shape,y.shape)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=62)

RF_model = RandomForestClassifier(n_estimators = 100, random_state = 42)

RF_model.fit(x_train, y_train)
pred_y = RF_model.predict(x)

feature_imp = RF_model.feature_importances_
print(x[0])
print(feature_imp)

ac = (y == pred_y).sum() / y.size
print('accuracy ac=', ac)


m = sm.confusion_matrix(y, pred_y)
print('confusion matrix：', m, sep='\n')


r = sm.classification_report(y, pred_y)
print('Overall Report：', r, sep='\n')


C2= sm.confusion_matrix(y, pred_y, labels=[0, 1])
sns.heatmap(C2,annot=True)
plt.show()