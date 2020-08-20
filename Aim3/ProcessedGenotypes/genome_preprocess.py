#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:29:57 2020

@author: guanhuali
"""

#这个是对data进行preprocess的，给每个genome input 一个 label
#genome文件是你process过的原始genome文件
#origin我上传在github/aim3/processedgenome里面了，是对应id的phenotype，需要他来给model input
#最后model 出来的结果会写回genome 文件里面，你得重新organize一下


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import sklearn.metrics as sm
import csv
import matplotlib.pyplot as plt
import save

features = pd.read_excel('genome_1.xlsm')

lists = []

for temp in features['Participant']:
    lists.append(temp)
    
j = 0
origin = pd.read_excel('origin.xlsm')
phenotype_list = []
test_list = []
for temp in origin['Participant']:
    if temp in lists:
        tempo = []
        tempo2 = []
        for feature in origin:
            tempo.append(origin[feature][j])
            if (feature == 'Participant') or (feature == 'Tested'):
                continue
            else:
                tempo2.append(origin[feature][j])
            
        test_list.append(tempo2)
        phenotype_list.append(tempo)
    
    j += 1
feature = []
for temp in origin:
    feature.append(temp)
with open('gp.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(feature)
    for i in phenotype_list:
        writer.writerow(i)

result = save.classify(test_list)

with open('genome_1.csv', 'a') as file:
    writer = csv.writer(file)
    for i in result:
        writer.writerow([i])



