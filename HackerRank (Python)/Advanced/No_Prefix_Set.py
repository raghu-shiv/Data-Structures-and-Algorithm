def noPrefix(words):
    '''
    The function accepts STRING_ARRAY words as parameter.
    Prints a string(s): either GOOD SET or BAD SET on one line followed by the word on the next line. No return value is expected.
    '''

    partial, full = set(), set()

    for word in words:
        if word in partial:
            print(f'BAD SET\n{word}')
            return
        for i in range(1, len(word)+1):
            if word[:i] in full:
                print(f'BAD SET\n{word}')
                return
            partial.add(word[:i])
        full.add(word)
    
    print("GOOD SET")