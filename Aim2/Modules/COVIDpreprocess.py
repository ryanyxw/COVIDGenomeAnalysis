import numpy as np
import csv
def buildtxt(Target_chr, Disease_type, Directory, Infile):
    Outfile = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\"+Disease_type+"\\[v2] Pos_and_Pvalue_by_Chr" + str(Target_chr) + "_" + Disease_type +".txt"
    open(Outfile, "w")
    Output = open(Outfile, "a")
    with open (Directory+"\\"+Infile, 'r') as Input:
        Output.write("CHR\tPOS\tPvalue\trsid\r")
        for row in csv.reader(Input,delimiter='\t'):
            if row[0] == str(Target_chr):
                Output.write(str(row[0])+'\t'+str(row[1])+'\t'+str(row[17])+'\t'+row[-1]+'\t\r')
            else:
                continue
    Output.close()
    print("[COVID] ["+Disease_type+" Chr"+str(Target_chr)+"] Build preprocessed txt output success")
    return Outfile
