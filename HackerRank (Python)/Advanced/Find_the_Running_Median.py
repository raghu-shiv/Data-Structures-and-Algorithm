from heapq import heappush, heappop

def runningMedian(a):
    '''
    runningMedian has the following parameters:
      - int a[n]: an array of integers
    
    Returns a float[n]: the median of the array after each insertion, modify the print statement in main to get proper formatting.  
    '''

    # initialize the variables
    minHeap, maxHeap, median = [], [], []
     
    for num in a:
        # insert the element
        addNum(num, minHeap, maxHeap)
        # rebalancing the heaps
        balance(minHeap, maxHeap)
        # find the median
        median.append(getMedian(minHeap, maxHeap))
        
    return median

def addNum(num, minHeap, maxHeap):
    if not maxHeap or num < -maxHeap[0]:
        heappush(maxHeap, -num)
    else:
        heappush(minHeap, num)

def balance(minHeap, maxHeap):
    if len(minHeap) - len(maxHeap) >= 2:
        heappush(maxHeap, -heappop(minHeap))
    if len(maxHeap) - len(minHeap) >= 2:
        heappush(minHeap, -heappop(maxHeap))

def getMedian(minHeap, maxHeap):
    if len(minHeap) == len(maxHeap):
        return (minHeap[0] - maxHeap[0]) / 2
    elif len(minHeap) > len(maxHeap):
        return float(minHeap[0])
    else:
        return float(-maxHeap[0])