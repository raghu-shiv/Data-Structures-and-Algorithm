def gamingArray(arr):
    '''
    gamingArray has the following parameter(s):
      - int arr[n]: an array of integers
    Returns a string: either ANDY or BOB.
    '''

    count = maxNum = 0
    
    for num in arr:
        if num > maxNum:
            maxNum = num
            count += 1
    
    return "ANDY" if count%2==0 else "BOB"