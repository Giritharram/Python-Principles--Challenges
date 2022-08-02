
def list_xor(n,list1,list2):
    if n not in list1 and n not in list2:
        return False
    if n in list1 and n in list2:
        return False
    if n in list1 and n not in list2:
        return True
    if n in list2 and n not in list1:
        return True
    

print(list_xor(1,[1,2,3],[4,6,7]))

