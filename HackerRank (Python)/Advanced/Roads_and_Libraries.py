def roadsAndLibraries(n, c_lib, c_road, cities):
    '''
    roadsAndLibraries has the following parameters:
      - int n: integer, the number of cities
      - int c_lib: integer, the cost to build a library
      - int c_road: integer, the cost to repair a road
      - int cities[m][2]: each  contains two integers that represent cities that can be connected by a new road
    Returns an int: the minimal cost.
    '''

    # Create adjacency list for graph connections
    graph = [[] for _ in range(n+1)]
    for x, y in cities:
        # Bi-directional graph 
        graph[x].append(y)
        graph[y].append(x)

    total_min_cost = 0
    visited = [False]*(n+1)

    # Main logic
    for v in range(1, n+1):
        if visited[v] == False:
            # Find number of cities in the subset of graph
            n_cities = getConnectedCities(v, graph, visited)
            # Calculate cost of roads and one library
            cost1 = (n_cities-1)*c_road + c_lib
            # Calculate cost of building libraries in all cities
            cost2 = n_cities*c_lib
            # add the minimum cost to the total
            total_min_cost += min(cost1, cost2)

    return total_min_cost

# Create Depth First Search (DFS) function to find the subset of cities that have possible connections
def getConnectedCities(u, graph, visited):
    visited[u] = True
    n_cities = 1
    for v in graph[u]:
        if visited[v] == False:
            n_cities += getConnectedCities(v, graph, visited)
    return n_cities