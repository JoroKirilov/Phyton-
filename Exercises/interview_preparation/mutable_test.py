# list are mutable
# list1 = [1, 2, 3, 5]
# print(list1)
# list2 = list1  # creating pointer that point to address of list 1

list3 = [3, 4, 5, 6]
list4 = list3.copy() # how to make copy of list ( new list )
list4.append(5)
print(list4)
print(list3)
# list_slicing = [10, 11, 12, 13, 14, 15]
# list77 = list_slicing[::-1]
# list77.remove(10)
# list77.pop
# del list77[0]
# print(list77)
# # ---------------------------------------------
# # string are immutable
# str1 = "hello"
# str1 += "gg"
# str2 = str1          # making a copy
# srt2 = ''
# print(str1)

# -------------------------------------------
# int is immutable
# n = 4
# m = 5  # this value of 5 is garbage
# m = n
# print(m)
# print(n)
# print(ord('a'))