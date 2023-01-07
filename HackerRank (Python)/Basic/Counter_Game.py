import math

def counterGame(n):
    '''
    counterGame has the following parameter(s):
      - int n: the initial game counter value

    Returns a string: either Richard or Louise.   
    '''

    if n == 1: 
        return "Richard"
    
    count = 1
    
    while n > 1:
        x = math.log2(n)
        if x.is_integer():
            n = n//2
        else:
            n = n - math.pow(2, int(x))
        count += 1   
    
    if count%2 == 0:
        return "Louise"

    return "Richard"