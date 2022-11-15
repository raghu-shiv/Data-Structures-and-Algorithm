def minimumBribes(q):
    '''
    minimumBribes has the following parameter(s):
      - int q[n]: the positions of the people after all bribes
    No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
    '''

    bribes = 0
    q = [x-1 for x in q]
    
    for i,x in enumerate(q):
        if x-i > 2:
            print("Too chaotic")
            return
            
        for j in range(max(x-1, 0), i):
            if q[j] > x:
                bribes += 1
    print(bribes)