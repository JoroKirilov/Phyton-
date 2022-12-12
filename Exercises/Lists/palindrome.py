words = input()
searching_palindrome = input()
result = words.split(" ")
palindrome_word = []
count_palindrome = 0
for word in result:
    back_idx = len(word) - 1
    front_idx = 0
    while back_idx != front_idx:
        if word[front_idx] != word[back_idx]:
            break
        front_idx += 1
        back_idx -= 1
    else:
        if word == searching_palindrome:
            count_palindrome += 1
        palindrome_word.append(word)
print(palindrome_word)
print(f"Found palindrome {count_palindrome} times")
