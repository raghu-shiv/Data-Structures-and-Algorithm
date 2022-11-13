from heapq import heapify, heappush, heappop

def cookies(k, A):
    '''
    Returns an int: the number of iterations required to increase the sweetness or -1. 

    '''

    heapify(A)
    ops = 0
    
    while A[0] < k and len(A) > 1:
        least_sweet = heappop(A)
        second_least_sweet = heappop(A)
        sweetness = least_sweet + 2*second_least_sweet
        heappush(A, sweetness)
        ops += 1

    return ops if A[0] >= k else -1