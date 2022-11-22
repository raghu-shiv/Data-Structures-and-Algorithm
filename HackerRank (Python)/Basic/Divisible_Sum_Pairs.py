def divisibleSumPairs(n, k, ar):
    '''
    divisibleSumPairs has the following parameter(s):
      - int n: the length of array ar 
      - int ar[n]: an array of integers
      - int k: the integer divisor
    Returns an int: the number of pairs.
    '''

    pairs = 0
    
    for i in range(n):
        for j in range(n):
            if i < j and (ar[i]+ar[j])%k == 0:
                pairs += 1
    return pairs