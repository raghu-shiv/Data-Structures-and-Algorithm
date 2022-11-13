def lilysHomework(arr):
    '''
    The function accepts INTEGER_ARRAY arr[n] as parameter.
    Returns an int: the minimum number of swaps required.
    '''

    swaps = []
    
    # We will iterate thru the sorted and reverse sorted array
    for toggle in [True, False]:
        s = arr.copy()
        sorted_s = sorted(arr, reverse=toggle)
    
        # Initialize a map for the values in the original array with the respective indices
        valMap = {v:i for i,v in enumerate(s)}
        
        # Initialize the swap count
        swap_count = 0

        # Iterate thru the values in original and sorted arrays
        for from_val, to_val in zip(s, sorted_s):
            # if values are equal, skip them
            if from_val == to_val:
                continue

            # For values not equal in both arrays.
            from_idx = valMap[from_val]
            to_idx = valMap[to_val]

            # Swap the values in the original array
            s[from_idx], s[to_idx] = s[to_idx], s[from_idx]
            # Swap the indices in the value map
            valMap[from_val], valMap[to_val] = valMap[to_val], valMap[from_val]
            # Increment the swap count by 1
            swap_count += 1
        
        swaps.append(swap_count)
    
    return min(swaps)