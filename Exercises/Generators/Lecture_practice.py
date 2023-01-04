from datetime import datetime
import random


def generate_students_info():
    for e in range(1, 11):
        for s in range(1, 200000):
            yield f"Student {s}", {
                "student_name": f"Student {s}",
                "exam": e,
                "points": random.randint(random.choice([30, 40, 50]), 100),
            }


def generate_students_info_list():
    return [
        (
            f"Student {s}", {
                "student_name": f"Student {s}",
                "exam": e,
                "points": random.randint(random.choice([30, 40, 50]), 100),
            }
        )
        for s in range(1, 200000)
        for e in range(1, 11)
    ]


now = datetime.now()
print(now)

for student_name, student_info in generate_students_info():
    print(student_name, student_info)

after_generator_loop = datetime.now()
print(after_generator_loop)
print((after_generator_loop - now).total_seconds())