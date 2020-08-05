#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:37:28 2020

@author: ryan04px2021
"""
#testRead = open("outputV3.txt", "r")
#testWrite = open("outputV4.txt", "w")

testRead = open("outputV5demo.txt", "r")
testWrite = open("outputV6demo.txt", "w")
currLine = testRead.readline().split("\t")

totalNum = 100
threshold = 1.5

#while(currLine != ['']):
for i in range(totalNum-1):
    if eval(currLine[1]) > threshold:
        testWrite.write(currLine[1] + "\n")
    currLine = testRead.readline().split("\t")


testWrite.close()
