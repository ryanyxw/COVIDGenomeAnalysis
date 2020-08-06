import numpy as np
import csv, re
Target_chr = "1"
Disease_type = "Coronary artery disease"
Filename = "Pos_and_Pvalue_by_Chr" + Target_chr + "_" + Disease_type +".txt"
open(Filename, "w")
Output = open(Filename, "a")
with open ('C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701\\I9_CORATHER.gwas.imputed_v3.both_sexes.txt', 'r') as f:
    Output.write("CHR\tPOS\tPvalue\r")
    #print('ss')
    for row in csv.reader(f,delimiter='\t'):
        #print(row[0])
        Number_part = re.sub("[^0-9]", "", row[0])
        Chr = Number_part[:len(Target_chr)]
        Pos = Number_part[len(Target_chr):]
        if Chr == Target_chr:
            Output.write(Chr+'\t'+Pos+'\t'+row[-1]+'\t\r')
        else:
            continue
    Output.close()
