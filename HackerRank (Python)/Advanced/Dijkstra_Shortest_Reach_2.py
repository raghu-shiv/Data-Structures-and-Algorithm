import sys
from heapq import heappush, heappop
from collections import defaultdict

def shortestReach(n, edges, s):
    '''
    shortestReach has the following parameter(s):
      - n: the number of nodes in the graph.
      - edges: a 2D array of integers where each edges[i] consists of three integers that represent the start and end nodes of an edge, followed by its length.
      - s: the start node number.

      Returns an INTEGER_ARRAY: the lengths of the shortest paths from the starting node to all other nodes in the graph.
    '''

    # Initialization of adjacency list
    graph = defaultdict(list)
    
    for (u, v), r in edges.items():
        graph[u].append((r, v))
        graph[v].append((r, u))

    distance = [sys.maxsize] * (n+1)
    visited = [False] * (n+1)

    # Initialize for starting node
    distance[s] = 0
    minHeap = [(0, s)]

    # main logic
    while minHeap:
        d, u = heappop(minHeap)
        if visited[u] == True: continue
        # Update node as visited
        visited[u] = True

        for r, v in graph[u]:
            if visited[v] == False and distance[v] > distance[u] + r:
                # update the minimum distance
                distance[v] = distance[u] + r
                # update the priority queue
                heappush(minHeap, (distance[v], v))
    
    # Delete unnecessary index in distance
    del distance[s]
    del distance[0]

    # Update unreachable nodes as -1
    for i in range(len(distance)):
        if distance[i] == sys.maxsize:
            distance[i] = -1

    return distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        # changed edges to a dict
        edges = dict()
        
        for _ in range(m):
            x, y, r = map(int, input().rstrip().split())
            if (x, y) in edges:
                edges[(x, y)] = min(edges[(x, y)], r)
            elif (y, x) in edges:
                edges[(y, x)] = min(edges[(y, x)], r)
            else:
                edges[(x, y)] = r
                
        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()