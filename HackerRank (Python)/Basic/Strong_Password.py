def minimumNumber(n, password):
    '''
    minimumNumber has the following parameters:
      - int n: the length of the password
      - string password: the password to test
    Returns an int: the minimum number of characters to add.
    '''

    splChar = '!@#$%^&*()-+'
    conditions = [0, 0, 0, 0]
    
    for char in password:
        if char.isdigit():
            conditions[0] = 1
        elif char.islower():
            conditions[1] = 1
        elif char.isupper():
            conditions[2] = 1
        elif char in splChar:
            conditions[3] = 1
    
    return max(6-n, 4-sum(conditions))