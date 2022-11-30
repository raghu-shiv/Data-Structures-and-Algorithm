def stockmax(prices):
    '''
    stockmax has the following parameter(s):
      - prices: an array of integers that represent predicted daily stock prices
    Returns an int: the maximum profit achievable.
    '''
    
    prices.reverse()
    n = len(prices)
    maxValue = totalProfit = 0

    for i in range(1, n):
        if prices[i] < prices[maxValue]:
            totalProfit += prices[maxValue] - prices[i]
        else:
            maxValue = i
            
    return totalProfit