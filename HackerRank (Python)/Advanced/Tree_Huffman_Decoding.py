"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

def decodeHuff(root, s):
    '''
    The function has the following parameters:
      - root: a reference to the root node of the Huffman tree
      - s: a Huffman encoded string
    Print the decoded string in a single line.
    '''

    # create temporary pointer 
    curNode = root
    decodedChars = []

    # traverse binary coded string
    for char in s:
        # traverse to left 
        if char == '0':
            curNode = curNode.left
        # traverse to right
        else:
            curNode = curNode.right

        # check for the leaf node
        if curNode.left == None and curNode.right == None:
            # append the data if found
            decodedChars.append(curNode.data)
            # return to the root
            curNode = root

    decodedString = "".join(decodedChars)
    print(decodedString)