def permutationGame(arr):
    '''
    permutationGame has the following parameter:
      - int arr[n]: the starting permutation
    Returns a string: either Alice or Bob.
    '''

    isIncreasing = lambda arr: all([arr[i] < arr[i+1] for i in range(len(arr)-1)])
    
    memo = {}
    
    def findWinner(arr):
        key = tuple(arr)

        if key in memo: return memo[key]
        if isIncreasing(arr): memo[key] = True; return True
    
        for idx in range(len(arr)):
            if findWinner(arr[:idx] + arr[idx+1:]):
                memo[key] = False; return False
        memo[key] = True; return True
    
    return 'Bob' if findWinner(arr) else 'Alice'