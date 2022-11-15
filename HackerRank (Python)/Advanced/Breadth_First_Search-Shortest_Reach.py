from collections import deque

def bfs(n, m, edges, s):
    '''
    bfs has the following parameter(s):
        - int n: the number of nodes
        - int m: the number of edges
        - int edges[m][2]: start and end nodes for edges
        - int s: the node to start traversals from
    Returns an int[n-1]: the distances to nodes in increasing node number order, not including the start node (-1 if a node is not reachable).    
    '''
    
    graph = [[] for _ in range(n+1)]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    distances = [-1]*(n+1)
    distances[s] = 0
    visited = [False]*(n+1)
    visited[s] = True
    queue = deque([(s,0)])
    
    while queue:
        node, dist = queue.popleft()
        
        for i in graph[node]:
            if visited[i] == False:
                distances[i] = dist + 6
                visited[i] = True
                queue.append((i, dist+6))
    
    distances.remove(0)
    
    return distances[1:]