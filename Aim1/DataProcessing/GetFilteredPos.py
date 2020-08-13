#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:14:40 2020

@author: ryan04px2021
"""

folderName = "Type2Diabetes"
pIndex = 32
posIndex = 4



in1 = open(folderName + "/FilteredDataFinal.txt", "r")
out1 = open(folderName + "/FilteredPos.txt", "w")

tempLine = in1.readline().strip().split("\t")

while(tempLine != ['']):
#for i in range(totalNum):
    out1.write(tempLine[2] + "\n")
    tempLine = in1.readline().strip().split("\t")

out1.close()
