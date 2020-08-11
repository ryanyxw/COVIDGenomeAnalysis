#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:24:11 2020

@author: guanhuali
"""


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import csv


features = pd.read_excel('../../Downloads/processed2.xlsm')

features = features.drop('Participant', axis = 1)

features = np.array(features)
#print(features['Eczema'])

for rows in features:
    count = 0

    for i in range(-45,-4):
        if rows[i] > 0:
            count += 1
    if (count > 5) and (rows[-3] == 0):
        rows[-3] = 1
    
    if rows[-3] < 0:
        rows[-3] = 0



with open('../../Downloads/new_processed.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([])
    for feature in features:
        writer.writerow(feature)