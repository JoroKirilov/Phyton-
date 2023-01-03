import csv
import os.path
import random
import string
from pathlib import Path

BASE_DIR = Path(os.path.abspath(__file__)).parent


def test_file_generator(file_name="decorator_test.csv", min_rows=32, max_rows=64, min_cols=5, max_cols=15):
    with open(os.path.join(BASE_DIR, file_name), "w") as csv_output:
        writer = csv.writer(csv_output)

        number_of_rows = random.randint(min_rows, max_rows)

        for _ in range(number_of_rows):
            number_of_columns = random.randint(min_cols, max_cols)
            row_data = [
                random.choice(string.ascii_letters) * 5 for _ in range(number_of_columns)
            ]
            writer.writerow(row_data)


test_file_generator()

