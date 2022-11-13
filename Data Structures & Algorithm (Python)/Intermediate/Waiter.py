def waiter(number, q):
  '''
  Returns an int[n]: the numbers on the plates after processing.
  '''

  def isPrime(n):
    '''
    Returns True if a number is prime, else returns False.
    '''
    for i in range(2, n):
      if n%i == 0:
        return False
    return True
  
  def getPrimes(N):
    '''
    Generate first N prime numbers
    '''
    num=2
    while N:
      if isPrime(num):
        yield num
        N-=1
      num+=1
    return

  answers, A, B = [], [], []
  primes = [p for p in getPrimes(q)]
    
  for i in range(q):
    while(number):
      popped = number.pop()
      if popped % primes[i] == 0:
        B.append(popped)
      else:
        A.append(popped)
        
    while(B):
      answers.append(B.pop())
        
    number = A
    A = []
    
  while(number):
    answers.append(number.pop())
    
  return answers