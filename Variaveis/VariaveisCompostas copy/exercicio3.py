#3. Inverter o vetor (Inverter a ordem dos valores de uma lista)

lista = [900,679,450,890]
lista.reverse()
print(lista)

#ou 

lista = [900,679,450,890]

for i in range(len(lista)//2):
    aux = lista[-(i+1)]
    lista[-(i+1)] = lista[i]
    lista[i] = aux
