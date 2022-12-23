# Write a function that receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console.

def return_symbols_between(char1, char2):
    list_of_char_value = []
    for value in range(ord(char1) + 1, ord(char2)):
        list_of_char_value.append(chr(value))
    return list_of_char_value


symbol = input()
symbol2 = input()
result = return_symbols_between(symbol, symbol2)
print(*result, sep=" ")

