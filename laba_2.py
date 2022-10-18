"""
19. Вычислить сумму знакопеременного ряда (-1)^(n-1)*(|х^(2n-2)|)/(2n-2)!,
где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная.
"""

import random
import numpy as np
from numpy import linalg
import math

print("\nРезультат работы программы:")

K = int(input('Введите размерность квадратной матрицы больше 1 и меньше 31:'))
while (K < 1) or (K > 31):
    K = int(input("Вы ввели неверное число. " 
"\nВведите количество строк (столбцов) квадратной матрицы больше 1 и меньше 31:"))

X = np.random.randint(5, size=(K,K))
print("Матрица:\n", X)

precision = int(input('Введите количество знаков после запятой в результате вычисления: '))
precision = 0.1**precision

fact = 1
n = 1
summa = 0
delta = 0
drob = 1
while abs(drob) > precision:
    delta += summa
    if n % 2 == 1:
        summa += -1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n - 2))) / fact)
    else:
        summa += 1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n - 2))) / fact)
    n += 1
    fact = fact * (2 * n - 2) * (2 * n - 3)
    drob = delta - summa
    delta = 0
    print(n - 1, ':', summa, ' ', drob)
print('Сумма знакопеременного ряда:', summa)