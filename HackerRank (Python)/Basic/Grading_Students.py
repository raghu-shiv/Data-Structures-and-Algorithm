def gradingStudents(grades):
    '''
    gradingStudents has the following parameter(s):
      - int grades[n]: the grades before rounding
    Returns an int[n]: the grades after rounding as appropriate.
    '''

    for i, grade in enumerate(grades):
        if grade >= 38:
            diff = 5 - grade%5
            if diff < 3:
                grades[i] = grade + diff
    return grades