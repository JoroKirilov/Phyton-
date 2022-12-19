n = int(input())
data_student = {}
for _ in range(n):
    name, data_score = input().split()
    score = float(data_score)
    if name not in data_student:
        data_student[name] = []
    data_student[name].append(score)

for key, value in data_student.items():
    print(f"{key} -> {' '.join(f'{el:.2f}' for el in value)} (avg: {sum(value)/len(value):.2f})")



