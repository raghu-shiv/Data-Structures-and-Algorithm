def maximumPerimeterTriangle(sticks):
    '''
    maximumPerimeterTriangle has the following parameter(s):
      - int sticks[n]: the lengths of sticks available
    Returns an int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or [-1].
    '''

    # To form a triangle,
    # Longest side < Sum of the other two sides.

    s = sorted(sticks, reverse=True)

    for i in range(len(sticks)-2):
        if(s[i] < s[i+1] + s[i+2]):
            return [s[i+2], s[i+1], s[i]]
    return [-1]