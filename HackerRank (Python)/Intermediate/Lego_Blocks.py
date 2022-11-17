def legoBlocks(n, m):
    '''
    The function accepts following parameters:
      1. INTEGER n: the height of the wall.
      2. INTEGER m: the width of the wall.
    Returns an int: the number of valid wall formations modulo (10^9 + 7). 
    '''

    mod = 10**9+7

    # Step 1: O(m)
    # We have combinations to make a wall of single row of width, m ranging from 1 to 4.
    singleRowCombo = [1, 2, 4, 8]
  
    # For m >= 4, the row combination is the sum of the row combinations for the last 4 widths:
    for i in range(4, m):
        singleRowCombo.append(sum(singleRowCombo[-4:])%mod)
  
    # Step 2: O(m)
    # Total combinations of the wall is calculated as rows of varying widths to the power of height, n (row^n):
    totalCombo = [(row**n)%mod for row in singleRowCombo]

    # Step 3: O(m^2)
    # We will initialize an array for valid combinations.
    # For m=1, valid combination is 1 for any height of the wall.
    validCombo = [1] 
  
    # Here, we will iterate through the width of the wall to check a straight vertical break across all rows of blocks.
    # For each vertical break, we have to separate sections of the wall.
    # Hence, the invalid combinations for this vertical break will be calculated as the total combinations of section A times the valid combinations of section B.
    # At last, add the invalid combinations for all the vertical breaks across the wall from left to right.
    for i in range(1, m):
        invalidCombo = sum([total*valid for total, valid in zip(totalCombo[:i], validCombo[::-1])])
        validCombo.append((totalCombo[i]-invalidCombo)%mod)

    return validCombo[-1]