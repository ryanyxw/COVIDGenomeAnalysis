#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:32:01 2020

@author: ryanwang
"""
import os
totalFiles = os.listdir("./Data/TSVProcess")

def run():
    count = 1
    for currentFile in totalFiles:
        fileName = currentFile
        addAnotherFile(fileName, count)
        count += 1
    
def addAnotherFile(fileName, count):
    
    in1 = open("Data/TSV/" + fileName, "r")
    out1 = open("Data/TSVProcess/" + fileName, "w")
    out1.write("# rsid\tchromosome\tposition")
    print(fileName)
    tempLine = in1.readline().strip().split("\t")
    while tempLine[0] != ">locus":
        tempLine = in1.readline().strip().split("\t")
    print(repr(count))
    tempLine = in1.readline().strip().split("\t")
    prevLocus = tempLine[0]
    tempLine = in1.readline().strip().split("\t")
    currLocus = tempLine[0]
    isFound = False
#    for i in range(1000):
    while(tempLine != ['']):
        if isFound:
            currLocus = tempLine[0]
        else:
            prevLocus = currLocus
            currLocus = tempLine[0]
            
        if (currLocus == prevLocus):
            out1.write(currLocus + "\t" + tempLine[3][-1] + "\t" + tempLine[4] + "\n")
            tempLine = in1.readline().strip().split("\t")
            if tempLine == ['']:
                break
            prevLocus = tempLine[0]
            tempLine = in1.readline().strip().split("\t")
            isFound = True
        else:
            tempLine = in1.readline().strip().split("\t")
            isFound = False
            
    out1.close()



run()
