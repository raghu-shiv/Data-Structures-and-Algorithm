from collections import deque

def minimumMoves(grid, startX, startY, goalX, goalY):
    '''
    minimumMoves has the following parameter(s):
      - string grid[n]: an array of strings that represent the rows of the grid
      - int startX: starting X coordinate
      - int startY: starting Y coordinate
      - int goalX: ending X coordinate
      - int goalY: ending Y coordinate
    Returns an int: the minimum moves to reach the goal.
    '''

    numOfMoves = 0
    visited = set() 
    queue = deque([[startX, startY, numOfMoves]])
    moves = [[1,0], [-1,0], [0,1], [0,-1]]

    while queue:
        pathX, pathY, numOfMoves = queue.popleft()
        numOfMoves += 1

        for xi, yi in moves:
            x, y = pathX, pathY

            while True:
                x, y = x+xi, y+yi

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.':
                    if x == goalX and y == goalY:
                        return numOfMoves
                    elif (x, y) not in visited:
                        visited.add((x, y))
                        queue.append([x, y, numOfMoves])
                else:
                    break
    return -1