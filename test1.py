# Составить алгоритм: если введенное число больше 7, то вывести “Привет”

print('Введите любое число')
x = float(input())
if isinstance(x, (float, int)):
    if x > 7:
     print("Привет")
     input()