import math

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
operator = (input('Введите операцию (-, +, *, /, %, **, //,): '))
result = 0
if operator == "-":
    result = a - b
elif operator == "+":
    result = a + b
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b
elif operator == "//":
    result = a // b
elif operator == "%":
    result = a % b
elif operator == "**":
    result = a ** b
print(f"Результат:  {result}")