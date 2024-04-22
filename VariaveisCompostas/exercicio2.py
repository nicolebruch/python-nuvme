#2. Onde está o maior? (A partir de um vetor, encontrar o maior valor)

lista = [900,6,20,506,13,6]
maior = 0

for i in range(1, len(lista)):
    if lista[i] > lista[maior]:
        maior = i
    
    print("indice", maior)
    print("numero", lista[maior])