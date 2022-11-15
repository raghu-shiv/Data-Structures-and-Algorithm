def gridChallenge(grid):
    '''
    gridChallenge has the following parameter(s):
      - string grid[n]: an array of strings
    Returns a string: either YES or NO.
    '''

    sorted_grid = [sorted(string) for string in grid]
    
    for m in range(len(grid[0])):
        for n in range(len(grid)-1):
            if sorted_grid[n][m] > sorted_grid[n+1][m]:
                return "NO"
    return "YES"