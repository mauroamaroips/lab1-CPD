import timeit
import numpy as np

rnd = np.random
n = [1000, 10000, 100000, 1000000, 10000000, 20000000]
bwRAM = [0] * len(n)

for k in range(len(n)):
    melhorTempo = [99999] * len(n)  # Um valor muito grande
    vetor = rnd.randint(1000, size=n[k])
    for i in range(3):  # Efetua 3 medições de tempo e mostra a melhor
        print(f"Medição {i + 1} para {n[k]} elementos...")

        starttime = timeit.default_timer()
        soma = 0.0
        for j in range(n[k]):
            soma += vetor[j]
        tempo = timeit.default_timer() - starttime # Pergunta 1.1 - Tempo da soma dos elementos dos vetores

        print(f"\t {tempo} segundos")
        if tempo < melhorTempo[k]:
            melhorTempo[k] = tempo

    bwRAM[k] = n[k] * 4 / melhorTempo[k] / (1024 * 1024)
    # print(f"Melhor tempo da soma para {n[k]} elementos: {melhorTempo} segundos")
    print(f"Largura de banda da RAM: {n[k] * 4 / melhorTempo[k] / (1024 * 1024):.2f} Mega Bytes por segundo")

# Print de testes
for i in bwRAM:
    print(i)
print(f"Média de largura de banda: {sum(bwRAM) / len(bwRAM):2f}")


# print(vetor.dtype)

# Pergunta 1.2 - A expressão acima utiliza o número de elementos do vetor (cada inteiro apresenta 4 bits), tem em conta o
# melhor tempo obtido entre as iterações e o 1024^2 representa a conversão de bytes para megabytes
# 1KB = 1024B  1MB = 1024KB