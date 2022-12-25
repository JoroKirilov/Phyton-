import re

str1 = "Hello, my name is Georgi and i love to play football with friends.I am from Plovdiv. My favorite football club is Lokomotiv Plovdiv"

searching_word = re.findall('Plovdiv', str1)
print(len(searching_word))
