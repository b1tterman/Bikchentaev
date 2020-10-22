# Составить алгоритм: если введенное число больше 7, то вывести “Привет”

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

print('Введите любое число')
x = float(input())
if is_float(x):
    if x > 7:
     print("Привет")
     input()