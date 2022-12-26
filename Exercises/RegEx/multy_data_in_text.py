import re

line = input()
list_product = []
total_cost = 0
while line != 'Purchase':
    pattern = r"(^>>)(?P<product>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        total_cost += float(obj['price']) * int(obj['quantity'])
        list_product.append(obj['product'])
    line = input()
print("Bought furniture:")
for element in list_product:
    print(element)
print(f"Total money spend: {total_cost:.2f}")