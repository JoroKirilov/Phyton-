input_data = [int(el) for el in input().split(" ")]
positive_sum = sum([el for el in input_data if el > 0])
negative_sum = sum([el for el in input_data if el < 0])
print(negative_sum)
print(positive_sum)
print("The positive are stronger than the positives") if positive_sum > abs(negative_sum) \
    else print("The negatives are stronger than the positives")
