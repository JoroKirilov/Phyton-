def exchange(nums_list , index ):

    if 0 <= index < len(nums_list):
        first_part = nums_list[0:index+1]
        second_part = nums_list[index+1]
        exchanged_list = second_part + first_part
        return exchanged_list

    else:
        print("Invalid index")
def get_max_odd(nums_list):
    filter_only_odds = []
    for el in nums_list:
        if el % 2 == 1:
            filter_only_odds.append(el)
    max_odd = max(filter_only_odds)
    for index in range(len(nums_list)-1, -1 , -1 ):
        if nums_list[index] == max_odd:
            print(index)
            break
def
    filter_only_odds = filter(lambda x: x%2 == 1  )
    max_odd = max(nums_list)
numbers_as_string = input().split()
number = list(map(int, numbers_as_string ))

command = input()
while not command == "end":

 if command.split()[0] == "exchange":
   index = int(command.split()[1])
   numbers = exchange(number, index)
 elif command.split()[0] == "max":
  if command.split()[1] == "odd":
   get_max_odd(numbers)
  elif command.split()[1] =="even"

command = input()

