# Note: For this exercise, always return a frequency array with 100 elements. 

def countingSort(arr):
    '''
    countingSort has the following parameter(s):
      - arr[n]: an array of integers
    Returns an int[100]: a frequency array.
    '''

    freqArray = [0 for _ in range(100)]
    maxRange = max(arr)
    
    for i in range(maxRange+1):
        freqArray[i] = arr.count(i)
        
    return freqArray  