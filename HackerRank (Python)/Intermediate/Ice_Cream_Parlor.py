def icecreamParlor(m, arr):
  '''
  The function accepts following parameters:
    1. INTEGER m
    2. INTEGER_ARRAY arr
  
  Returns an int[2]: the indices of the prices of the two flavors they buy, sorted ascending.
  '''

  for i, cost_i in enumerate(arr, 1):
    for j, cost_j in enumerate(arr, 1):
      if i != j and cost_i + cost_j == m:
        return [i, j]