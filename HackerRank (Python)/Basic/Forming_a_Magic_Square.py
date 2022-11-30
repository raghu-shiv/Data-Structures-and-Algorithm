import sys

def formingMagicSquare(s):
    '''
    formingMagicSquare has the following parameter(s):
      - int s[3][3]: a 3x3 array of integers
    Returns an int: the minimal total cost of converting the input square to a magic square.
    '''

    s = sum(s, [])

    magicMatrices = [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8], [8,3,4,1,5,9,6,7,2], [4,3,8,9,5,1,2,7,6], [6,7,2,1,5,9,8,3,4], [2,7,6,9,5,1,4,3,8]]
    
    minCost = sys.maxsize
    
    for magic in magicMatrices:
        cost = 0
        for i,j in zip(s,magic):
            cost += abs(i-j)
        minCost = min(minCost, cost)
    return minCost