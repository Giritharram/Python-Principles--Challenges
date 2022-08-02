def consecutive_zeros(s):
    a = s.split("1")
    t = max(a)
    return len(t)

print(consecutive_zeros("100110000100110"))