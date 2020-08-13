def WithinRange(pos, low, up):
    return ((low <= pos) and (pos < up))

def AverageP(array):
    Sum = 0
    for position in array:
        Sum += position[2]
    return (Sum/len(array))

import numpy as np
import pandas as pd
import csv
Target_chr = "1"
Disease_type = "Covid"
Directory = 'C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701'
###1. Sort LD blocks in ascending starting position###
def SortBlocks(Target_chr, Directory):
    Infile = '1000G_CEPH_ldblocks_wp_16102013\\chr'+str(Target_chr)+'_1000G_CEPH_ldblocks_wp_16102013.txt'
    Input = pd.read_csv(Directory+"\\"+Infile\
                        , sep = "\t", usecols = [1,2,3], skiprows=[0], header=None)
    return Input.sort_values(by=[1])

def buildtxt(Target_chr, Disease_type, Infile, Sorted_blocks):
    ###2. Create output file###
    Outfile = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\"+Disease_type+"\\[v2] LDmapped_" + Disease_type + "_Pvalues_by_Chr" + str(Target_chr) + ".txt"
    open(Outfile, "w")
    Output = open(Outfile, "a")
    Output.write("CHR\tPOS\tPvalue\tBlStart\tBlEnd\tBlock#\tAverageP\r")

    ###3. Map using LD blocks###
    with open (Infile, 'r') as f:
        Current_start_pos = 1
        Pvalue_list = list(csv.reader(f,delimiter='\t'))
        #print('Original length =',len(Pvalue_list),' Reduced length after mapping =',len(Sorted_blocks))
        ###4. Put all SNP within same haplotype block into temp array###  
        for block in np.array(Sorted_blocks):
            Temp_array = []
            while True:
                try:
                    Current_value = Pvalue_list[Current_start_pos]
                except IndexError:
                    break
                if WithinRange(int(Current_value[1]), block[0], block[1]):
                    Current_value[2] = eval(Current_value[2])
                    Temp_array.append(Current_value)
                elif (int(Current_value[1])>block[1]):
                    break
                Current_start_pos += 1
        ###5. Find min p-value in each block and output###
            Min_p = sorted(Temp_array, key=lambda a_entry: a_entry[2])
            if len(Min_p) != 0:
                #print("out:\t"+str(Min_p[0][1])+'\t'+str(block[0])+'\t'+str(block[1])+'\t')
                Output.write(str(Target_chr)+'\t'+str(Min_p[0][1])+'\t'+str(Min_p[0][2])+'\t'\
                             +str(block[0])+'\t'+str(block[1])+'\t'+str(block[2])+'\t'+str(AverageP(Min_p))+'\r')
            else: continue
    Output.close()
    print("["+Disease_type+" Chr"+str(Target_chr)+"] Build haplotype mapped txt output success")
    return Outfile
        
        
