from heapq import heappush, heappop

qHeap1 = []
dataset = set()

Q = int(input())
for i in range(Q):
    cmd = input().split()
    q = list(map(int, cmd))
    
    # Insertion
    if q[0] == 1:
        heappush(qHeap1, q[1])
        dataset.add(q[1])
    # Deletion
    elif q[0] == 2:
        dataset.discard(q[1])
    # Print the minimum value
    elif q[0] == 3:
        while qHeap1[0] not in dataset:
            heappop(qHeap1)
        print(qHeap1[0])