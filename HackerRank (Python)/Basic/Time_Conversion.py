def timeConversion(s):
    '''
    timeConversion has the following parameter(s):
      - string s: a time in 12 hour format
    Returns a string: the time in 24 hour format.
    '''

    militaryTime = ""
    hh = int(s[0:2])
    mmss = s[2:-2]
    
    if s[-2] == "P":
        if hh > 0 and hh < 12:
            hh += 12
        t = str(hh) + mmss

    elif s[-2] == "A":
        if hh == 12:
            hh = 0
        t = "0" + str(hh) + mmss
    
    militaryTime += t
    return militaryTime