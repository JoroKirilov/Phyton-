def student_grade(grade:float):
    student = ""
    if grade > 2 and grade < 3:
        student = "Fail"
    elif grade >= 3 and grade < 3.5:
        student = "Poor"
    elif grade >= 3.5 and grade < 4.5:
        student = "Good"
    elif grade >= 4.5 and grade < 5.5:
        student = "Very Good"
    else:
        student = "Excellent"

    return student


grade = float(input())
print(student_grade(grade))

