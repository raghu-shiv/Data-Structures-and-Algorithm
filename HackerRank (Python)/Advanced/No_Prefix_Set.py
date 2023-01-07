def noPrefix(words):
    '''
    noPrefix has the following parameter(s):
        - string words[n]: an array of strings.
    
    Prints a string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.
    '''

def noPrefix(words):
    trie = {}
    for word in words:
        if insert(trie, word):
            print(f'BAD SET\n{word}')
            return    
    print('GOOD SET')

def insert(trie, word):
    for i, char in enumerate(word):
        if char in trie:
            if trie[char][1] or i == len(word)-1:
                return True
        else:
            trie[char] = {}, i == len(word)-1
        
        trie, _ = trie[char]
        
    return False
