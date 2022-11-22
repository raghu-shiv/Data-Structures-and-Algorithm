'''
Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format:
    1. Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
    2. The operation will either be S (split) or C (combine)
    3. M indicates method, C indicates class, and V indicates variable
    4. In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
    5. In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.
'''

while True:
    try:
        q = input().rstrip()
    except EOFError:
        break
    op = q[0]
    st = q[2]
    string = list(q[4:])
    
    if op == 'S':
        temp1 = ''
        if st == 'M':
            for s in string[:-2]:
                if s.islower():
                    temp1 += s
                elif s.isupper():
                    temp1 += f' {s.lower()}'
            print(temp1)
        elif st == 'V':
            for s in string:
                if s.islower():
                    temp1 += s
                elif s.isupper():
                    temp1 += f' {s.lower()}'
            print(temp1)
        elif st == 'C':
            temp1 += string[0].lower()
            for s in string[1:]:
                if s.islower():
                    temp1 += s
                elif s.isupper():
                    temp1 += f' {s.lower()}'
            print(temp1)
    
    if op == 'C':
        temp2 = ''
        if st == 'M':
            temp2 = string.copy()
            for i in range(len(string)):
                if string[i] == ' ':
                    temp2[i+1] = temp2[i+1].upper()
            temp2 = "".join(temp2)
            temp2 = temp2.replace(' ', '')
            print(temp2+"()")
        elif st == 'V':
            temp2 = string.copy()
            for i in range(len(string)):
                if string[i] == ' ':
                    temp2[i+1] = temp2[i+1].upper()
            temp2 = "".join(temp2)
            print(temp2.replace(' ', ''))
        elif st == 'C':
            temp2 = string.copy()
            for i in range(len(string)):
                if string[i] == ' ':
                    temp2[i+1] = temp2[i+1].upper()
            temp2[0] = temp2[0].upper()
            temp2 = "".join(temp2)
            print(temp2.replace(' ', ''))
    