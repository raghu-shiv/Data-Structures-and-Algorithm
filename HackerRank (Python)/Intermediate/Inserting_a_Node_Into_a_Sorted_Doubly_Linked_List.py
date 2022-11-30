def sortedInsert(llist, data):
    '''
    sortedInsert has two parameters:
      - DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list
      - int data: An integer denoting the value of the data field for the DoublyLinkedListNode you must insert into the list.

    Returns a DoublyLinkedListNode pointer: a reference to the head of the list.
    '''

    newNode = DoublyLinkedListNode(data)
    head, prev = llist, None

    while llist and llist.data < data:
        prev, llist = llist, llist.next
        
    # Insert newNode between prev and llist
    newNode.prev = prev
    newNode.next = llist

    if llist: llist.prev = newNode
    if prev: prev.next = newNode
    else: head = newNode
    
    return head