#4. Animais (Preencher um vetor com o nome de N animais)

N = int(input("Insira o numero de animais:" ))

listaAnimais = []

for i in range(N):
    animal = input("Insira o nome do animal: ")
    listaAnimais.append (animal)

print(listaAnimais)