def countSort(arr):
    '''
    countSort has the following parameter(s):
      - string arr[n][2]: each arr[i] is comprised of two strings, x and s

    Returns nothing. Print the finished array with each element separated by a single space.

    Note: The first element of each arr[i], x, must be cast as an integer to perform the sort.
    '''

    result = [[] for i in range(100)]
    
    # for first half
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
        
    # for second half
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])
        
    # print the results
    for string in result:
        if string:
            print(*string, end=' ')