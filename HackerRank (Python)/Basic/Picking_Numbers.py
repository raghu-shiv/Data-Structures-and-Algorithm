def pickingNumbers(a):
    '''
    pickingNumbers has the following parameter(s):
      - int a[n]: an array of integers
    Returns an int: the length of the longest subarray that meets the criterion.
    '''

    maxLength = 0
    
    for n in set(a):
        count1 = a.count(n) + a.count(n-1)
        count2 = a.count(n) + a.count(n+1)

        if count1 > maxLength or count2 > maxLength:
            maxLength = max(count1, count2)

    return maxLength