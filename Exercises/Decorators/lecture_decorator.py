import csv
import os.path
import random
import string
from functools import wraps
from pathlib import Path
import operator

# from Decorators.example1 import print_time_stats

BASE_DIR = Path(os.path.abspath(__file__)).parent


# def test_file_generator(
#     file_name="decorator_example.csv",
#     min_rows=32,
#     max_rows=64,
#     min_cols=random.randint(3, 8),
#     max_cols=random.randint(12, 18),
# ):
#     with open(os.path.join(BASE_DIR, file_name), "w") as csv_output:
#         writer = csv.writer(csv_output)
#         number_of_rows = random.randint(min_rows, max_rows)
#
#         for _ in range(number_of_rows):
#             number_of_columns = random.randint(min_cols, max_cols)
#             row_data = [
#                 "".join([random.choice(string.ascii_letters) for _ in range(2)])
#                 for _ in range(number_of_columns)
#             ]
#             writer.writerow(row_data)


def track_min_length_rows_of_a_csv_file(func):
    """How to make decorator, that returns the min length row(s) of a CSV file."""

    @wraps(func)
    def wrapper_func(file_path):
        csv_content = func(file_path)
        shortest_row = min((len(row) for row in csv_content), default=0)
        shortest_rows = [
            i for i, row in enumerate(csv_content) if len(row) == shortest_row
        ]
        if shortest_rows:
            print(f"Shortest rows of {file_path.name} are: {shortest_rows}")
        return csv_content

    return wrapper_func


def track_max_length_rows_of_a_csv_file(func):
    """How to make decorator, that returns the max length row(s) of a CSV file."""

    @wraps(func)
    def wrapper_func(file_path):
        csv_content = func(file_path)
        longest_row = max((len(row) for row in csv_content), default=0)
        longest_rows = [
            i for i, row in enumerate(csv_content) if len(row) == longest_row
        ]
        if longest_rows:
            print(f"Longest rows of {file_path.name} are: {longest_rows}")
        return csv_content

    return wrapper_func


def ensure_csv_content(func):
    @wraps(func)
    def wrapper_func(file_path):
        content = func(file_path)
        if not isinstance(content, list):
            raise Exception("CSV file doesn't have any valid content")
        return content

    return wrapper_func


# How to make decorator that returns the word with max occurrences ONLY if those are wanted


# @print_time_stats
def get_max_occurrences_word(required=True):
    def decorator(func):
        def wrapper(file_path):
            if not required:
                return func(file_path)
            text_input = ''
            dict_filter = {}
            result_list = func(file_path)
            for element in result_list:
                for word in element:
                    dict_filter.setdefault(word, 0)
                    dict_filter[word] += 1

            dict_srt = dict(sorted(dict_filter.items(), key=(lambda x: -x[1])))
            for k, v in dict_srt.items():
                text_input += f"{k} -> {v} \n"
            return text_input



        return wrapper

    return decorator


@get_max_occurrences_word(required=True)
@track_max_length_rows_of_a_csv_file
@track_min_length_rows_of_a_csv_file
@ensure_csv_content
def get_csv_file_content(file_path: Path):
    if file_path.suffix != ".csv":
        # Check if file_path is of CSV file, if not exit with Message
        print("Not sent correct type of file")
        return []

    # Read the CSV file, using the file_path and return its content as list of lists
    try:
        # Check if file_path actually exists, if not exit with Message
        with open(file_path, "r") as csv_source:
            csv_content = csv.reader(csv_source)
            return list(csv_content)
    except FileNotFoundError:
        print("Given file_path not found on this machine")
        return []


if __name__ == "__main__":
    file_name = "decorator_example.csv"
    # test_file_generator()
    file_path_with_path_class = Path(os.path.join(BASE_DIR, file_name))
    print(
        f"CSV content of {file_path_with_path_class.name}:"
        f" {get_csv_file_content(file_path_with_path_class)}"
    )
