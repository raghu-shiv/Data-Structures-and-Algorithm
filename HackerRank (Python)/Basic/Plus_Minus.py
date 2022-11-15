def plusMinus(arr):
    '''
    plusMinus has the following parameter(s):
      - int arr[n]: an array of integers
    Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.
    '''

    positive = negative = zero = 0
    size = len(arr)
    
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    
    positive_ratio = "{:.6f}".format(positive/size)
    negative_ratio = "{:.6f}".format(negative/size)
    zero_ratio = "{:.6f}".format(zero/size)

    print(f'{positive_ratio}\n{negative_ratio}\n{zero_ratio}')