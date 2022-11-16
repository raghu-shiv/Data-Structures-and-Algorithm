def reverse(llist):
    '''
    Returns a DoublyLinkedListNode: a reference to the head of the reversed list.
    '''

    head = llist

    if(head == None): return None
    if(head.next == None): return head
    
    while head.next != None:
        head.next, head.prev, head = head.prev, head.next, head.next
    
    head.next, head.prev = head.prev, None

    return head