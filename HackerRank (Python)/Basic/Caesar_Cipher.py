def caesarCipher(s, k):
    '''
    caesarCipher has the following parameter(s):
      - string s: cleartext
      - int k: the alphabet rotation factor
    Returns a string: the encrypted string
    '''

    enString = ""
    
    for letter in s.lower():
        if letter.isalpha():
            enString += chr((ord(letter)+k-97)%26+97)
        else:
            enString += letter
    
    enString = list(enString)
    for i in range(len(enString)):
        if s[i].isupper():
            enString[i] = enString[i].upper()
    
    enString = "".join(enString)
    return enString