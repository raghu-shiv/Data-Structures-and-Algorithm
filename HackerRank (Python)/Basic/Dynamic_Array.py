def dynamicArray(n, queries):
    '''
    dynamicArray has the following parameters:
      - int n: the number of empty arrays to initialize in arr
      - string queries[q]: query strings that contain 3 space-separated integers
    Returns an int[]: the results of each type 2 query in the order they are presented.
    '''

    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    
    for query in queries:
        if query[0] == 1:
            idx = (query[1]^lastAnswer)%n
            arr[idx].append(query[2])
        elif query[0] == 2:
            idx = (query[1]^lastAnswer)%n
            lastAnswer = arr[idx][query[2]%len(arr[idx])]
            answers.append(lastAnswer)
    return answers