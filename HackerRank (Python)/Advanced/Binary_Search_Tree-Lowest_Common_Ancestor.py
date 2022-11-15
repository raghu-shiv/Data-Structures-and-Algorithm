'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree, which contains info as data, left, right
'''

def lca(root, v1, v2):
    '''
    lca has the following parameters:
      - root: a pointer to the root node of a binary search tree
      - v1: a node.data value
      - v2: a node.data value
    Returns a pointer to the lowest common ancestor node of the two values given.
    '''

    # Calculate min and max of v1, v2 to ensure n1 is lesser and n2 is greater
    n1 = min(v1, v2)
    n2 = max(v1, v2)
    curNode = root

    while True:
        # if both values are lesser
        if n1 < curNode.info and n2 < curNode.info:
            curNode = curNode.left
        # if both values are greater
        elif n1 > curNode.info and n2 > curNode.info:
            curNode = curNode.right
        # LCA
        else:
            return curNode