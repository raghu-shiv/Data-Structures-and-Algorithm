def isValid(s):
    '''
    isValid has the following parameter(s):
      - string s: a string
    Returns a string: either YES or NO
    '''

    if len(s) == 1: return "YES"
    
    chars = set(s)
    freqs = []
    
    for char in chars:
        charCount = list(s).count(char)
        freqs.append(charCount)
    
    freqs.sort()
    n = len(freqs)    
    
    if(freqs[n-2]+1==freqs[n-1] and freqs[0]==freqs[n-2]):
        return "YES"
    elif(freqs[0]==freqs[n-1]):
        return "YES"
    elif(freqs[0]==1 and freqs[1]==freqs[n-1]):
        return "YES"
    return "NO"