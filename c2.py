def mid(a):
    b=list(a)
    l = len(a)
    if l%2 == 0 or l==2:
        return ""
    else:
        r = int(l/2)
        return b[r] 

print(mid("abcd"))

# s="aaaaaaaaaaa"
# l = len(s)

# a = l/2

# print(int(a)+1)