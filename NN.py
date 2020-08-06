#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:44:43 2020

@author: guanhuali
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=62)

NN_model = MLPRegressor(solver='lbfgs', activation='relu', hidden_layer_sizes=(42, 1), random_state=1000)
NN_model.fit(x_train, y_train)  
result = NN_model.predict(x_test) 
test = NN_model.predict(x_train)
score = NN_model.score(x_train, y_train)  
MSE = np.sqrt(metrics.mean_squared_error(y_train, test))
plt.figure()
plt.plot(np.arange(len(y_train)), y_train, "bo-", label="True Value")  
plt.plot(np.arange(len(test)), test, "ro-", label="Predict Value")  
plt.title(f"sklearn NN model:testing aim3\nsimilar score:{score}\n testing_size:{len(x_train)}-- MSE:{MSE}")
plt.legend(loc="best")
plt.show()


fig, ax = plt.subplots()
ax.scatter(y_train, test)
ax.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
# plt.scatter(x_train,y_train,c='red')
# plt.show()

# plt.plot(x_train,test)   
# plt.scatter(x_train,test,c='red')
# plt.xlabel('headsize')
# plt.ylabel('brain weight')




