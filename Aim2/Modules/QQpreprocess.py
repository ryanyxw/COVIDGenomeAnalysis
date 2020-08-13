import numpy as np
import csv, re
import pandas as pd
#Infile = 'I9_CORATHER.gwas.imputed_v3.both_sexes.txt'
def buildtxt(Target_chr, Disease_type, Directory, Infile):
    Temp_array = []
    Outfile = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\"+Disease_type+"\\[v3] Pos_and_Pvalue_by_Chr" + str(Target_chr) + "_" + Disease_type +".txt"
    open(Outfile, "w")
    Output = open(Outfile, "a")
    with open (Directory+"\\"+Infile, 'r') as Input:
        Output.write("CHR\tPOS\tPvalue\r")
        for row in Input:
            Snp = re.split('\t|:|\n', row)
            #print(Snp)
            if Snp[2] == str(Target_chr):
                #print(Snp)
                Temp_array.append([Snp[2],int(Snp[3]),Snp[1]])
    for Snp in sorted(Temp_array, key=lambda a_entry: a_entry[1]):
        Output.write(Snp[0]+'\t'+str(Snp[1])+'\t'+Snp[2]+'\r')
    Output.close()
    print("[QQplot] ["+Disease_type+" Chr"+str(Target_chr)+"] Build preprocessed txt output success")
    return Outfile

