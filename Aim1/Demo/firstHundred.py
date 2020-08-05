#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:32:05 2020

@author: ryan04px2021
"""

import math
import matplotlib.pyplot as plt
import numpy as np

#testRead = open("../../sortedOutput.txt", "r")
#testWrite = open("outputV3.txt", "w")
testRead = open("outputV4demo.txt", "r")
testWrite = open("outputV5demo.txt", "w")

currLine = testRead.readline()

logTen = math.log(10)

y = []
x = []

#totalNum = 24600932
totalNum = 100

count = totalNum
#while(currLine != ['']):

for i in range(totalNum-1):
    currVal = currLine
    print("currLine = " + currVal)
    ind = currVal.find("e")
    tempNum = 0
    if (ind != -1):
        firstNum = currVal[:ind]
        secondNum = currVal[ind+1:]
        tempNum = math.log(eval(firstNum), 10) + int(secondNum) * logTen
    else:
        tempNum = math.log(eval(currVal), 10)
#    yRecordVal = -1/2.5 * tempNum
    yRecordVal = -1 * tempNum - 1
#    print("yRecordVal = " + repr(yRecordVal))
    y += [yRecordVal]
    currLine = testRead.readline()
    
    
    currPerc = count / totalNum
    count -= 1
    xRecordVal = -1 * math.log(currPerc, 10)
#    print("currPerc = " + repr(currPerc))
#    print("xRecordVal = " + repr(xRecordVal))
    x += [xRecordVal]
    testWrite.write(str(xRecordVal) + "\t" + str(yRecordVal) + "\n")

x.sort()
y.sort()

xAxis = np.array(x)
yAxis = np.array(y)

plt.plot(xAxis, yAxis, "o")


plt.plot([0, 7], [0, 7])


plt.xlabel("Predicted -log(P-value)")
plt.ylabel("Actual -log(P-value)")

plt.title("QQ Plot of COVID GWAS")
plt.show()

testWrite.close()

