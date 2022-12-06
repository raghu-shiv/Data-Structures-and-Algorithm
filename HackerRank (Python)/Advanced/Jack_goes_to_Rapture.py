import math

def getCost(g_nodes, g_from, g_to, g_weight):
    '''
    getCost has the following parameters:
      - int g_nodes: the number of stations in the network
      - int g_from[g_edges]: end stations of a bidirectional connection
      - int g_to[g_edges]: g_from[i] is connected to g_to[i] at cost g_weight[i] 
      - int g_weight[g_edges]: the cost of travel between associated stations
    
    Prints an int or string: the cost of the lowest priced route from station 1 to station g_nodes or NO PATH EXISTS. No return value is expected.
    '''

    routes = [[] for _ in range(g_nodes+1)]
    
    for i in range(len(g_from)):
        routes[g_from[i]].append((g_to[i], g_weight[i]))
        routes[g_to[i]].append((g_from[i], g_weight[i]))
        
    fares = [math.inf] * (g_nodes + 1)
    fares[1] = 0
    currStation = set([1])
    
    while len(currStation) > 0:
        nextStation = set()
        for f in currStation:
            for (t, w) in routes[f]:
                altRoute = max(fares[f], w)
                if altRoute < fares[t]:
                    fares[t] = altRoute
                    nextStation.add(t)
        currStation = nextStation
    
    print(fares[g_nodes] if fares[g_nodes] != math.inf else "NO PATH EXISTS")