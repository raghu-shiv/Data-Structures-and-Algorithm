def bigSorting(unsorted):
    '''
    bigSorting has the following parameter(s):
      - string unsorted[n]: an unsorted array of integers as strings.
    Returns a STRING_ARRAY, the array sorted in numerical order.
    '''

    def sortBy(x):
        return len(x), x
    
    unsorted.sort(key=sortBy)
    return unsorted