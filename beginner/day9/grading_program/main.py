student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        grades[student] = "Outstanding"
    elif score >= 81:
        grades[student] = "Exceeds Expectations"
    elif score >= 71:
        grades[student] = "Acceptable"
    else:
        grades[student] = "Fail"

print(grades)