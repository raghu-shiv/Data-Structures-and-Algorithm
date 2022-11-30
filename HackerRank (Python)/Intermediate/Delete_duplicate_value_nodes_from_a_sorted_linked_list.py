def removeDuplicates(llist):
    '''
    removeDuplicates has the following parameter:
      - SinglyLinkedListNode pointer head: a reference to the head of the list.

    Returns a SinglyLinkedListNode pointer: a reference to the head of the revised list.
    '''

    # create a temporary pointer
    temp = llist
    
    while temp.next != None:
        if temp.data == temp.next.data:
            # delete the next node
            temp.next = temp.next.next
        else:
            temp = temp.next
    
    return llist