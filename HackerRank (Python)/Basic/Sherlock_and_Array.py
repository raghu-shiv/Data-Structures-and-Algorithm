def balancedSums(arr):
    '''
    balancedSums has the following parameter(s):
      - int arr[n]: an array of integers
    Returns a string: either YES or NO.
    '''

    right = sum(arr)
    left = 0
    
    for num in arr:
        right -= num
        if left == right:
            return "YES"
        left += num
    return "NO"