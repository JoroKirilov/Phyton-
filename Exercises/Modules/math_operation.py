from helper.operation_mapper import dict_operator

data = input().split()
operant1 = float(data[0])
operant2 = float(data[2])
sign = data[1]

result = dict_operator[sign](operant1, operant2)
print(f"{result:.2f}")