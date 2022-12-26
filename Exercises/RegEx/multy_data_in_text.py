import re

line = input()
while line:
    pattern = r"(>>)?(?P<product>[A-Za-z]+)(<<)?(?P<price>\d+\.?[\d]+)?!?(?P<quntity>\d+)?"
    matches = re.finditer(pattern, line)
    for match in matches:
        result = match.groupdict()
        print(f"{result['product']} is {result['price']}")
    line = input()
