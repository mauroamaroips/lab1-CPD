import timeit
import numpy as np

rnd = np.random

# n define a dimensão das matrizes (500 linhas e 500 colunas)
n = 500
matriz1 = rnd.uniform(0, 500, size=(n, n))
matriz2 = rnd.uniform(0, 500, size=(n, n))

#matriz1 = [[1, 2], [3, 4]]
#matriz2 = [[-1, 3], [4, 2]]
resultado = np.zeros((n, n))

# Multiplicação de matrizes
starttime = timeit.default_timer()
for i in range(n):  # número de linhas da primeira matriz
    for j in range(n):  # número de linhas da segunda matriz
        temp = 0
        for k in range(n):  # número de elementos na linha/coluna
            temp += matriz1[i][k] * matriz2[k][j]
        resultado[i][j] = temp
print(f"Tempo para multiplicação de matrizes: {timeit.default_timer() - starttime}")

#print(matriz1)
#print(matriz2)
#print(resultado)

#Multiplicação de matrizes utilizando a função matmul da biblioteca NumPy

np.matmul(matriz1, matriz2)
print(f"Tempo para multiplicação de matrizes: {timeit.default_timer() - starttime}")


