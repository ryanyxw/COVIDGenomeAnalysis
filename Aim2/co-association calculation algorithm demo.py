def Association_between(pValue, Array):
    Distances = []
    Association_score = []
    for value in Array:
        Distances.append(1/abs(value-pValue))
    Sum = sum(Distances)
    for dist in Distances:
        Association_score.append(dist/Sum)
    return Association_score

print(Association_between(1,[2,2,4]))
print(Association_between(8.06458e-02,[1.64869e-01,8.64203e-01,5.81415e-02]))



