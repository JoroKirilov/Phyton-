# 'a', 'o', 'u', 'e', 'i'.
string_no_vowels = ""
no_vowels_text = input()
result = [char for char in no_vowels_text if char != 'a' and char != 'o' and char != 'u' and char != 'e' and char != 'i']

print(string_no_vowels.join(result))