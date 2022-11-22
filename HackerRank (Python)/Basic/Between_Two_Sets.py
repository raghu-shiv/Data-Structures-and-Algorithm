def getTotalX(a, b):
    '''
    getTotalX has the following parameter(s):
      - int a[n]: an array of integers
      - int b[m]: an array of integers
    Returns an int: the number of integers that are between the sets.
    '''

    maxA = max(a)
    minB = min(b)
    betweenTheSets = 0
    
    for i in range(maxA, minB+1):
        if all([i%x==0 for x in a]):
            if all([y%i==0 for y in b]):
                betweenTheSets += 1

    return betweenTheSets