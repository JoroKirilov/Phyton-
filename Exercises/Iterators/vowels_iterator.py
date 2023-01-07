# class Vowels:
#     def __init__(self, obj):
#         self.obj = obj
#         self.i = 0
#         self.end = len(obj) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.i <= self.end:
#             current = self.obj[self.i]
#             self.i += 1
#             if current in "AaEeOoIi":
#                 return current
#         else:
#             raise StopIteration
#
#
# str_list = "AvdpeaioiesaciWioreewmk"
# vowel_iterator = Vowels(str_list)
# for char in vowel_iterator:
#     print(char, end=' ')