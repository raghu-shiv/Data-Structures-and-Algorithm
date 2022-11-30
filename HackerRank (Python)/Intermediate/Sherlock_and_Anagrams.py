def sherlockAndAnagrams(s):
    '''
    sherlockAndAnagrams has the following parameter(s):
      - string s: a string
    Returns an int: the number of unordered anagrammatic pairs of substrings in s.
    '''

    pairs = 0
    hashMap = {}
    n = len(s)

    for i in range(1, n+1):
        for j in range(n-i+1):
            subString = str(''.join(sorted(s[j:j+i])))
            
            if subString in hashMap:        
                pairs += hashMap[subString]
                hashMap[subString] += 1
            else:
                hashMap[subString] = 1
        
    return pairs