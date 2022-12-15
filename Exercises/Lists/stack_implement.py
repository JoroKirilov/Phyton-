expresions = input()

stack_list = []

for index in range(len(expresions)):
    if expresions[index] == '(':
        stack_list.append(index)
    if expresions[index] == ')':
        start_index = stack_list.pop()
        print(expresions[start_index: index + 1])
