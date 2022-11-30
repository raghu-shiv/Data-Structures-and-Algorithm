def largestRectangle(h):
    '''
    largestRectangle has the following parameter(s):
      - int h[n]: the building heights
      
    Returns a long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings.
    '''

    stack = []
    area = i = 0
    h.append(0)

    while i < len(h):
        # stack is empty or greater height is found
        if not stack or h[stack[-1]] < h[i]:
            # push the index of the building
            stack.append(i)
            i += 1
        # if height is lesser
        else:
            top = stack.pop()
            area = max(area, h[top] * (i-stack[-1] - 1 if stack else i))

    return area