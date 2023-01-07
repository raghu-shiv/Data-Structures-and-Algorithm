def closestNumbers(arr):
    '''
    closestNumbers has the following parameter(s):
      - int arr[n]: an array of integers

    Returns an int[]: an array of integers as described.
    '''

    arr.sort()
    pairs = []
    minDiff = arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        diff = abs(arr[i-1] - arr[i])
        # new minimum difference
        if diff < minDiff:
            minDiff = diff
            pairs = [arr[i-1], arr[i]]
        # already existing minimum difference
        elif diff == minDiff:
            pairs.extend([arr[i-1], arr[i]])
            
    return pairs