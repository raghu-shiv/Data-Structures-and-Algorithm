def rotateLeft(d, arr):
    '''
    rotateLeft has the following parameters:
      - int d: the amount to rotate by
      - int arr[n]: the array to rotate
    Returns an int[n]: the rotated array.
    '''

    left = arr[:d]
    right = arr[d:]
    newArr = right + left
    return newArr