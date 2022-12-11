# 2) Напишете функция, която приема стринг и връща индекса на първия character,
# който не се повтаря (среща се само един път в целия стринг). Ако няма такъв върнете -1.
# input: "abcdcaf"
# expected_output: 1 (връщаме 1, защото b е първият char, който не се повтаря и е с индекс 1 в стринга "abcdcaf")
from collections import Counter

def char_repeat(str):
    p = Counter(str)
    for key, value in p.items():
        if value == 1:
            return str.index(key)
    else:
        return -1

my_string = "abcdcaf"
print(char_repeat(my_string))