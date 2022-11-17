def highestValuePalindrome(s, n, k):
    '''
    The function accepts following parameters:
      1. STRING s, n-digit string of numbers.
      2. INTEGER n, the number of digits in the number. 
      3. INTEGER k, the maximum number of changes allowed.
    Returns a string: a string representation of the highest value achievable or -1.
    '''

    s = list(s)
    
    # To identify changes at a particular index
    mark = [0]*n
    
    # Change the digits to palindrome
    l = 0   # left index
    r = n-1 # right index
    
    while l <= r:
        if s[l] != s[r]:
            if s[l] > s[r]:
                s[r] = s[l]
                mark[r] = 1
            else:
                s[l] = s[r]
                mark[l] = 1
            k -= 1
        l += 1
        r -= 1
    
    if k < 0:
        return '-1'
    
    # Maximize the digits
    l, r = 0, n-1
    
    while l <= r:
        if l==r and k>=1:
            s[l] = '9'
            break
        
        elif s[l] < '9':
            # if there were no changes before
            if mark[l]==0 and mark[r]==0 and k>=2:
                s[l] = s[r] = '9'
                k -= 2
            # if the string was changed before
            elif (mark[l]==1 or mark[r]==1) and k>=1:
                s[l] = s[r] = '9'
                k -= 1
        
        l += 1
        r -= 1
        
    return "".join(s)