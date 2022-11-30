def fibonacciModified(t1, t2, n):
    '''
    fibonacciModified has the following parameter(s):
      - int t1: an integer
      - int t2: an integer
      - int n: the iteration to report
    Returns an int: the nth number in the sequence.
    '''

    fibSeq = [t1, t2]
    
    for i in range(n):
        nextNum = fibSeq[i] + fibSeq[i+1]**2
        fibSeq.append(nextNum)
    
    return fibSeq[-3]