orders = int(input())
price_for_caffe = 0
total = 0
for order in range(orders):
    price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if (0 < price < 100) and (1 <= days <= 31) and (1 <= capsule_per_day <= 2000):
        price_for_caffe = price * days * capsule_per_day
        format_price = "{:.2f}".format(price_for_caffe)
        print(f"The price for the coffee is: ${format_price}")
        total += price_for_caffe
format_float = "{:.2f}".format(total)
print(f"Total: ${format_float}")
