def get_bigger_string(str1: str, str2: str):
    if str1 > str2:
        return str1, str2
    return str2, str1


def compare_strings(text1: str, text2: str):
    if text1 == text2:
        return True
    str1_length = len(text1)
    str2_length = len(text2)
    str_diff = 0
    if str1_length == str2_length:
        for index in range(str2_length):
            if text1[index] != text2[index]:
                str_diff += 1
        if str_diff < 2:
            return True
    check_diff = str1_length - str2_length
    if abs(check_diff) == 1:
        bigger_text, smaller_text = get_bigger_string(text1, text2)
        if smaller_text in bigger_text:
            print("smaller")
            return True
        index_of_diff = 0
        for index in range(len(smaller_text)):
            if smaller_text[index] != bigger_text[index]:
                index_of_diff = index
        if smaller_text[index_of_diff:] in bigger_text:

            return True


    return False


str1 = "hllo"
str2 = "hello"

print(compare_strings(str1, str2))
