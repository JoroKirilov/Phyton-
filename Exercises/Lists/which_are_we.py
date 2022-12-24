# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line,
# which are substrings of any string in the second input line.

# Input	                                        Output
# arp, live, strong
# lively, alive, harp, sharp, armstrong	   ['arp', 'live', 'strong']
result_list = []
sub_strings = input().split(', ')
words = input().split(', ')
for sub_string in sub_strings:
    for word in words:
        if sub_string in word:
            if sub_string not in result_list:
                result_list.append(sub_string)
print(result_list)
