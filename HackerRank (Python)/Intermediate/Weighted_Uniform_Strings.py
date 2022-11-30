def weightedUniformStrings(s, queries):
    '''
    weightedUniformStrings has the following parameter(s):
      - string s: a string
      - int queries[n]: an array of integers

    Returns a string[n]: an array of strings that answer the queries.
    '''
    
    answers = []
    # to store the weights present in the string
    weightDict = {}
    weight = 0

    for i in range(len(s)):
        # if adjacent chars are different
        if i == 0 or s[i] != s[i-1]:
            weight = ord(s[i]) - ord('a') + 1
        else:
            weight += ord(s[i]) - ord('a') + 1
        
        # store the weight
        weightDict[weight] = 1

    # result
    for q in queries:
        answers.append('Yes' if q in weightDict else 'No')
    
    return answers