def sansaXor(arr):
    '''
    sansaXor has the following parameter(s):
      - int arr[n]: an array of integers
    Returns an int: the result of calculations.
    '''
    result = 0

    if len(arr)%2 == 0:
        return 0
    
    for i in range(0, len(arr), 2):
        result ^= arr[i]
    return result