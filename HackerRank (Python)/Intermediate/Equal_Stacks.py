def equalStacks(h1, h2, h3):
    """
    Returns int: the height of the stacks when they are equalized.
    Note: An empty stack is still a stack.
    """
  
    heights_arr = [h1, h2, h3]
    sums = [sum(heights) for heights in heights_arr]
    
    while True:
        max_sum = max(sums)
        min_sum = min(sums)
        
        if max_sum == min_sum:
            break
        for i in range(len(sums)):
            if sums[i] > min_sum:
                sums[i] -= heights_arr[i].pop(0)
                                
    return sums[0]