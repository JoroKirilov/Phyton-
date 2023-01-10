import argparse

def get_bigger_string(str1: str, str2: str):
    if len(str1) > len(str2):
        return str1, str2
    return str2, str1


def compare_strings(processed_output):
    text1 = processed_output.string1
    text2 = processed_output.string2
    if text1 == text2:
        return True
    str1_length = len(text1)
    str2_length = len(text2)
    str_diff = 0
    # if string is with equal length check char by char and if is only one difference return true
    if str1_length == str2_length:
        for index in range(str2_length):
            if text1[index] != text2[index]:
                str_diff += 1
        if str_diff < 2:
            return True
    # check if is only one difference between strings
    check_diff = str1_length - str2_length
    if abs(check_diff) == 1:
        bigger_text, smaller_text = get_bigger_string(text1, text2)
        # check is smaller string is sub string of bigger one and return True if is it
        if smaller_text in bigger_text:
            return True
        index_of_diff = 0
        # find in which index we have difference
        for index in range(len(smaller_text)):
            if smaller_text[index] != bigger_text[index]:
                index_of_diff = index

        # if difference is in on last index of smaller text, we check if last char of two strings is equal
        if len(smaller_text) == index_of_diff + 1:
            if smaller_text[index_of_diff] == bigger_text[-1]:
                return True
            else:
                return False
        # check sub string starting on index of difference is in bigger text
        sub_string_to_check = smaller_text[index_of_diff + 1:]
        if sub_string_to_check in bigger_text:
            return True

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to strings game")
    parser.add_argument("string1", type=str, help="enter first string")
    parser.add_argument("string2", type=str, help="enter second string")
    parsed_args = parser.parse_args()
    print(compare_strings(parsed_args))







