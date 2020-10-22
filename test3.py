# Составить алгоритм: на входе есть числовой массив,
# необходимо вывести элементы массива кратные 3
from array import *

print('Input array of integer')
x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])
    if x[i] % 3 == 0:
        print(x[i])
input() 