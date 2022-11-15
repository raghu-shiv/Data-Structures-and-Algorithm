def findMedian(arr):
    '''
    findMedian has the following parameter(s):
      - int arr[n]: an unsorted array of integers
    Returns an int: the median of the array.
    '''

    arr.sort()
    medianIndex = (len(arr)+1)//2

    return arr[medianIndex-1]