def marsExploration(s):
    '''
    marsExploration has the following parameter(s):
      - string s: the string as received on Earth
    Returns an int: the number of letters changed during transmission.
    '''

    changedLetters = 0
    
    for i in range(0, len(s), 3):
        if s[i] != 'S': changedLetters += 1
        if s[i+1] != 'O': changedLetters += 1
        if s[i+2] != 'S': changedLetters += 1

    return changedLetters