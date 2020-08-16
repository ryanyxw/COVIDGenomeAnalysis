#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:26:01 2020

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
    out1 = open("CombinedHap.txt", "w")
    for fileName in totalFiles:
        addAnotherFile(fileName, out1)
    out1.close()

def addAnotherFile(fileName, out1):
    
    in1 = open("../../Aim2/Association score/" + fileName)

    tempLine = in1.readline().strip().split("\t")
    print(tempLine)
    tempLine = in1.readline().strip().split("\t")
    while(tempLine != ['']):
    #for i in range(totalNum):
        out1.write(tempLine[0] + "\t" + tempLine[-2] + "\t" + tempLine[-1] + "\n")
        tempLine = in1.readline().strip().split("\t")


#run()

