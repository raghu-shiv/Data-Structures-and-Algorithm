def flippingBits(n):
    '''
    flippingBits has the following parameter(s):
      - int n: an integer
    Returns an int: the unsigned decimal integer result.
    '''

    binary = bin(n)[2:]
    l = len("0"*32) - len(binary)
    binary_32bit = "0"*l + binary
    binary_list = list(binary_32bit)
    
    for i in range(len(binary_list)):
        if binary_list[i] == "0":
            binary_list[i] = "1"
        else:
            binary_list[i] = "0"
    
    result = "".join(binary_list)
    return int(result, 2)