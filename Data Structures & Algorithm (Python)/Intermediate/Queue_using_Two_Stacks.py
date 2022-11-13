'''
Implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

(a) 1 x: Enqueue element x into the end of the queue.
(b) 2: Dequeue the element at the front of the queue.
(c) 3: Print the element at the front of the queue.
'''

stack_enqueue = []
stack_dequeue = []

q = int(input())

for i in range(q):
    query = list(input().split())
    
    if query[0] == '1':
        stack_enqueue.append(query[1])
    
    elif query[0] == '2':
        if not stack_dequeue:
            while stack_enqueue:
                stack_dequeue.append(stack_enqueue.pop())
        stack_dequeue.pop()
    
    else:
        if not stack_dequeue:
            while stack_enqueue:
                stack_dequeue.append(stack_enqueue.pop())
        print(stack_dequeue[-1])