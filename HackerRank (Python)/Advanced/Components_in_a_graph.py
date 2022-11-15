def dfs(i, graph, visited):
    queue = [i]
    item = 0
    res = 0
    
    while item < len(queue):
        i = queue[item]
        item += 1
        
        if visited[i]: continue
        visited[i] = True
        res += 1
        
        for j in graph[i]:
            if visited[j] == False:
                queue.append(j)
    return res
    
def componentsInGraph(gb):
    '''
    connectedComponents has the following parameter(s):
        - int bg[n][2]: a 2-d array of integers that represent node ends of graph edges
    Returns an int[2]: an array with 2 integers, the smallest and largest component sizes.
    '''

    graph = [[] for _ in range(2*n)]
    
    for u, v in gb:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
        
    visited = [False]*(2*n)
    res_min = 1000000000000000
    res_max = -1
    
    for i in range(2*n):
        if visited[i] == False:
            vertices = dfs(i, graph, visited)
            
            if vertices >= 2:
                res_min = min(res_min, vertices)
                res_max = max(res_max, vertices)
                
    return res_min, res_max