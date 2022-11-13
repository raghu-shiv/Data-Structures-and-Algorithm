def insertNodeAtPosition(llist, data, position):
  '''
  The function accepts following parameters:
    1. INTEGER_SINGLY_LINKED_LIST llist
    2. INTEGER data
    3. INTEGER position
  
  Returns a SinglyLinkedListNode pointer: a reference to the head of the revised list.
  '''

  newNode = SinglyLinkedListNode(data)

  if llist==None:
    llist = newNode
  elif position==0:
    newNode.next = llist
    return newNode
  else:
    curNode = llist
    i = 1
    while curNode!=None and i<position:
      curNode = curNode.next
      i += 1
    newNode.next = curNode.next
    curNode.next = newNode
  return llist