from collections import Counter

def missingNumbers(arr, brr):
    '''
    missingNumbers has the following parameter(s):
      - int arr[n]: the array with missing numbers
      - int brr[m]: the original array of numbers
    Returns an int[]: an array of integers.
    '''

    c1 = Counter(arr)
    c2 = Counter(brr)
    c = c2 - c1
    # print(c)
    
    missingNum = sorted(c.keys())
    return missingNum