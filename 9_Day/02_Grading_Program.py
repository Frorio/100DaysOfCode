student_scores = {
    "Petrovich": 81,
    "Macdonald": 78,
    "Sanok": 74,
    "Your mom": 100
}
# Create an empty dictionary called student_grades
student_grades = {}

# Add the grades to student_grades
for student in student_scores:
    score = student_scores[student]
    if score > 90: 
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else: student_grades = "Fail"