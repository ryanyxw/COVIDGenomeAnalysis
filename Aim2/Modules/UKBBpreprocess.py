import numpy as np
import csv, re
import pandas as pd
#Infile = 'I9_CORATHER.gwas.imputed_v3.both_sexes.txt'
def buildtxt(Target_chr, Disease_type, Directory, Infile):
    Outfile = "[v2] Pos_and_Pvalue_by_Chr" + str(Target_chr) + "_" + Disease_type +".txt"
    open(Outfile, "w")
    Output = open(Outfile, "a")
    with open (Directory+"\\"+Infile, 'r') as Input:
        Output.write("CHR\tPOS\tPvalue\r")
        for row in Input:
            Snp = re.split('\t|:|\n', row)
            if Snp[0] == str(Target_chr):
                #print(Snp)
                Output.write(Snp[0]+'\t'+Snp[1]+'\t'+Snp[-2]+'\r')
    Output.close()
    print("[UKBB] ["+Disease_type+" Chr"+str(Target_chr)+"] Build preprocessed txt output success")
    return Outfile
