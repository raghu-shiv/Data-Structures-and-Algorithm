def pangrams(s):
    '''
    pangrams has the following parameter(s):
      - string s: a string to test
    Returns a string: either pangram or not pangram
    '''

    unique_set = set(s.lower().replace(" ", ""))
    
    if len(unique_set) == 26:
        return "pangram"
    return "not pangram"