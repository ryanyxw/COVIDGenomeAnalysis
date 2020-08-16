#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:46:37 2020

@author: ryanwang
"""

currentFile = "hu8A5FBF" + ".txt"

def run():
    out1 = open("GenotypeMatrix.txt", "w")
    addIndividual(currentFile, out1)
    
    out1.close()

def addIndividual(currentFile, out1):
    in1 = open("Data/" + currentFile, "r")
    hapFile = open("CombinedHap.txt")
    tempLine = in1.readline().strip().split("\t")
    tempHap = hapFile.readline().strip().split("\t")
 #   tempLine = repr(in1.readline())
    while(tempLine[0] != "# rsid"):
#    for i in range(15):
#        print(tempLine)
        tempLine = in1.readline().strip().split("\t")
#        tempLine = repr(in1.readline())
    tempLine = in1.readline().strip().split("\t")
    print(tempLine)
    hapChrom = int(tempHap[0])
    hapPosStart = int(tempHap[1])
    hapPosEnd = int(tempHap[2])
    hapArr = []
    hapArr += ["0"]
    hapIndex = 0
    
    
    tempLine = in1.readline().strip().split("\t")
    currChrom = int(tempLine[1])
    currPos = int(tempLine[2])
    
    isHap = False#False = tempLine incrased, while True = hap increased
    while ((tempLine != [""]) and (tempHap != [""])):
        if isHap:
            hapChrom = int(tempHap[0])
            hapPosStart = int(tempHap[1])
            hapPosEnd = int(tempHap[2])
            hapIndex += 1
            hapArr += ["0"]
        else:
            currChrom = int(tempLine[1])
            currPos = int(tempLine[2])
        if currChrom < hapChrom:
            tempLine = in1.readline().strip().split("\t")
            isHap = False
        elif currChrom > hapChrom:
            tempHap = hapFile.readline().strip().split("\t")
            isHap = True
        else:
            if currPos < hapPosStart:
                tempLine = in1.readline().strip().split("\t")
                isHap = False
            elif currPos > hapPosStart and currPos < hapPosEnd:
                hapArr[hapIndex] = "1"
                tempLine = in1.readline().strip().split("\t")
                isHap = False
            else:
                tempHap = hapFile.readline().strip().split("\t")
                isHap = True
    returnStr = "\t".join(hapArr)
    out1.write(returnStr + "\n")
run()