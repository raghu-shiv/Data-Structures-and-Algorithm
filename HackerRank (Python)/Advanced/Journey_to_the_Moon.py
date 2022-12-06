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

    # BFS to traverse, get the number of each group: group[]
    visited = [False] * n
    group = []

    for i in range(n):
        if visited[i] == False:
            st = [i]
            visited[i] = True
            a = 1
            while len(st) > 0:
                start = st.pop()
                # add all its neighbours
                for neigh in graph[start]:
                    if visited[neigh] == False:
                        visited[neigh] = True
                        st.append(neigh)
                        a += 1
            group.append(a)

    # choose from group A and other groups (by presum) and sum all possible group A to avaoid repetition, only joins with the groups with index < index_A

    pairs = 0
    presum = []
    for i in range(len(group)):
        pairs += group[i]
        presum.append(pairs)

    pairs = 0
    for i in reversed(range(1, len(group))):
        pairs += group[i] * presum[i-1]
    return pairs