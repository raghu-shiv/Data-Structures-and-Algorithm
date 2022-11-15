def bomberMan(n, grid):
    '''
    bomberMan has the following parameter(s):
      - int n: the number of seconds to simulate
      - string grid[r]: an array of strings that represents the grid
    Returns a string[r]: n array of strings that represent the grid in its final state.
    '''

    if n == 1:
        return grid
    if n%2 == 0:
        return ['O'*c for i in range(r)]
    
    n = n//2
    
    for alt_states in range((n+1)%2 + 1):
        new_grid = [['O']*c for i in range(r)]
        
        def detonate(x, y):
            if 0<=x<r and 0<=y<c:
                new_grid[x][y] = '.'
        
        xi = [0, 0, 0, 1, -1]
        yi = [0, 1, -1, 0, 0]
        
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    for i,j in zip(xi, yi):
                        detonate(x+i, y+j)
        
        grid = new_grid
    return ["".join(x) for x in grid]