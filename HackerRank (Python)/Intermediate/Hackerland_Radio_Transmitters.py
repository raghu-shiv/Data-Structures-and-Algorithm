def hackerlandRadioTransmitters(x, k):
    '''
    hackerlandRadioTransmitters has the following parameter(s):
        - int x[n]: the locations of houses
        - int k: the effective range of a transmitter
    Returns an int: the minimum number of transmitters to install.
    '''

    x.sort()
    minTransmitters = 0
    
    i = 0
    while i < n:
        # For houses in the left side of the transmitter
        leftRange = x[i] + k
        while i < n and x[i] <= leftRange:
            i += 1
            
        # Install transmitter and stop at that location
        i -= 1
        minTransmitters += 1
        
        # For houses in the right side of the transmitter        
        rightRange = x[i] + k
        while i < n and x[i] <= rightRange:
            i += 1
    
    return minTransmitters