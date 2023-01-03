import csv
import os.path
import random
import string
from pathlib import Path

BASE_DIR = Path(os.path.abspath(__file__)).parent


class InvalidFileExtension(Exception):
    pass


def test_file_generator(file_name="decorator_test.csv", min_rows=32, max_rows=64, min_cols=5, max_cols=15):
    with open(os.path.join(BASE_DIR, file_name), "w") as csv_output:
        writer = csv.writer(csv_output)

        number_of_rows = random.randint(min_rows, max_rows)
        for _ in range(number_of_rows):
            number_of_columns = random.randint(min_cols, max_cols)
            row_data = [
                "".join(
                    [random.choice(string.ascii_letters) for _ in range(5)]
                )
                for _ in range(number_of_columns)
            ]
            writer.writerow(row_data)


# test_file_generator()

# Make decorator that returns the min length rows of CSV file
def track_min_length_rows(func):
    def wrapper_func(file_path):
        csv_content = func(file_path)
        shortest_row = min((len(row) for row in csv_content), default=0)
        shortest_rows = [i for i, row in enumerate(csv_content) if len(row) == shortest_row]
        print(f"Shortest rows of {file_path.name} are {shortest_rows}")
        return csv_content
    return wrapper_func


# Make decorator that return the max length rows of CSV file
def track_max_length_row(func):
    def wrapper_func(file_path):
        csv_content = func(file_path)
        longest_row = max((len(row) for row in csv_content), default=0)
        longest_rows = [i for i, row in enumerate(csv_content) if len(row) == longest_row]
        print(f"Longest rows of {file_path.name} are {longest_rows}")
        return csv_content
    return wrapper_func

@track_max_length_row
@track_min_length_rows
def get_csv_file_content(file_path: Path):
    # todo Check if file_path is of CSV FILE

    if file_path.suffix != ".csv":
        print("Not sent correct type")
        return False

    # Read the CSV file
    try:
        with open(file_path, "r") as csv_source:
            csv_content = csv.reader(csv_source)
            return list(csv_content)

    except FileNotFoundError:
        print("No such file or directory")
        return False


file_name = "decorator_test.csv"
file_path_1 = Path(os.path.join(BASE_DIR, file_name))
print(get_csv_file_content(file_path_1))
