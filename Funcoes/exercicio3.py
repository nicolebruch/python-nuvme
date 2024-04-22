#3. Crie uma função para determinar se um número é par ou ímpar:

def parOuImpar():

    while True: 
        numero = int(input("numero: "))
        if numero % 2 == 0:
            return("parzao")
        
print(parOuImpar())



