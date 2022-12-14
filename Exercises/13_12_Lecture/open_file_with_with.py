import csv
import os
from contextlib import suppress
from pathlib import Path

# print(Path(os.path.abspath(__file__)))
Header = ['student', 'exam', 'points']
current_directory = Path(os.path.abspath(__file__)).parent
with open(os.path.join(current_directory, "students_exams.csv"), "r") as csv_source:
    reader = csv.reader(csv_source)

    for student_id, number, score in reader:
        if :
            continue
        print(row)
