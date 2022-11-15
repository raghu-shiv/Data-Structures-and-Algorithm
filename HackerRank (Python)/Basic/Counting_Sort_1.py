# Note: For this exercise, always return a frequency array with 100 elements. 

def countingSort(arr):
    '''
    countingSort has the following parameter(s):
      - arr[n]: an array of integers
    Returns an int[100]: a frequency array.
    '''

    freq_array = [0]*100
    max_range = max(arr)
    
    for i in range(max_range+1):
        freq_array[i] = arr.count(i)
    return freq_array  