from re import T


def palindrome(s1):
    s2 = s1[::-1]
    if s2 == s1:
        return True
    return False
    

    

print(palindrome("dfda"))