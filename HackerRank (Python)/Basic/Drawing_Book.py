def pageCount(n, p):
    '''
    pageCount has the following parameter(s):
      - int n: the number of pages in the book
      - int p: the page number to turn to
    Returns an int: the minimum number of pages to turn.
    '''

    front = p//2
    back = n//2 - p//2
    
    if front < back:
        return front
    else:
        return back