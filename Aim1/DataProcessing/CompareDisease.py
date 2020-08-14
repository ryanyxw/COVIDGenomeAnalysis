#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:42:08 2020

@author: ryan04px2021
"""

inputFolder = "Type2Diabetes"

def getValue(inputFolder, COVIDFile):

    folderName = inputFolder
    
    
    
    in1 = open(COVIDFile, "r")
    in2 = open(folderName + "/FilteredPos.txt", "r")
    
    tempLine1 = in1.readline().strip().split(":")
    tempLine2 = in2.readline().strip().split(":")
    
    
    
    chrom1 = tempLine1[0]
    chrom2 = tempLine2[0]
    position1 = tempLine1[1]
    position2 = tempLine2[1]
    
    totalWithin = 0
    total = 0 #Result of comparison = totalWithin / total
    
    
    
    
    while(tempLine1 != [''] and tempLine2 != ['']):
#        print("chrom1 = " + repr(chrom1))
#        print("chrom2 = " + repr(chrom2))
#        print("position1 = " + repr(position1))
#        print("position2 = " + repr(position2))
        position1 = int(position1)
        position2 = int(position2)
        chrom1 = int(chrom1)
        chrom2 = int(chrom2)
        if (chrom1 == chrom2):
 #           print("Chromosome Same")
            diff = position1 - position2
            if abs(diff) < 100000:
 #               print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Within Range")
                totalWithin += 1
                tempLine2 = in2.readline().strip().split(":")
                if (tempLine2 == [""]):
                    break
                chrom2 = tempLine2[0]
                position2 = tempLine2[1]
                total += 1
            else:
#                print("Not in range")
                if diff < 0:
#                    print("Chrom1 smaller than Chrom2")
                    tempLine1 = in1.readline().strip().split(":")
                    if (tempLine1 == [""]):
                        total += 1
                        break
                    chrom1 = tempLine1[0]
                    position1 = tempLine1[1]
    
                else:
#                    print("Chrom1 bigger than chrom2")
                    tempLine2 = in2.readline().strip().split(":")
                    if (tempLine2 == [""]):
                        break
                    chrom2 = tempLine2[0]
                    position2 = tempLine2[1]
                    total += 1
        else:
#            print("Chromosome Different")
            while(chrom1 != chrom2):
#                print("position1 = " + repr(position1))
#                print("position2 = " + repr(position2))
#                print("chrom1 = " + repr(chrom1))
#                print("chrom2 = " + repr(chrom2))
                if chrom1 < chrom2:
                    tempLine1 = in1.readline().strip().split(":")
                    if (tempLine1 == [""]):
                        total += 1
                        break
                    chrom1 = int(tempLine1[0])
                    position1 = tempLine1[1]
                    total += 1
                else:
                    tempLine2 = in2.readline().strip().split(":")
                    if (tempLine2 == [""]):
                        break
                    chrom2 = int(tempLine2[0])
                    position2 = tempLine2[1]
                    total += 1
        
    

    returnValue = totalWithin / total
    print(COVIDFile + " : " + repr(returnValue))
    return returnValue


def getDisease(inputFolder):
    covidArr = ["NewInfected/FilteredPos.txt", "NewSevere/FilteredPos.txt", "NewHospitalized/FilteredPos.txt"]
    out1 = open(inputFolder  + "/Compare.txt", "w")
    print("Disease = " + inputFolder)
    for cov in covidArr:
        tempReturn = getValue(inputFolder, cov)
        out1.write(str(tempReturn) + "\t")
    out1.close()


totalDisease = ["BreastCancer", "ChronicKidneyDisease", "ChronicObstructivePulmonaryDisease", "CoronaryArteryDisease", "LungCancer", "Obesity", "Type2Diabetes"]

for inputFolder in totalDisease:
    getDisease(inputFolder)
