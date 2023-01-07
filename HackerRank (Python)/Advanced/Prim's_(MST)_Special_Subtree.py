import sys

def prims(n, edges, start):
    '''
    prims has the following parameter(s):
      - int n: the number of nodes in the graph
      - int edges[m][3]: each element contains three integers, two nodes numbers that are connected and the weight of that edge
      - int start: the number of the starting node
      
    Returns an int: the minimum weight to connect all nodes in the graph.
    '''
    
    # create adjacency matrix
    graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    # assign weights for the edges
    for u, v, w in edges:
        # bi-directional graph
        graph[u][v] = w
        graph[v][u] = w
    
    visited = [False] * (n+1)
    weights = [sys.maxsize] * (n+1)
    
    weights[start] = 0
    
    for _ in range(1, n+1):
        x = findMinIndex(weights, visited)
        visited[x] = True
        
        for y in range(1, n+1):
            # check if the edge has minimum weight and update
            if graph[x][y] >= 0 and visited[y] == False and weights[y] > graph[x][y]:
                weights[y] = graph[x][y]
    
    return sum(weights[1:])

def findMinIndex(weights, visited):
    '''
    Returns node with minimum weight.
    '''

    minWeight = sys.maxsize

    for i in range(1, len(weights)):
        if weights[i] < minWeight and visited[i] == False:
            minWeight = weights[i]
            minIndex = i

    return minIndex