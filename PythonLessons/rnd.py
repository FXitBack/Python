import random

random_number = random.randint(1, 5)
user_number = int(input('Угадай число (от 1 до 5): '))
if random_number == user_number:
    print("Ты угадал число " + str(random_number))
else:
    print("Ты не угадал число " + str(random_number))    # вариант 1
    print(f"Ты не угадал число {random_number}")         # вариант 2