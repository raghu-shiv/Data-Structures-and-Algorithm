def getWays(n, c):
    '''
    getWays has the following parameter(s):
      - int n: the amount to make change for
      - int c[m]: the available coin denominations

    Returns an int: the number of ways to make change.
    '''

    numOfWays = [1] + [0]*n
    
    for coin in c:
        for i in range(coin, n+1):
            numOfWays[i] += numOfWays[i-coin]
            
    return numOfWays[n]