string = input()
while string != 'End':
    tmp_string = ''
    if string != "SoftUni":
        for char in string:
            tmp_string = tmp_string + (char * 2)
    print(tmp_string)
    string = input()
