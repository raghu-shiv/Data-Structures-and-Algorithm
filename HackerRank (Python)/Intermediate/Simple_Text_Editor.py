'''
The editor initially contains an empty string, S. Perform Q operations of the following  types:

1. append(W) - Append string W to the end of S.
2. delete(k) - Delete the last k characters of S.
3. print(k) - Print the kth character of S.
4. undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting  to the state it was in prior to that operation.
'''

stack = []
S = ""
Q = int(input())

for ops in range(Q):
  op = input().split() 

  if op[0] == '1':
    stack.append(S)
    S += op[1]

  elif op[0] == '2':
    stack.append(S)    
    S = S[:-int(op[1])]

  elif op[0] == '3':
    print(S[int(op[1])-1])
    
  elif op[0] == '4':
    S = stack.pop()