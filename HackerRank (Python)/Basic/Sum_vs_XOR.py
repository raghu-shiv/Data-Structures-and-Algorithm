def sumXor(n):
    '''
    sumXor has the following parameter(s):
      - int n: an integer
    Returns an int: the number of values found.
    '''

    binary = bin(n)[2:]
    zeroes = binary.count('0')
    
    if n == 0:
        return 1
    else:
        return 2**zeroes 