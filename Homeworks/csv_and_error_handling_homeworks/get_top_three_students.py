import csv
import os
from pathlib import Path

student_dict = {}

Header = ['student', 'exam', 'points']
current_directory = Path(os.path.abspath(__file__)).parent
with open(os.path.join(current_directory, "students_data.csv"), "r") as csv_source:
    reader = csv.reader(csv_source)

    for student_id, exam, points in reader:
        if [student_id, exam, points] == Header:
            continue
        student_dict.setdefault(student_id, {})
        student_dict[student_id][int(exam)] = int(points)

student_score = {}

for key, value in student_dict.items():
    total_result = 0
    for exam, points in value.items():
        total_result += points
    student_score.setdefault(key, 0)
    student_score[key] = total_result


sorted_by_score = sorted(student_score.items(), key=lambda x: x[1], reverse=True)

position = 1
for student, score in sorted_by_score:
    print(f"{student} is on {position} with {score}")
    position += 1
    if position > 3:
        break



