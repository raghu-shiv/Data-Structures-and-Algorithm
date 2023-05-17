from collections import defaultdict

def shortPalindrome(s):
    '''
    shortPalindrome has the following paramter(s):
      - string s: a string

    Returns an int: the number of tuples, modulo (10^9 + 7).
    '''
    
    mod = 10**9 + 7
    tuples = 0
    
    d1 = defaultdict(int)
    d2 = defaultdict(lambda: defaultdict(int))
    d3 = defaultdict(lambda: defaultdict(int))
    
    for char in s:
        tuples += sum(d3[char].values()) % mod
        for k, d in d2.items():
            d3[k][char] += d[char]
        for k, v in d1.items():
            d2[k][char] += v
        d1[char] += 1
    return tuples % mod
