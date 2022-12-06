import sys

def minimumLoss(price):
    '''
    minimumLoss has the following parameter(s):
      - int price[n]: home prices at each year
    
    Returns an int: the minimum loss possible
    '''

    prices = {}
    
    for i, p in enumerate(price):
        prices[p] = i
    
    price.sort()
    
    minVal = sys.maxsize
    for i in range(1, len(price)):
        if prices[price[i-1]] > prices[price[i]]:
            minVal = min(minVal, price[i] - price[i-1])
            
    return minVal