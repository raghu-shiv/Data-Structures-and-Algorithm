def pylons(k, arr):
    '''
    pylons has the following parameter(s):
      - int k: the distribution range
      - int arr[n]: each city's suitability as a building site
    Returns an int: the minimum number of plants required or -1.
    '''

    powPlant = i = 0
    cp = i+k-1
    
    while i < n:
        if arr[cp] == 1:
            powPlant += 1
            
            i = cp+k
            cp = i+k-1
            if cp >= n:
                cp = n-1
        
        else:
            cp -= 1
            if cp < i-k+1 or cp < 0:
                return -1
                
    return powPlant