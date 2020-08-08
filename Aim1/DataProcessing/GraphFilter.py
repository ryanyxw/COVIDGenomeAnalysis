#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 15:44:18 2020

@author: ryan04px2021
"""
import subprocess
import math
import matplotlib.pyplot as plt
import numpy as np

folderName = "CoronaryArteryDisease"
fileName= "CoronaryArteryDisease.tsv"
pIndex = 11
posIndex = 0

##############################################################################################################################################################################################
in2 = open(folderName + "/Sorted.txt", "r")
out2 = open(folderName + "/GraphValue.txt", "w")

tempLine = in2.readline().split("\t")

logTen = math.log(10, 10)

y = []
x = []

lengthCommand = ("wc -l " + folderName + "/Sorted.txt").split(" ")
result = subprocess.run(lengthCommand, stdout=subprocess.PIPE)
strResult = str(result.stdout)


totalCount = ""
isFound = False
isStop = False
for i in strResult:
    if i.isdigit():
        isFound = True
        totalCount += i
    else:
        if isFound == True:
            break

totalCount = int(totalCount)

print("Total of " + repr(totalCount) + " rows found")

#totalCount = 24600932
#totalCount = 100

count = totalCount
#while(tempLine != ['']):

for i in range(totalCount-1):
    currVal = tempLine[0]
#    print("tempLine = " + repr(tempLine))
#    print("currVal = " + currVal)
    ind = currVal.find("e")
    tempNum = 0
    if (ind != -1):
        firstNum = currVal[:ind]
#        print("firstNum = " + repr(firstNum))
        secondNum = currVal[ind+1:]
#        print("secondNum = " + repr(secondNum))
#        print("inted = " + repr(int(secondNum)))
        tempNum = math.log(eval(firstNum), 10) + int(secondNum) * logTen
    else:
        tempNum = math.log(eval(currVal), 10)
#    yRecordVal = -1/2.5 * tempNum
    yRecordVal = -1 * tempNum
#    print("yRecordVal = " + repr(yRecordVal))
    
#    if yRecordVal > 25:
#        break
    
    y += [yRecordVal]
#    print("yRecordVal ======================== " + repr(yRecordVal))
    tempLine = in2.readline().split("\t")
    
    
    currPerc = count / totalCount
    count -= 1
    xRecordVal = -1 * math.log(currPerc, 10)
#    print("currPerc = " + repr(currPerc))
#    print("xRecordVal = " + repr(xRecordVal))
    x += [xRecordVal]
    
    out2.write(str(xRecordVal) + "\t" + str(yRecordVal) + "\n")

print("X and Y Axis values computed")

#x.sort()
#print(x == sorted(x))
#y.sort()
#print(x)
xAxis = np.array(x)
#print(y)
yAxis = np.array(y)

plt.plot(xAxis, yAxis, "o")


plt.plot([0, 7], [0, 7])


plt.xlabel("Predicted -log(P-value)")
plt.ylabel("Actual -log(P-value)")

plt.title("QQ Plot of COVID GWAS")
plt.show()

out2.close()

print("Graph plotted")

##############################################################################################################################################################################################


QQRead = open(folderName + "/GraphValue.txt", "r")
SNPRead = open(folderName + "/Sorted.txt", "r")
out3 = open(folderName + "/FilteredDataFinal.txt", "w")
currQQLine = QQRead.readline().strip().split("\t")
currSNPLine = SNPRead.readline().split("\t")


threshold = input("Please type the threshold : ")

count = 0

while(currQQLine != ['']):
#    print(currSNPLine)
    if eval(currQQLine[1]) > eval(threshold):
        out3.write(currQQLine[1] + "\t" + currSNPLine[0] + "\t" + currSNPLine[1])
        count += 1
    currQQLine = QQRead.readline().strip().split("\t")
    currSNPLine = SNPRead.readline().split("\t")


QQRead.close()
SNPRead.close()
print("Process Complete with " + repr(count) + " SNPs remaining")