def average_grade(roster):
    # roster is a list of student objects
    sum = 0
    for student in roster:
        sum += student.get_grade()
    return sum / len(roster)
