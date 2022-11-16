def icecreamParlor(m, arr):
    '''
    icecreamParlor has the following parameter(s):
      1. int m: the amount of money they have to spend
      2. int cost[n]: the cost of each flavor of ice cream
    Returns an int[2]: the indices of the prices of the two flavors they buy, sorted ascending.
    '''

    for flavorA, costA in enumerate(arr, 1):
        for flavorB, costB in enumerate(arr, 1):
            if flavorA != flavorB and costA+costB == m:
                return [flavorA, flavorB]