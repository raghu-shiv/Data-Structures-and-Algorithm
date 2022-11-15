'''
Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.
'''

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:    # changed = to ==
            res += '0'      # changed = to += and removed ;
        else:
            res += '1'      # changed = to += and removed ;

    return res

s = input()
t = input()
print(strings_xor(s, t))
