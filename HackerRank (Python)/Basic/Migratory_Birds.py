def migratoryBirds(arr):
    '''
    migratoryBirds has the following parameter(s):
      - int arr[n]: the types of birds sighted
    Returns an int: the lowest type id of the most frequently sighted birds.
    '''       

    arr.sort()
    birds = {}
    birdId = maxCount = 0
    
    for bird in arr:
        if bird not in birds:
            birds[bird] = 1
        else:
            birds[bird] += 1
            
        if maxCount < birds[bird]:
            maxCount = birds[bird]
            birdId = bird
    
    return birdId