def cutTheTree(data, edges):
    '''
    cutTheTree has the following parameter(s):
        - int data[n]: an array of integers that represent node values
        - int edges[n-1][2]: an 2 dimensional array of integer pairs where each pair represents nodes connected by the edge
    Returns an int: the minimum achievable absolute difference of tree sums.
    '''

    treeMap = {i:set() for i in range(1, n+1)}
    for u, v in edges:
        treeMap[u].add(v)
        treeMap[v].add(u)
    # print(treeMap)

    nodes = {1}
    depthLevel = 0
    edgeDepth = [0]*(n+1)
    
    while nodes:
        newNodes = set()
        for u in nodes:
            edgeDepth[u] = depthLevel ; newNodes |= treeMap[u]
            for v in treeMap[u]: treeMap[v].remove(u)
        depthLevel += 1 ; nodes = newNodes
        # print(nodes)

    for u in sorted(range(1, n+1), key=lambda x: -edgeDepth[x]):
            data[u-1] += sum(data[v-1] for v in treeMap[u])
    # print(data)
    
    return min(abs(data[0] - 2*data[i]) for i in range(1, n))