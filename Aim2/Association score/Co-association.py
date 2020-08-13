import CoassociationAlgorithm as CoA
import pandas as pd
import math
def buildtext(Target_disease):
    Disease = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\"+Target_disease+"\\"
    CovidInf = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\Covid\\"
    CovidHos = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\HosCovid\\"
    CovidSev = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Modules\\SevereCovid\\"
    Outfile = "C:\\Users\\timq1\\Desktop\\Machine Learning Genomics\\Codes\\Score\\"+Target_disease+"_Co-association_score.txt"
    open(Outfile, "w")
    Output = open(Outfile, "a")
    Output.write("CHR\tPOS\tPvalue\t-Log\twithInf\twithHos\twithSev\tMax\tBlStart\tBlEnd\r")
    #================
    print(Target_disease)
    for Target_chr in range(1,23):
        print("#"*10+str(Target_chr)+"#"*10)
        Dis = pd.read_csv(Disease+"[v2] LDmapped_"+Target_disease+"_Pvalues_by_Chr"+str(Target_chr)+".txt", sep = "\t")
        Inf = pd.read_csv(CovidInf+"[v2] LDmapped_Covid_Pvalues_by_Chr"+str(Target_chr)+".txt", sep = "\t")
        Hos = pd.read_csv(CovidHos+"[v2] LDmapped_HosCovid_Pvalues_by_Chr"+str(Target_chr)+".txt", sep = "\t")
        Sev = pd.read_csv(CovidSev+"[v2] LDmapped_SevereCovid_Pvalues_by_Chr"+str(Target_chr)+".txt", sep = "\t")
        #print(Dis);print(Inf);print(Hos);print(Sev)
        #print(pd.Index(Inf["BlStart"]).get_loc(6020992))
        #print(pd.Index(Inf["BlStart"]).contains(6020992))
        #and (Position in Hos["BlStart"]) and (Position in Sev["BlStart"])
        for Dis_index in range(len(Dis)):
            Position = Dis["BlStart"][Dis_index]
            if pd.Index(Inf["BlStart"]).contains(Position) and pd.Index(Hos["BlStart"]).contains(Position) and pd.Index(Sev["BlStart"]).contains(Position):
                Inf_index = pd.Index(Inf["BlStart"]).get_loc(Position)
                Hos_index = pd.Index(Hos["BlStart"]).get_loc(Position)
                Sev_index = pd.Index(Sev["BlStart"]).get_loc(Position)
                Pdisease = Dis["Pvalue"][Dis_index]
                Parray = [Inf["Pvalue"][Inf_index], Hos["Pvalue"][Hos_index], Sev["Pvalue"][Sev_index]]
                #print(Position, Inf["Pvalue"][Inf_index])
                Score = CoA.score(Pdisease,Parray)
                Output.write(str(Target_chr)+"\t"+str(Dis["POS"][Dis_index])+"\t"+str(Dis["Pvalue"][Dis_index])+"\t"+str(-math.log10(Dis["Pvalue"][Dis_index]))+"\t"+\
                             str(Score[0])+"\t"+str(Score[1])+"\t"+str(Score[2])+"\t"+str(max(Score))+"\t"+str(Dis["BlStart"][Dis_index])+"\t"+str(Dis["BlEnd"][Dis_index])+"\r")

    Output.close()
    return Outfile
for Target_disease in ["BreastCancer","ChronicKidneyDisease","ChronicObstructivePulmonaryDisease","CoronaryArteryDisease","LungCancer","Obesity","Type2Diabetes"]:
    print(buildtext(Target_disease))

