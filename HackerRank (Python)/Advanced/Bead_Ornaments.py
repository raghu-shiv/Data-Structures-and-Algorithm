from operator import mul
from functools import reduce

def beadOrnaments(b):
    '''
    beadOrnaments has the following parameters: 
      - int b[n]: the number of beads of each color
    
    Returns an int: the number of arrangements modulo (10^9 + 7).
    '''

    mod = 10**9 + 7
    reduced = reduce(mul, map(lambda x: x**(x-1), b), 1)
    sums = sum(b)**(len(b)-2)
    
    return int(reduced*sums) % mod