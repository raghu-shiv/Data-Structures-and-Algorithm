def reverse(llist):
  '''
  Returns a DoublyLinkedListNode: a reference to the head of the reversed list.
  '''

  if(llist == None):
    return None
  elif(llist.next == None):
    return llist
    
  while llist.next != None:
    llist.next, llist.prev, llist = llist.prev, llist.next, llist.next
    
  llist.next, llist.prev = llist.prev, None

  return llist