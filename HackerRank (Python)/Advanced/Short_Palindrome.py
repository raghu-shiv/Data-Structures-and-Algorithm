def shortPalindrome(s):
    '''
    shortPalindrome has the following paramter(s):
      - string s: a string

    Returns an int: the number of tuples, modulo (10^9 + 7).
    '''

    mod = 10**9 + 7
    tuples = 0
    s = list(s)
    s1, s3 = [0]*26, [0]*26
    s2 = [[0]*26 for _ in range(26)]
    
    while s:
        i = ord(s.pop()) - 97
        tuples += s3[i] % mod
        
        for j in range(26):
            s3[j] += s2[j][i]
            s2[j][i] += s1[j]
        
        s1[i] += 1
        tuples %= mod
    
    return tuples