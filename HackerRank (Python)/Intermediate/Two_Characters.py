def alternate(s):
    '''
    alternate has the following parameter(s):
      - string s: a string

    Returns an int: the length of the longest valid string, or 0 if there are none.
    '''

    if len(s)==1 or len(s)==0 or len(set(s))==1: return 0

    maxNum = count = 0
    # produces unique chars
    alphabets = list(set(s))
    
    # find all combos of chars
    for i in range(len(alphabets)):
        for j in range(i+1, len(alphabets)):
            l = [alphabets[i], alphabets[j]]
            
            # checks which char comes first in the string
            if s.index(alphabets[i]) < s.index(alphabets[j]):
                idx = 0
            else:
                idx = 1
            
            # check for alternate chars and increment count
            for char in s:
                if char in l:
                    if char == l[idx]:
                        count += 1
                        # flip the index
                        idx = idx^1
                    else:
                        count = 0
                        break
            # store the max length 
            maxNum = max(maxNum, count)
            count = 0
            
    return maxNum