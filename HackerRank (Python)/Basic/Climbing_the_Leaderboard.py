def climbingLeaderboard(ranked, player):
    '''
    climbingLeaderboard has the following parameter(s):
      - int ranked[n]: the leaderboard scores
      - int player[m]: the player's scores
      
    Returns an int[m]: the player's rank after each new score.
    '''

    ranked = sorted(set(ranked), reverse=True)
    rankings = []
    
    for p in player:
        while ranked and p >= ranked[-1]:
            ranked.pop()
        rankings.append(len(ranked)+1)
    return rankings 