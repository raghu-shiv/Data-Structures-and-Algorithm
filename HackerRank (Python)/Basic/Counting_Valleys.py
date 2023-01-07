def countingValleys(steps, path):
    '''
    countingValleys has the following parameter(s):
      - int steps: the number of steps on the hike
      - string path: a string describing the path
    Returns an int: the number of valleys traversed.
    '''

    seaLevel = valleys = 0
    stepValue = {'U':1, 'D':-1}
    
    for step in path:
        seaLevel += stepValue[step]
        if seaLevel==0 and step=='U':
            valleys += 1

    return valleys