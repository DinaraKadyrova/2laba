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
X = np.zeros((K,K),dtype=int) #создаём матрицу Х

for i in range(K):
    for j in range(K):
        X[i][j] = np.random.randint(-5, 5) #заполняем матрицу рандомными числами
print(X)

precision = float(input("Введите точность: "))
n = 1
fact = 1
summa = 0
fg = 0
difference = 1
while abs(difference) > precision:
    fg += summa
    if n % 2 == 1:
        summa += -1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n - 2))) / fact)
    else:
        summa += 1 * ((np.linalg.det(linalg.matrix_power(X, 2 * n - 2))) / fact)
    n += 1
    fact = fact * (2 * n - 2) * (2 * n - 3)
    difference = abs(fg-summa)
    fg = 0
    print(n-1, ':', summa, ' ', difference)
print('Сумма знакопеременного ряда:', summa)


