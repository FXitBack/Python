# Простое , Четное, Кратно
number = int(input("Введите число "))
is_simple = True
for i in range(2, number // 2 ):
    if number % i == 0:
        is_simple = False
        break

is_even = number % 2 == 0
is_divided_by_5 = number % 5 == 0

print(f"Число {number}:")
print(f"- Простое: {'да' if is_simple else 'нет'}")
print(f"- Четное: {'да' if is_even else 'нет'}")
print(f"- Кратно 5: {'да' if is_divided_by_5 else 'нет'}")

num1 = float(input("Первое число: "))
num2 = float(input("Второе число: "))
op = (input("Введите оерацию (*,+,-,/) :"))

# Калькулятор
if op == "*":
    result = num1 * num2
elif op == "+":
    result = num1 + num2
elif op == "/":
    result = num1 / num2
elif op == "-":
    result = num1 - num2
print(f"Результат:, {result}")

# Конвертер не работает
amount = float(input("Введите сумму:"))
original = input("Введите валюту:")
to = input("Введите валюту конвертации:")

if original == "USD" and to == "EUR":
   result = amount * 0.93
   print(f"{result} EUR")
elif original == "EUR" and to == "USD":

# Циклы

for i in range(1, 6, 2):
    print(i)

count = 0
word = "Hello world!"
for i in word:
   if i == "l":
       count += 1
print("Count", count)

i = 5
while i <= 15:
    print(i)
    i += 2

isHasCar = True

while isHasCar:
    if input("Enter data: ") == "Stop":
        isHasCar = False

for i in range(1, 11):
    if i >= 5:
        break
    if i % 2 == 0:
        continue
    print (i)

found = None
for i in "hello":
    if i == "l":
        found = True
        break
else:
    found = False

print(found)

nums = [5, 7, 2, 4, 6, True, "Hello", [1, 5]]

nums[0] = 50
nums[5] = 2

print(nums[-1][0])

numbers = [5, 2, 7, False]
# numbers[3] = 100
numbers.append(100)
# append () добавляет в конец списка
numbers.insert(1, True,)

b = (5, 6, 8)
numbers.extend(b)
# Метод extend расширяет список, добавляя элементы
numbers.sort()
# Метод sort сортирует элементы списка в возрастающем или убывающем порядке
numbers.reverse()
# разворачивает последовательность.
# Возвращает элементы последовательности в обратном порядке
numbers.pop(-2)
# Метод pop() удаляет элемент по индексу и возвращает его.
# Если не указывать параметры, то будет удален последний элемен
numbers.remove(6)
# Метод remove (): удаление по значению. remove() можно использовать,
# когда мы точно знаем значение, от которого хотим избавиться
numbers.clear()
# удаляет все
print(numbers.count(True))
print(len(numbers))
