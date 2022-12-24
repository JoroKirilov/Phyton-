# You are fed up with changing the version of your software manually.
# Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the previous number.
# For more clarification, see the examples below.

# Input	Output
# 1.2.3	1.2.4
# 1.3.9	1.4.0
# 3.9.9	4.0.0

def update_version(num1, num2, num3):
    if num3 < 9:
        num3 += 1
    elif num3 == 9:
        num3 = 0
        if num2 < 9:
            num2 += 1
        elif num2 == 9:
            num2 = 0
            num1 += 1
    print(f"{num1}.{num2}.{num3}")


n1, n2, n3 = input().split('.')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
update_version(n1, n2, n3)
