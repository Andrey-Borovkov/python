import math
print('Введите значение коордитаны Х первой точки:')
x1 = int(input())
print('Введите значение коордитаны Y первой точки:')
y1 = int(input())
print('Введите значение коордитаны Х второй точки:')
x2 = int(input())
print('Введите значение коордитаны Y второй точки:')
y2 = int(input())
result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(round(result,3))