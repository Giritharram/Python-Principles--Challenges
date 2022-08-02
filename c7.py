
def add_dots(s):
    adstring = s 
    adstring = ".".join(s)
    return adstring

def remove_dots(s):
    rdstring = s
    rdstring = s.replace(".","")
    return rdstring

print(add_dots("test"))
print(remove_dots("t.e.s.t"))

print(remove_dots(add_dots("test")))