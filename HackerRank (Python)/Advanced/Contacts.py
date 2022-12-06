from collections import Counter

def contacts(queries):
    '''
    contacts has the following parameters:
      - string queries[n]: the operations to perform.

    Returns an int[]: the results of each find operation.
    '''

    nameCount = []
    contacts = Counter()
    
    for cmd, name in queries:
        if cmd == 'add':
            for i in range(1, len(name)+1):
                contacts.update([name[:i]])
        else:
            nameCount.append(contacts[name])
    
    return nameCount