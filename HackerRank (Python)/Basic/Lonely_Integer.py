def lonelyinteger(a):
    '''
    lonelyinteger has the following parameter(s):
      - int a[n]: an array of integers
    Returns an int: the element that occurs only once.
    '''

    if len(a) == 1:
        return a[0]
    
    for num in a:
        if a.count(num) == 1:
            return num