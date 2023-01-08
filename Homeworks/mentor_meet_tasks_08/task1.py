# Напишете функция която приема лист от уникални стрингове и връща само палиндромите.
# words = ['diaper', 'abc', 'test', 'cba', 'repaid']
# expected_output = [['diaper', 'repaid'], ['abc', 'cba']]

words = ['diaper', 'abc', 'test', 'cba', 'repaid']
words_set = set(words)
list_palindrome = []
idx = 0
for word in words:
    rev_word = word[::-1]
    if rev_word in words_set:
        list_palindrome.append(word)


print(list_palindrome)