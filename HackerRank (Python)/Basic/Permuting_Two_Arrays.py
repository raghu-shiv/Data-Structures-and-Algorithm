def twoArrays(k, A, B):
    '''
    twoArrays has the following parameter(s):
      - int k: an integer
      - int A[n]: an array of integers
      - int B[n]: an array of integers
    Returns a string: either YES or NO.
    '''

    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        if (A[i]+B[i]) < k:
            return "NO"
    return "YES"