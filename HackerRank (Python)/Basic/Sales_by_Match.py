def sockMerchant(n, ar):
    '''
    sockMerchant has the following parameter(s):
      - int n: the number of socks in the pile
      - int ar[n]: the colors of each sock
    Returns an int: the number of pairs
    '''

    colors = set(ar)
    pairs = 0
    
    for color in colors:
        pairs += ar.count(color)//2
    return pairs