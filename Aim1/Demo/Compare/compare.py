#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:42:08 2020

@author: ryan04px2021
"""

testRead1 = open("compare1.txt", "r")
testRead2 = open("compare2.txt", "r")

testWrite = open("outputV5.txt", "w")
currLine1 = testRead1.readline()
currLine2 = testRead2.readline()

totalWithin = 0
total = 0 #Result of comparison = totalWithin / total

while(currLine1 != '' and currLine2 != ''):
#    print("currLine1 = " + currLine1)
#    print("currLine2 = " + currLine2)
    value1 = eval(currLine1)
    value2 = eval(currLine2)
    diff = value1 - value2
    if abs(diff) < 200:
        totalWithin += 1
        currLine2 = testRead2.readline()
        total += 1
    else:
        if diff < 0:
            currLine1 = testRead1.readline()
            if currLine1 == '':
                total += 1
        else:
            currLine2 = testRead2.readline()
            total += 1
    

testWrite.write(str(totalWithin / total))

print(totalWithin / total)
testWrite.close()
