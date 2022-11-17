def maxSubarray(arr):
    '''
    maxSubarray has the following parameter(s):
      - int arr[n]: an array of integers
    Returns int[2]: the maximum subarray and subsequence sums.
    '''
  
    maxSubarr = maxSubseq = curMax = arr[0]
    
    for i in range(1, len(arr)):
        # for max subarray sum
        curNum = arr[i]
        curMax = max(curNum, curNum+curMax)
        maxSubarr = max(maxSubarr, curMax)
        
        # for max subsequence sum
        if maxSubseq < 0:
            maxSubseq = max(maxSubseq, curNum)
        else:
            maxSubseq += max(curNum, 0)
            
    return maxSubarr, maxSubseq