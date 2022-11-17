from heapq import heapify, heappush, heappop

def cookies(k, A):
    '''
    cookies has the following parameters:
        - int k: the threshold value
        - int A[n]: an array of sweetness values
    Returns an int: the number of iterations required to increase the sweetness or -1. 
    '''

    heapify(A)
    ops = 0
    
    while A[0] < k and len(A) > 1:
        leastSweet = heappop(A)
        secondLeastSweet = heappop(A)
        newCookie = leastSweet + 2*secondLeastSweet
        heappush(A, newCookie)
        ops += 1

    return ops if A[0] >= k else -1