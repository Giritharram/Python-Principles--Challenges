def zap(a,b):
    r = []
    for i in range(len(a)):
        tup = (a[i],b[i])
        r.append(tup)
    return r 

print(zap([0, 1, 2, 3], [5, 6, 7, 8]))
