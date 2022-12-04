import math 

n, m = map(int, input().split())

# create distance graph
dist_graph = [[math.inf for i in range(n+1)] for j in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    # update weights in the distance graph
    dist_graph[u][v] = w

# update diagonal of the distance matrix to 0 (node to itself)
for i in range(1, n+1):
    dist_graph[i][i] = 0

# Floyd Warshall Algorithm
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # update minimum distance
            dist_graph[i][j] = min(dist_graph[i][j], dist_graph[i][k] + dist_graph[k][j])

q = int(input())

for _ in range(q):
    x, y = map(int, input().split())

    print(-1 if dist_graph[x][y]==math.inf else dist_graph[x][y])