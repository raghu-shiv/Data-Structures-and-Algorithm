def chiefHopper(arr):
    '''
    chiefHopper has the following parameter(s):
      - int arr[n]: building heights
    Returns an int: the minimum starting botEnergy.
    '''

    energy = 0
    
    for height in arr[::-1]:
        energy = (energy + height + 1) // 2
        # energy = math.ceil((energy + height) / 2)

    return energy