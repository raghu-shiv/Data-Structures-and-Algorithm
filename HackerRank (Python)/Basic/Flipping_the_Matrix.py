def flippingMatrix(matrix):
    '''
    flippingMatrix has the following parameters:
      - int matrix[2n][2n]: a 2-dimensional array of integers
    Returns an int: the maximum sum possible.
    '''

    l = len(matrix)
    maxSum = 0

    for i in range(l//2):
        for j in range(l//2):
            maxSum += max(matrix[i][j], matrix[i][l-j-1], matrix[l-i-1][j], matrix[l-i-1][l-j-1])
    
    return maxSum