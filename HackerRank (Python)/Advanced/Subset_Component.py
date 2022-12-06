def findConnectedComponents(d):
    '''
    findConnectedComponents has the following parameters:
      - int d[n]: an array of integers
    
    Returns an int: the sum of the number of connected components for all subsets of d.
    '''

    count = 0
    # generate powerset
    p = 1 << len(d)

    for i in range(p):
        # get current subset of powerset using bits of s to indicate if the ith element of d is in the subset
        subset = [n for idx, n in enumerate(d) if 1<<idx & i!=0]
        # print(i, 'subset', subset)

        vertices = connectedCount = 0

        for s in subset:
            # skip if power of 2 or zero, won't contribute to connections
            if (formatBin(s).count('1') - 1 if s else 0) < 1:
                continue
            # check if new connected component has been found
            if not vertices & s:
                # print('new connected component', formatBin(vertices), formatBin(s))
                connectedCount += 1
            # update running vertices with connections
            vertices |= s
        # get vertex count that contribute to connections
        vertexCount = formatBin(vertices).count('1')

        # print('vertices', formatBin(vertices), 'connectedCount', connectedCount, 'vertexCount', vertexCount)

        # update count
        subsetCount = 64 - vertexCount + connectedCount
        count += subsetCount
        # print(subsetCount)
    return count

def formatBin(s): return '{:b}'.format(s)