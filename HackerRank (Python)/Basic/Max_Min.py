def maxMin(k, arr):
    '''
    maxMin has the following parameter(s):
      - int k: the number of elements to select
      - int arr[n]:: an array of integers
    Returns an int: the minimum possible unfairness.
    '''

    arr.sort()
    unfairness = []
    for i in range(len(arr)-k+1):
        arr1 = arr[i:k+i]
        unfairness.append(arr1[-1] - arr1[0])
    return min(unfairness)