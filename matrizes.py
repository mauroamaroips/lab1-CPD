import timeit
import numpy as np

rnd = np.random
# n define as dimensões dos vetores e da matriz
n = 5000
vetor = rnd.uniform(0, 1000, size=n)
matriz = rnd.uniform(0, 1000, size=(n, n))
resultado = np.zeros(n)

# primeira implementação
starttime = timeit.default_timer()
for i in range(len(matriz)):  # número de linhas da matriz
    for j in range(len(vetor)):  # número de elementos no vetor
        resultado[i] += matriz[i, j] * vetor[i]
print(f"Tempo 1: {timeit.default_timer() - starttime}")
print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")

# segunda implementação
starttime = timeit.default_timer()
for i in range(len(matriz)):  # número de linhas da matriz
    temp = 0
    for j in range(len(vetor)):  # número de elementos no vetor
        temp += matriz[i, j] * vetor[i]
    resultado[i] = temp
print(f"Tempo 2: {timeit.default_timer() - starttime}")
print(f"Primeiros elementos do vetor resultado: {resultado[0:5]}")

# Pergunta 1.1 - A segunda implementação é mais performante pois o 2º ciclo for não faz,a cada iteração,
# o update do valor na lista. Esta vai guardando a soma entre cada iteração e apenas no fim do ciclo e apenas no
# fim atribui o valor ao respetivo index.

# Pergunta 1.2 - Variando os valores de n entre 500 e 5000, o tempo de execução é maior quão maior for o valor de n.
# A diferença nos tempos de execução torna-se mais acentuada quanto maior for n.