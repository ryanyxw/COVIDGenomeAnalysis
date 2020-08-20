#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:47:43 2020

@author: guanhuali
"""
#model 主文件，preprocess过后你整理下genome xlsm就可以直接run了，假如data变多，你把n_esti 和 randomstate都适当变大一下

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import sklearn.metrics as sm
import csv
import matplotlib.pyplot as plt


features = pd.read_excel('genome_1.xlsm')

y = np.array(features['COVID'])
features = features.drop('COVID',axis=1)
features = features.drop('Hap41',axis =1 )
features = features.drop('Participant',axis=1)
labels = []
for rows in features:
    labels.append(rows)
x = np.array(features)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=100)

RF_model = RandomForestClassifier(n_estimators = 26, random_state = 13)

RF_model.fit(x_train, y_train)
pred_y = RF_model.predict(x_test)

feature_imp = RF_model.feature_importances_
dictions = {}

for num, name in zip(feature_imp,labels):
    dictions[name] = num

new = sorted(dictions.items(),key=lambda x: x[1])
info_list = []
for info in new:
    info_list.append([info[0],info[1]])
    
with open('info.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow([])
    for i in info_list:
        writer.writerow(i)
        
        
        
ac = (y_test == pred_y).sum() / y_test.size
print('accuracy ac=', ac)


m = sm.confusion_matrix(y_test, pred_y)
print('confusion matrix：', m, sep='\n')


r = sm.classification_report(y_test, pred_y)
print('Overall Report：', r, sep='\n')


C2= sm.confusion_matrix(y_test, pred_y, labels=[0, 1])
sns.heatmap(C2,annot=True)
plt.show()