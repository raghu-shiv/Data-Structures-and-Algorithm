import sys
sys.setrecursionlimit(10**4)

def journeyToMoon(n, astronaut):
    '''
    journeyToMoon has the following parameter(s):
      - int n: the number of astronauts
      - int astronaut[p][2]: each element astronaut[i] is a 2 element array that represents the ID's of two astronauts from the same country
    
    Returns an int: the number of valid pairs.
    '''

    # create adjacency list for graph edges
    graph = [[] for _ in range(n)]
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    # calculate total pairs     
    pairs = n * (n-1) // 2
    
    # main logic
    for i in range(n):
        if visited[i] == False:
            # no. of astronauts from the same country
            n_astronauts = getCompatriot(i, graph, visited)
            # remove possible combinations from the same country
            pairs -= n_astronauts * (n_astronauts-1) // 2
    
    return pairs    

# create DFS function to find no. of astronauts from the same country (subset)
def getCompatriot(u, graph, visited):
    visited[u] = True
    astronauts = 1  # astronauts = vertices
    for v in graph[u]:
        if visited[v] == False:
            astronauts += getCompatriot(v, graph, visited)
    return astronauts
    
