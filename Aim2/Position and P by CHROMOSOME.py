import numpy as np
import csv
Target_chr = "1"
Disease_type = "Covid"
Filename = "Pos_and_Pvalue_by_Chr" + Target_chr + "_" + Disease_type +".txt"
open(Filename, "w")
Output = open(Filename, "a")
with open ('C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701\\COVID19_HGI_ANA_A2_V2_20200701.txt', 'r') as f:
    Output.write("CHR\tPOS\tall_inv_var_meta_p\trsid\r")
    #print('ss')
    for row in csv.reader(f,delimiter='\t'):
        #print(row[0])
        if row[0] == Target_chr:
            Output.write(str(row[0])+'\t'+str(row[1])+'\t'+str(row[17])+'\t'+row[-1]+'\t\r')
        else:
            continue
    Output.close()
