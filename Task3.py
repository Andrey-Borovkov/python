#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значение Х:')
x = int(input())
print('Введите значение Y:')
y = int(input())
print('Введите значение Z:')
z = int(input())
if not (x and y and z) == (not x) or (not y) or (not z):
    print('Утверждение истино')
else:
    print('Утверждение НЕ истино')