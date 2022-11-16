def isBalanced(s):
    '''
    isBalanced has the following parameter(s):
      - string s: a string of brackets
    Returns a STRING: either YES or NO.
    '''

    stack = []
    brackets = { '(':')', '{':'}', '[':']' }
    
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if brackets[top] != char:
                    return "NO"
            else:
                return "NO"
    
    return "NO" if stack else "YES"