def mergeLists(head1, head2):
    '''
    Returns a SinglyLinkedListNode pointer: a reference to the head of the merged list.
    '''

    if head1==None and head2==None: return None
    
    merged = SinglyLinkedList()
    node1, node2 = head1, head2
  
    while node1 or node2: 
        if not node1:
            merged.insert_node(node2.data)
            node2 = node2.next
        elif not node2:
            merged.insert_node(node1.data)
            node1 = node1.next
        else:
            if node1.data <= node2.data:
                merged.insert_node(node1.data)
                node1 = node1.next
            else:
                merged.insert_node(node2.data)
                node2 = node2.next

    return merged.head