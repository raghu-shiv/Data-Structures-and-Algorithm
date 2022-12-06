import copy

def hanoi(posts):
    '''
    hanoi has the following parameters:
      - int posts[n]: posts[i] is the location of the disk with radius i 
    
    Returns an int: the minimum moves to reset the game to its initial state.
    '''

    # each step have the equal cost(1), use BFS
    # maximum no. of state = 4^10 = 1048576
    init = tuple(posts)
    goal = [1 for _ in range(len(posts))]
    goal_tup = tuple(goal)
    if init == goal_tup: # special case, checked before
        return 0
    
    # BFS, use list to implement a queue
    queue = [(posts,1,0), (goal,2,0)] # (state,type,length) 
    front = 0 # front included
    visited = {init:(1,0), goal_tup:(2,0)} # (type,length)
    
    while front < len(queue):
        # pop
        (state,t,l) = queue[front]
        front += 1
        if front >= 100000:
            queue = queue[front:]
            front = 0
        # expand--move the top disc for each rod
        top = [100] # means no disc
        for i in range(1,5): # 1--4
            if i in state:
                top.append(state.index(i))
            else:
                top.append(100)
        # try to move
        for s in range(1,5): # from, start
            for e in range(1,5): # to, end
                if s != e and top[s] < top[e]: 
                    newstate = copy.copy(state)
                    newstate[top[s]] = e
                    newtuple = tuple(newstate)
                    if newtuple not in visited:
                        queue.append((newstate, t, l+1))
                        visited[newtuple] = (t, l+1)
                    elif visited[newtuple][0] != t:
                        # print(newtuple, l+1, visited[newtuple][1])
                        return l+1+visited[newtuple][1]

    return -1