def matchingStrings(strings, queries):
    '''
    matchingStrings has the following parameters:
      - string strings[n] - an array of strings to search
      - string queries[q] - an array of query strings
    Returns an int[q]: an array of results for each query.
    '''

    results = []
    
    for query in queries:
        query_count = strings.count(query)
        results.append(query_count)
    return results