def palindromeIndex(s):
    '''
    palindromeIndex has the following parameter(s):
      - string s: a string to analyze
    Returns an int: the index of the character to remove or -1.
    '''

    if s == s[::-1]: 
        return -1
        
    l = len(s)
    for i in range(l//2):
        if s[i] != s[l-i-1]:
            s1 = s[:i] + s[i+1:]
            if s1 == s1[::-1]:
                return i
            else:
                return l-i-1
    return -1