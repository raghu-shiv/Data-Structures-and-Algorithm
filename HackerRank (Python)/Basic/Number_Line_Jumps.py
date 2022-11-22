def kangaroo(x1, v1, x2, v2):
    '''
    kangaroo has the following parameter(s):
      - int x1, int v1: starting position and jump distance for kangaroo 1
      - int x2, int v2: starting position and jump distance for kangaroo 2
    Returns a string: either YES or NO.
    '''

    if v1 <= v2:
        return "NO"

    return 'YES' if (x1-x2)%(v2-v1) == 0 else "NO"
