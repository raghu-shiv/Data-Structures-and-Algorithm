def truckTour(petrolpumps):
    '''
    The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
    Returns an INTEGER, which will be the smallest index of the petrol pump from which we can start the tour.
    '''

    petrolInTruck = start = 0
    N = len(petrolpumps)

    amount, distance = zip(*petrolpumps)
    
    for i in range(N):
        remainingPetrol = amount[i] - distance[i]
        petrolInTruck += remainingPetrol
        
        if petrolInTruck < 0: 
            start = i + 1
            petrolInTruck = 0
    
    return start