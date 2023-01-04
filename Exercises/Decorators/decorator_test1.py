import os.path
import random
import string
from pathlib import Path
from functools import lru_cache
import csv

# from Decorators.example1 import print_time_stats

BASE_DIR = Path(os.path.abspath(__file__)).parent


def print_list(list):
    row_index = 0
    for row in list:
        print(row_index, row)
        row_index += 1


# def test_file_generator(file_name="decorator_test.csv", min_rows=32, max_rows=64, min_cols=5, max_cols=15):
#     with open(os.path.join(BASE_DIR, file_name), "w") as csv_output:
#         writer = csv.writer(csv_output)
#
#         number_of_rows = random.randint(min_rows, max_rows)
#         for _ in range(number_of_rows):
#             number_of_columns = random.randint(min_cols, max_cols)
#             row_data = [
#                 "".join(
#                     [random.choice(string.ascii_letters) for _ in range(5)]
#                 )
#                 for _ in range(number_of_columns)
#             ]
#             writer.writerow(row_data)


#test_file_generator()


def track_max_length_rows_of_a_csv_file(func):
    def wrapper_func(file_path):
        csv_content = func(file_path)
        longest_row = max(len(row) for row in csv_content)
        longest_rows = [i for i, row in enumerate(csv_content) if len(row) == longest_row]
        if longest_rows:
            print(f"Longest rows of {file_path.name} are: {longest_rows}")
        return csv_content

    return wrapper_func


def track_min_length_rows_of_a_csv_file(func):
    def wrapper_func(file_path):
        csv_content = func(file_path)
        shortest_row = min(len(row) for row in csv_content)
        shortest_rows = [i for i, row in enumerate(csv_content) if len(row) == shortest_row]
        if shortest_rows:
            print(f"Shortest rows of {file_path.name} are: {shortest_rows}")
        return csv_content

    return wrapper_func


# How to make decorator, that returns the min length rows of a CSV file
# How to make decorator, that returns the max length rows of a CSV file
# How to make decorator that returns the word with max occurrences ONLY if those are wanted

# Should protect our decorators against not existing files


def ensure_csv_content(func):
    def wrapper_func(file_path):
        content = func(file_path)
        if not isinstance(content, list):
            print("CSV file doesn't have any valid content")
            return [""]
        return content

    return wrapper_func


# def get_max_occurrences_word(required):
#     pass
#
#
# @get_max_occurrences_word(required=False)
@track_min_length_rows_of_a_csv_file
@track_max_length_rows_of_a_csv_file
@ensure_csv_content
# @print_time_stats
def get_csv_file_content(file_path: Path):
    # Check if file_path is of CSV file, if not exit with Message
    if file_path.suffix != ".csv":
        print("Not sent correct type of file")
        return []

    # Read the CSV file , using the file_path and return its content as list of lists
    try:
        with open(file_path, "r") as csv_source:
            csv_content = csv.reader(csv_source)
            return list(csv_content)
    except FileNotFoundError:
        print("Given file_path not found on this machine")
        return []


FILE_NAME = "decorators_test1.csv"
file_path_with_path_class = Path(os.path.join(BASE_DIR, FILE_NAME))
print_list(get_csv_file_content(file_path_with_path_class))