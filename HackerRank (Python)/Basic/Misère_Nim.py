from functools import reduce

def misereNim(s):
    '''
    misereNim has the following parameters:
      - int s[n]: the number of stones in each pile
    Returns a string: either First or Second.
    '''

    if set(s)=={1} and n%2==1:
        return "Second"
    elif set(s)=={1} and n%2==0:
        return "First"
    elif reduce((lambda x,y:x^y), s):
        return "First"
    else:
        return "Second"