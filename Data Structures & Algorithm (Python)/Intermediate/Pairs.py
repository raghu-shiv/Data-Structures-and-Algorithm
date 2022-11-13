def pairs(k, arr):
    '''
    The function accepts following parameters:
      1. INTEGER k, the target difference.
      2. INTEGER_ARRAY arr, an array of integers.  
    Returns an int: the number of pairs that satisfy the criterion.
    '''

    pairs = 0
    arr = set(arr)
    
    for num in arr:
        if num + k in arr:
            pairs += 1
    
    return pairs