def superReducedString(s):
    '''
    superReducedString has the following parameter(s):
      - string s: a string to reduce
    Returns a string: the reduced string or Empty String.
    '''
    
    reduced = []
    
    for i in range(len(s)):
        if len(reduced) == 0 or reduced[-1] != s[i]:
            reduced.append(s[i])
        else:
            reduced.pop()
            
    if len(reduced) == 0:
        return "Empty String"
    else:
        return "".join(reduced)