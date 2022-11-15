def superDigit(n, k):
    '''
    superDigit has the following parameter(s):
      - string n: a string representation of an integer
      - int k: the times to concatenate n to make p
    Returns an int: the super digit of n repeated k times.
    '''

    total = sum(int(d) for d in n)*k
    
    if total%9 == 0:
        return 9
    return total%9