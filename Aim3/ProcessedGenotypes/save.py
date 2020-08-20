#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:32:45 2020

@author: guanhuali
"""
#new_processed我也上传上去了

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import sklearn.metrics as sm
import csv
import matplotlib.pyplot as plt
def classify(test_feature):
    features = pd.read_excel('../../Downloads/new_processed.xlsm')
    
    y = np.array(features['Tested'])
    features = features.drop('Tested',axis=1)

    x = np.array(features)
    
    RF_model = RandomForestClassifier(n_estimators = 248, random_state = 140)

    RF_model.fit(x, y)
    pred_y = RF_model.predict(test_feature)
    return pred_y


