budget = int(input())
command = input()
all_sum = 0
while command != 'End':
    all_sum += int(command)
    if all_sum > budget:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")
