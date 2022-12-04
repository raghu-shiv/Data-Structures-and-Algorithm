from copy import *

def almostSorted(arr):
    '''
    almostSorted has the following parameter(s):
      - int arr[n]: an array of integers
    Print the results as described and return nothing.
    '''

    # copy array elements
    sort_arr = deepcopy(arr)
    sort_arr.sort()
    
    # if the array is already sorted
    if sort_arr == arr:
        print('yes')
        return
    
    # if the array can be sorted
    l = r = -1
    
    # left index
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            l = i
            break
    
    # right index
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            r = i
            break
    
    # check for swap
    temp = deepcopy(arr)
    
    # swap
    temp[l], temp[r] = temp[r], temp[l]
    
    if temp == sort_arr:
        print('yes')
        print('swap', l+1, r+1)
        return
    
    # check for reverse
    temp = deepcopy(arr)
    
    # reverse
    temp = temp[:l] + temp[l:r+1][::-1] + temp[r+1:]
    
    if temp == sort_arr:
        print('yes')
        print('reverse', l+1, r+1)
        return
    
    # array can't be sorted
    print('no')