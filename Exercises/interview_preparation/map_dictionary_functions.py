map_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b
}

w = 5
sign = '+'
x = 10
result = map_dict[sign](w, x)
print(result)


class Operator:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sort_by_name():
        print("sorting by name")
    @staticmethod
    def sort_by_title():
        print("sort by title")

book = Operator("t")

book.sort_by_title()

sort_method = "title"
call_operator = "book.sort_by_" + sort_method + "()"
operation = "5 + 23"
eval(call_operator)
print(eval(operation))