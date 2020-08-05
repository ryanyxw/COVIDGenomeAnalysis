#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:09:27 2020

@author: ryan04px2021
"""

#This file takes the two columns of position and pvalue and creates a file sortedPValue.txt that only has one column of pvalue

#testRead = open("SNP+PValue.txt", "r")
#testWrite = open("sortedPValue.txt", "w")

testRead = open("outputV2demo.txt", "r")
testWrite = open("outputV3demo.txt", "w")
currLine = testRead.readline().split("\t")
currLine = testRead.readline().split("\t")



while(currLine != ['']):
    testWrite.write(currLine[1])
    currLine = testRead.readline().split("\t")


    
testWrite.close()

