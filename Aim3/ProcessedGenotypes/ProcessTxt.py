#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:46:37 2020

@author: ryanwang
"""

totalFiles = ['BreastCancer_Co-association_score.txt',
              'ChronicKidneyDisease_Co-association_score.txt',
              'ChronicObstructivePulmonaryDisease_Co-association_score.txt',
              'CoronaryArteryDisease_Co-association_score.txt',
              'LungCancer_Co-association_score.txt',
              'Obesity_Co-association_score.txt',
              'Type2Diabetes_Co-association_score.txt']

def run():
#    out1 = open("CombinedHap.txt", "w")
    in1 = open("Data/hu8A5FBF.txt", "r")
    tempLine = in1.readline().strip().split("\t")
 #   tempLine = repr(in1.readline())
    while(tempLine[0] != "# rsid"):
#    for i in range(15):
#        print(tempLine)
        tempLine = in1.readline().strip().split("\t")
 #       tempLine = repr(in1.readline())
    print(tempLine)
#    out1.close()

run()