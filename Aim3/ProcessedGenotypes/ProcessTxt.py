#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:46:37 2020

@author: ryanwang
"""
import os

folderName = "TXT"
totalFile = os.listdir("./Data/" + folderName)

#totalFile = ["hu8A5FBF", "hu781EE2", "huE24522", "huFD847C"]

def run():
    out1 = open(folderName + "GenotypeMatrix.txt", "w")
    count = 1
    
    for personID in totalFile:
        currentFile = folderName + "/" + personID
        addIndividual(currentFile, out1, count)
        count += 1
    out1.close()

def addIndividual(currentFile, out1, count):
    print(currentFile)
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
    #tempLine = in1.readline().strip().split("\t")
    print(repr(count))
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
            if tempLine[1] == "X" or tempLine[1] == "Y":
                break
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
    print("final = " + repr(tempLine))
    returnStr = "\t".join(hapArr)
    out1.write(returnStr + "\n\n")
run()