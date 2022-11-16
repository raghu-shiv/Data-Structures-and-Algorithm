def insertNodeAtPosition(llist, data, position):
    '''
    The function accepts following parameters:
      1. INTEGER_SINGLY_LINKED_LIST llist
      2. INTEGER data
      3. INTEGER position
  
    Returns a SinglyLinkedListNode pointer: a reference to the head of the revised list.
    '''

    head = llist
    newNode = SinglyLinkedListNode(data)
    
    if head == None: 
        head = newNode
    if position == 0:
        newNode.next = head
        return newNode
        
    currNode = head
    i = 1
    while currNode != None and i < position:
        currNode = currNode.next
        i += 1
    currNode.next, newNode.next = newNode, currNode.next
    return head