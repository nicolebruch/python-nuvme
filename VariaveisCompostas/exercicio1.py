#1. Preenchimento de Vetor (Preencher um vetor com os quadrados de 1 até N)

N = int(input("Insira o valor de N:" ))

listaQuadrados = []

for i in range(1, N + 2):
    
    listaQuadrados.append (i * i)

print(listaQuadrados)