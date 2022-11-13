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
  q1, q2 = op[0], op[1]

  if q1 == '1':
    stack.append(S)
    S += q2
  elif q1 == '2':
    stack.append(S)    
    S = S[:-int(q2)]
  elif q1 == '3':
    print(S[int(q2)-1])
  elif q1 == '4':
    S = stack.pop()