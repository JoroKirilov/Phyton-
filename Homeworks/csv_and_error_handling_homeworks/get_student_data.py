import csv
import os
from pathlib import Path


def get_students_data(file_name):
    INPUT_DIR = Path(os.path.abspath(__file__)).parent
    data_student = {}
    header = ['student', 'exam', 'points']
    with open(os.path.join(INPUT_DIR, file_name), 'r') as source:
        reader = csv.reader(source)

        for student_id, num_exam, score in reader:
            if [student_id, num_exam, score] == header:
                continue
            if not all([student_id, num_exam, score]):
                continue
            data_student.setdefault(student_id, {})
            data_student[student_id].update({num_exam: score})

    return data_student


first_data_students = {}
first_data_students = get_students_data("students_data.csv")

for student, exams in first_data_students.items():
    print(student, exams)





