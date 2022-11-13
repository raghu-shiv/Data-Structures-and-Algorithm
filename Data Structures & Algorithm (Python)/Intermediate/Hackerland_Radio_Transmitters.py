def hackerlandRadioTransmitters(x, k):
    '''
    Returns an int: the minimum number of transmitters to install.
    '''

    x.sort()
    minTransmitters = 0
    
    i = 0
    while i < n:
        # For houses in the first half of the transmitter
        next_location = x[i] + k
        while i < n and x[i] <= next_location:
            i += 1
            
        # Install transmitter and stop at that location
        i -= 1
        minTransmitters += 1
        
        # For houses in the second half of the transmitter        
        next_location = x[i] + k
        while i < n and x[i] <= next_location:
            i += 1
    
    return minTransmitters