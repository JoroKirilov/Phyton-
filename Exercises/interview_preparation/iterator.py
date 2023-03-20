# class vowels:
#     def __init__(self, string):
#         self.string = string
#         self.i = 0
#         self.end = len(string) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.i <= self.end:
#             current = self.string[self.i]
#             self.i += 1
#             if current.lower() in "aeiou":
#                 return current
#         else:
#             raise StopIteration
#
# iter_obj = vowels("AfdsroeudaeACD")
# for element in iter_obj:
#     print(element)


my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))