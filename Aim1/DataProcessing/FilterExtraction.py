#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 10:47:08 2020

@author: ryan04px2021
"""
import subprocess


folderName = "NewHospitalized"
fileName= "Hospitalized.txt"
pIndex = 32
posIndex = 4

#Tests how to extract a specific column in a file

in1 = open("../Data/" + fileName, "r")

'''
currLine = in1.readline().strip().split("\t")
print(currLine)
print(currLine.index("SNP"))
print(currLine.index("all_inv_var_meta_p"))
#out1 = open("outputV2.txt", "w")
'''
out1 = open(folderName + "/PvaluePos.txt", "w")
currLine = in1.readline().strip().split("\t")


def convertNum(num):
    ind = num.find("e")
    if (ind != -1):
        firstNum = num[:ind]
        secondNum = num[ind+1:]
        num = secondNum + firstNum
    else:
        print("Error. Scientific notation not used")
    return num

def isValid(currLine):
    try:
#        print(type(currLine[posIndex]))
#        print("currLine = " + repr(currLine))
#        print("posIndex = " + currLine[posIndex])
        if (currLine[posIndex][0].isdigit() == False or currLine[pIndex][-1].isdigit() == False):
            return False
        return True
    except:
        print("entered except, pvalue is not a integer")
        return False
 
#totalNum = 1000
while(currLine != ['']):
#for i in range(totalNum):
    if isValid(currLine):
        out1.write(currLine[pIndex] + "\t" + currLine[posIndex] + "\n")
    currLine = in1.readline().strip().split("\t")

print("Data extraction and preliminary processing complete")
out1.close()
command = "sort -g -r -o " + folderName + "/Sorted.txt " + folderName + "/PvaluePos.txt"
#command = "sort -g -r -o Obesity/Sorted.txt Obesity/PvaluePos.txt"

p = subprocess.Popen(command, shell=True)
print(p)
print("Data sorting complete")


