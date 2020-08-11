#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:21:06 2020

@author: guanhuali
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import seaborn as sns
import sklearn.metrics as sm
import matplotlib.pyplot as plt

features = pd.read_excel('../../Downloads/new_processed.xlsm')
features = features.drop('TestedContact',axis=1)
features = features.drop('UntestedContact',axis=1)
y = np.array(features['Tested'])
features = features.drop('Tested',axis=1)

x = np.array(features)
print(x.shape)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.35, random_state=100)

NN_model = MLPClassifier(solver='lbfgs', activation='relu', hidden_layer_sizes=(244, 122), random_state=1000)

NN_model.fit(x_train, y_train)
pred_y = NN_model.predict(x_test)


ac = (y_test == pred_y).sum() / y_test.size
print('accuracy ac=', ac)


m = sm.confusion_matrix(y_test, pred_y)
print('confusion matrix：', m, sep='\n')


r = sm.classification_report(y_test, pred_y)
print('Overall Report：', r, sep='\n')


C2= sm.confusion_matrix(y_test, pred_y, labels=[0, 1])
sns.heatmap(C2,annot=True)
plt.show()