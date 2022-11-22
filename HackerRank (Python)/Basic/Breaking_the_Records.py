def breakingRecords(scores):
    '''
    breakingRecords has the following parameter(s):
      - int scores[n]: points scored per game
    Returns an int[2]: An array with the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
    '''

    minScore = maxScore = scores[0]
    minCount = maxCount = 0
    
    for score in scores:
        if score==minScore or score==maxScore:
            continue
        elif score < minScore:
            minScore = score
            minCount += 1
        elif score > maxScore:
            maxScore = score
            maxCount += 1
    
    return [maxCount, minCount]