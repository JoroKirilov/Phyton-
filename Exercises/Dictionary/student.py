student_info = [element for element in input().split(":")]
student_book = dict()
while student_info[0][0].isupper():
    student_id = student_info[1]
    student_name = student_info[0]
    student_courses = student_info[2]
    student_book.setdefault(student_id, [student_name, student_courses])
    student_info = [element for element in input().split(":")]
else:
    searching_courses = student_info[0]
for key, value in student_book.items():
    if searching_courses == value[1]:
        print(f"{value[0]} - {key}")


