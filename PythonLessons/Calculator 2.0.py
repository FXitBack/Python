import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.CYAN)

expr = input("Введите математическое выражение: ")
result = numexpr.evaluate(expr)

print(Fore.YELLOW)
print(Style.BRIGHT)
print(f"Ответ {result}")


"""
Coloroma - цвета, фон и тд
Numexpr - Для калькулятора
pyinstaller - Для создания программы .exe
"""