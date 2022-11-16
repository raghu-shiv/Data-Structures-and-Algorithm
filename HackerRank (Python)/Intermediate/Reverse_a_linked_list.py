def reverse(llist):
    '''
    Returns a SinglyLinkedListNode pointer: a reference to the head of the reversed list.
    '''

    head = llist
    
    if head == None: return None
    if head.next == None: return head
    
    currNode = head
    prevNode = None
    
    while currNode != None:
        nextNode, currNode.next = currNode.next, prevNode
        prevNode, currNode = currNode, nextNode
    
    head = prevNode
    return head