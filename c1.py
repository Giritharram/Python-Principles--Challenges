def capital_indexes(a):
    b=0
    l=[]
    for i in a:
        if i.isupper():
            l.append(b)
        b+=1
    return l

print(capital_indexes("HI"))