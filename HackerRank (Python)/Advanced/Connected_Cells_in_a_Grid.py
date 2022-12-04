def connectedCell(matrix):
    '''
    connectedCell has the following parameter(s):
      - int matrix[n][m]: matrix[i] represents the ith row of the matrix

    Returns an int: the area of the largest region.
    '''

    maxCells = 0

    for i in range(n):
        for j in range(m):
            maxCells = max(maxCells, helper(i, j, matrix, 0))
    
    return maxCells

def helper(i, j, matrix, count):
    '''
    helper function to check the possible connection between cells.
    Returns an int: the total number of cells connected.
    '''

    # coordinates for traversing the matrices
    xi = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    yi = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    # return if not 1
    if matrix[i][j] != 1: return count

    # mark the cell as visited by placing 9
    count += 1
    matrix[i][j] = 9

    for x, y in zip(xi, yi):
        if 0<=(i+x)<n and 0<=(j+y)<m:
            count = max(count, helper(i+x, j+y, matrix, count))
    
    return count