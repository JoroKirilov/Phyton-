def difference_max_one_correction(str_one, str_two):
    len_difference = abs(len(str_one) - len(str_two))

    if len_difference == 0:
        return max_one_difference_if_same_length(str_one, str_two)
    elif len_difference == 1:
        return max_one_difference_different_length(str_one, str_two)
    else:
        return False


def max_one_difference_different_length(str_one, str_two):
    len_one = len(str_one)
    len_two = len(str_two)
    difference = 0

    if len_one < len_two:
        for i in range(len_two):
            if difference == 1:
                if str_one[i - 1] != str_two[i]:
                    difference += 1
            if difference == 0 and i < len_two - 1:
                if str_one[i] != str_two[i]:
                    difference += 1
            if difference > 1:
                return False
    else:
        for i in range(len_one):
            if difference == 1:
                if str_two[i - 1] != str_one[i]:
                    difference += 1
            if difference == 0:
                if str_two[i] != str_one[i]:
                    difference += 1
            if difference > 1:
                return False

    return True


def max_one_difference_if_same_length(str_one, str_two):
    difference = 0
    for i in range(len(str_one)):
        if str_one[i] != str_two[i]:
            difference += 1
        if difference > 1:
            return False
    return True


print("Hello, Hell:", difference_max_one_correction("Hello", "Hell"))
print("abba, abba:", difference_max_one_correction("abba", "abba"))
print("hellas, hellasa:", difference_max_one_correction("hellas", "hellasa"))
print("hello, herfl:", difference_max_one_correction("hello", "herfl"))