import csv
import os
from pathlib import Path
import random

student_dict = {}

Header = ['student', 'exam', 'points']
current_directory = Path(os.path.abspath(__file__)).parent
with open(os.path.join(current_directory, "students_exams.csv"), "r") as csv_source:
    reader = csv.reader(csv_source)

    for student_id, exam, points in reader:
        if [student_id, exam, points] == Header:
            continue
        # print(student_id, exam, points)
        student_dict.setdefault(student_id, {})
       # student_dict[student_id] = {exam: points}
        student_dict[student_id][int(exam)] = int(points)

passed_students = {}
failed_students = []


for key, value in student_dict.items():
    total_result = 0
    for exam, points in value.items():
        total_result += points

    if total_result < 800:
        failed_students.append(key)
    else:
        passed_students.setdefault(key, total_result)
print(len(failed_students))
count = 0
for student in failed_students:
    for key, value in student_dict.items():
        if key == student:
            for exam, points in value.items():
                if points < 80:
                    for _ in range(3):
                        points = random.choice(range(62, 92))
                        student_dict[student][exam] = points
                        if points >= 80:
                            break
            average = 0
            for exam, points in value.items():
                average += points
            if average > 800:
                passed_students.setdefault(key, average)

print(list(student_dict))
for key , value in passed_students.items():
    print(f" {key}, pass with {value} result")
                   # print(f"student {student} is failed on exam {exam} ")



# for index in range(3):
#     for key, value in failed_students:


# for key, value in passed_students.items():
#     print(key)
#     print(value)
# print(len(passed_students))



# def get_student_average(student_dict):
#
#     for key, value in student_dict.items():
#         average_result = 0
#         for exam, points in value.items():
#             average_result += points
#
