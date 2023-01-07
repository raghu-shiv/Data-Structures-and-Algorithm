def cubeSum(n, operations):
    '''
    cubeSum has the following parameters: 
      - *int n: the dimensions of the 3-d matrix 
      - string operations[m]: the operations to perform

    Returns an int[]: the results of each QUERY operation.
    '''

    matrix = {}
    results = []
    
    for operation in operations:
        query = operation.split(' ')
        op = query[0]
        
        if op == 'UPDATE':
            [x, y, z, w] = [int(q) for q in query[1:]]
            matrix[(x, y, z)] = w

        elif op == 'QUERY':
            [x1, y1, z1, x2, y2, z2] = [int(q) for q in query[1:]]
            
            value = 0
            
            for (x, y, z) in matrix:
                if x2>=x>=x1 and y2>=y>=y1 and z2>=z>=z1:
                    value += matrix[(x, y, z)]
            
            results.append(value)
    
    return results