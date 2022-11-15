def birthday(s, d, m):
    '''
    birthday has the following parameter(s):
      - int s[n]: the numbers on each of the squares of chocolate
      - int d: Ron's birth day
      - int m: Ron's birth month
    Returns an int: the number of ways the bar can be divided.
    '''

    numOfWays = 0

    for i in range(len(s)):
        if d == sum(s[i:i+m]):
            numOfWays += 1
            
    return numOfWays