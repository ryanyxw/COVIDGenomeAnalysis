import QQpreprocess as DisPre
import HAPmapping as HapMap
Directory = 'C:\\Users\\timq1\\Desktop\\COVID19_HGI_ANA_A2_V2_20200701'
Disease_type = "BreastCancer"
for Target_chr in range(1,23):
    Sorted_blocks = HapMap.SortBlocks(str(Target_chr), Directory)
    Disease = DisPre.buildtxt(Target_chr, Disease_type, Directory,"BreastCancer.txt")
    #Covid = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\Covid-19\\[v2] Pos_and_Pvalue_by_Chr1_Covid-19.txt"
    Mapped = HapMap.buildtxt(Target_chr, Disease_type, Disease, Sorted_blocks)
