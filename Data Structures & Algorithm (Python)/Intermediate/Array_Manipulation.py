def arrayManipulation(n, queries):
    '''
    The function accepts following parameters:
      1. INTEGER n, the number of elements in the array
      2. 2D_INTEGER_ARRAY queries, where each queries[i] contains three integers, a, b, and k.
    Returns an int - the maximum value in the resultant array.
    '''

    arr = [0] * (n+2)
    
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
    
    maxVal = curVal = 0
    for num in arr:
        curVal += num
        maxVal = max(curVal, maxVal)
    
    return maxVal