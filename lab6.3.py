import random

def generate_set(size, lower_bound, upper_bound):
    return set(random.randint(lower_bound, upper_bound) for _ in range(size))

set1 = generate_set(10, 1, 20)
set2 = generate_set(10, 1, 20)

common_elements = set1.intersection(set2)

print("Множина 1:", set1)
print("Множина 2:", set2)
print("Спільні елементи:", common_elements)
