from collections import Counter

def anagram(s):
    '''
    anagram has the following parameter(s):
      - string s: a string

    Returns an int: the minimum number of characters to change or -1. 
    '''

    l = len(s)
    
    if l%2 == 1: return -1
    
    s = Counter(s[:l//2]) - Counter(s[l//2:])
    
    return sum(s.values())