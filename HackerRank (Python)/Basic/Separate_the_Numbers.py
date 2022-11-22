def separateNumbers(s):
    '''
    separateNumbers has the following parameter:
      - s: an integer value represented as a string
    
    Returns nothing. If the string is beautiful, print YES x, where x is the first number of the increasing sequence. 
    If there are multiple such values of x, choose the smallest. Otherwise, print NO.    
    '''

    if len(s) == 1: 
        print("NO")
        return
    else:
        # generate integer strings by increment of one
        for i in range(1, len(s)//2 + 1):
            numString = s[:i]
            num = int(numString)
            
            # do operation until it reaches the length
            while len(numString) < len(s):
                num += 1
                numString += str(num)
                
            # check if it is equal
            if numString == s:
                print("YES", s[:i])
                return
        
        print("NO")