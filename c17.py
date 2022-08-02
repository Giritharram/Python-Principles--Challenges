def triple_and(a,b,c):
    if a and b and c == True:
        return True
    return False

p = 5
q = 5

a = p==q
b = p==q
c = p==q
print(triple_and(a,b,c))