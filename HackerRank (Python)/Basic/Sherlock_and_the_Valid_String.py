def isValid(s):
    '''
    isValid has the following parameter(s):
      - string s: a string
    Returns a string: either YES or NO
    '''

    if len(s)==1:
        return "YES"
    
    f_dict = {}
    for letter in s:
        if letter not in f_dict.keys():
            f_dict[letter] = 1
        else:
            f_dict[letter] += 1
            
    f_arr = []
    for letter in f_dict.keys():
        f_arr.append(f_dict[letter])
    f_arr.sort()
    
    n = len(f_arr)
    
    if(f_arr[n-2]+1==f_arr[n-1] and f_arr[0]==f_arr[n-2]):
        return "YES"
    if(f_arr[0]==f_arr[n-1]):
        return "YES"
    if(f_arr[0]==1 and f_arr[1]==f_arr[n-1]):
        return "YES"
    return "NO"