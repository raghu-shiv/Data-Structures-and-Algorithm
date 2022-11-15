def diagonalDifference(arr):
    '''
    diagonalDifference takes the following parameter:
      - int arr[n][m]: an array of integers
    Returns an int: the absolute diagonal difference.
    '''

    l = len(arr)
    diagonal_1 = diagonal_2 = 0
    
    for i in range(l):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][l-1-i]
    
    diagonal_diff = abs(diagonal_1 - diagonal_2)
    return diagonal_diff