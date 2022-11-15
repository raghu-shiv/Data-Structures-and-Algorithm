def towerBreakers(n, m):
    '''
    towerBreakers has the following paramter(s):
      - int n: the number of towers
      - int m: the height of each tower
    Returns an int: the winner of the game.
    '''

    if n%2 == 0 or m == 1:
        return 2
    else:
        return 1