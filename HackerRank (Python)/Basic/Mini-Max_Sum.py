def miniMaxSum(arr):
    '''
    miniMaxSum has the following parameter(s):
      - arr: an array of 5 integers
    Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.
    '''

    arr_sorted = sorted(arr)
        
    min_sum = sum(arr_sorted[:4])
    max_sum = sum(arr_sorted[-4:])

    print(f"{min_sum} {max_sum}")