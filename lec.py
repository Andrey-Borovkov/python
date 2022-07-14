print('Введите цифру от 1 до 7')
a = int(input())
if not (a in range(1, 8)):
    print('Введенная цифра не из диапозона от 1 до 7')
elif a in range(1, 6):
    print('Будний день')
else:
    print('Выходной день')
