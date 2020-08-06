import numpy as np
import csv, re
Target_chr = "2"
Filename = "Sorted_LD_map_by_Chr" + Target_chr + ".txt"
open(Filename, "w")
Output = open(Filename, "a")
Ld_blocks = []
with open ('C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701\\1000G_CEPH_ldblocks_wp_16102013\\chr2_1000G_CEPH_ldblocks_wp_16102013.txt', 'r') as f:
    for row in csv.reader(f,delimiter='\t'):
        Block_number = re.sub("[^0-9]", "", row[3])
        Ld_blocks.append([int(row[1]),int(row[2]),int(Block_number)])
Sorted_blocks = sorted(Ld_blocks, key=lambda a_entry: a_entry[0])
print(np.array(Sorted_blocks))
