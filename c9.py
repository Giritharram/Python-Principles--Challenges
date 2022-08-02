from collections import Counter

def is_anagram(s1,s2):
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False


print(is_anagram("listen","silent"))