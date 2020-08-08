def WithinRange(pos, low, up):
    return ((low <= pos) and (pos < up))


import numpy as np
import csv, re
Target_chr = "1"
Target_disease = "Covid"
###1. Sort LD blocks in ascending starting position###
Ld_blocks = []
with open ('C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701\\1000G_CEPH_ldblocks_wp_16102013\\chr1_1000G_CEPH_ldblocks_wp_16102013.txt', 'r') as f:
    for row in csv.reader(f,delimiter='\t'):
        Block_number = re.sub("[^0-9]", "", row[3])
        Ld_blocks.append([int(row[1]),int(row[2]),int(Block_number)])
Sorted_blocks = sorted(Ld_blocks, key=lambda a_entry: a_entry[0])
print(np.array(Sorted_blocks))

###2. Create output file###
Filename = "LDmapped_" + Target_disease + "_Pvalues_by_Chr" + Target_chr + ".txt"
open(Filename, "w")
Output = open(Filename, "a")
Output.write("CHR\tPOS\tPvalue\tBlStart\tBlEnd\tBlock#\r")

###3. Map using LD blocks###
with open ('C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701\\Pos_and_Pvalue_by_Chr1_Covid.txt', 'r') as f:
    Current_start_pos = 1
    Pvalue_list = list(csv.reader(f,delimiter='\t'))
    print('Original length =',len(Pvalue_list),' Reduced length after mapping =',len(Sorted_blocks))
    ###4. Put all SNP within same haplotype block into temp array###  
    for block in Sorted_blocks:
        #print("next")
        Temp_array = []
        while True:
            Current_value = Pvalue_list[Current_start_pos]
            if WithinRange(int(Current_value[1]), block[0], block[1]):
                
                Current_value[2] = eval(Current_value[2])
                Temp_array.append(Current_value)
            elif int(Current_value[1])>block[1]:
                break
            Current_start_pos += 1
    ###5. Find min p-value in each block and output###
        Min_p = sorted(Temp_array, key=lambda a_entry: a_entry[2])
        if len(Min_p) != 0:
            #print("out:\t"+str(Min_p[0][1])+'\t'+str(block[0])+'\t'+str(block[1])+'\t')
            Output.write(Target_chr+'\t'+str(Min_p[0][1])+'\t'+str(Min_p[0][2])+'\t' +str(block[0])+'\t'+str(block[1])+'\t'+str(block[2])+'\r') 
        else: continue
Output.close()
    
        

        
