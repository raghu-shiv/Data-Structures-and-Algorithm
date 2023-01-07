def miniMaxSum(arr):
    '''
    miniMaxSum has the following parameter(s):
      - arr: an array of 5 integers
    Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
    '''

    arr.sort()
        
    minSum = sum(arr[:4])
    maxSum = sum(arr[-4:])

    print(f"{minSum} {maxSum}")