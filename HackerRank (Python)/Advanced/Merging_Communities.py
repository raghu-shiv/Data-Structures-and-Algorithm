import sys

q = [line.strip() for line in sys.stdin]
dp = {}

for i in range(1, len(q)):
    line = q[i]
    
    if line[0] == 'M':
        [i, j] = line[2:].split(' ')
        if i not in dp:
            dp[i] = [i]
        if j not in dp:
            dp[j] = [j]
        if dp[i] == dp[j]:
            continue
        
        [bigger, smaller] = [dp[i], dp[j]] if len(dp[i]) >= len(dp[j]) else [dp[j], dp[i]]
        
        for k in smaller:
            bigger.append(k)
            dp[k] = bigger
    
    elif line[0] == 'Q':
        n = line[2:]
        print(len(dp[n]) if n in dp else 1)