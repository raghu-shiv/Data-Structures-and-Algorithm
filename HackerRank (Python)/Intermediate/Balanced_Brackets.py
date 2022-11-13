def isBalanced(s):
  '''
  The function accepts STRING s as parameter.
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