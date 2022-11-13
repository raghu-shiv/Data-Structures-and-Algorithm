def reverse(llist):
  '''
  Returns a SinglyLinkedListNode pointer: a reference to the head of the reversed list.
  '''

  if(llist == None):
    return None
  elif(llist == 1):
    return llist
    
  curNode = llist
  prevNode = None
    
  while curNode != None:
    nextNode, curNode.next = curNode.next, prevNode
    prevNode, curNode = curNode, nextNode
    
  llist = prevNode
  return llist