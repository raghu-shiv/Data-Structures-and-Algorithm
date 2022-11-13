from collections import deque

def solve(arr, queries):
    '''
    Function has the following parameter(s):
    - int arr[n]: an array of integers.
    - int queries[q]: the lengths of subarrays to query.
    
    Returns an int[q]: the answers to each query
    '''

    answers = []
    
    for d in queries:
        # Initializing the min and max values in the range of d
        minNum = maxNum = max(arr[:d])
        queue = deque(arr[:d])

        i = d
        while i < len(arr):
            # Sliding the window
            queue.append(arr[i])
            popped = queue.popleft()

            # Checking for min and max values
            maxNum = max(maxNum, arr[i]) if popped < maxNum else max(queue)
            minNum = min(minNum, maxNum)

            # Incrementing the index of the window
            i += 1

        answers.append(minNum)

    return answers