def get_row_col(s):
    t1=s.upper()
    col =t1[0]
    row =int(t1[1])-1

    b = {"A":0,"B":1,"C":2}

    for k in b:
        if k == col:
            column = b[k]
            print(row,column)

get_row_col("a3")