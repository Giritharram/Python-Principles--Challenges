

def largest_difference(list1):
    list1.sort()
    r = list1[-1] - list1[0]
    return r

list1 = [66,44,3,12]
print(largest_difference(list1))