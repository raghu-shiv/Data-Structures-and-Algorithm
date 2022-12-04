def commonChild(s1, s2):
    '''
    commonChild has the following parameter(s):
      - string s1: a string
      - string s2: another string

    Returns an int: the length of the longest string which is a common child of the input strings.
    '''

    n = len(s2)
    strLen = [0 for _ in range(n)]
    
    for char in s1:
        curMax = 0
        for i in range(n):
            if char == s2[i]:
                prev = curMax 
                curMax = strLen[i]
                strLen[i] = prev + 1
            else:
                if curMax < strLen[i]:
                    curMax = strLen[i] 
    
    return max(strLen)