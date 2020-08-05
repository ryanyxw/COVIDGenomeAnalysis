#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:54:45 2020

@author: ryan04px2021
"""

#Tests how to extract a specific column in a file

testRead = open("../COVID19_HGI_ANA_C2_V2_20200701.txt", "r")
#testWrite = open("outputV2.txt", "w")
testWrite = open("outputV2demo.txt", "w")
currLine = testRead.readline().split("\t")

totalNum = 100
#while(currLine != ['']):
for i in range(totalNum):
    testWrite.write(currLine[4] + "\t" + currLine[62] + "\n")
    currLine = testRead.readline().split("\t")


    
testWrite.close()


