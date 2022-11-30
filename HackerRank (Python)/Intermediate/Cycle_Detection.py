def has_cycle(head):
    '''
    has_cycle has the following parameter:
      - SinglyLinkedListNode pointer head: a reference to the head of the list.

    Returns an int: 1 if there is a cycle or 0 if there is not.
    Note: If the list is empty, head will be null.
    '''
    
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast: return 1
    
    return 0