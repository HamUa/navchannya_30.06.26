import random

numbers = random.randint(3, 10)

random_list = [random.randint(1, 10) for _ in range(numbers)]

result = [random_list[0], random_list[2], random_list[-2]]

print(f"{random_list} == {result}")