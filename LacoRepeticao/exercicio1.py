# Lista de laços de repetição


#1. Idades: (ler uma quantidade indeterminada de idades até um número negativo ser digitado)
idade = 1
while idade > 0:
    idade = int(input("Digite a sua idade: "))
    print(idade)

# Outra maneira de fazer:   
while True: 
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        break 
    print(idade)
