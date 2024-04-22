## Extras

#1. Escrever um algoritmo de divisão inteira por subtração sucessiva:

divisor = int(input("Insira um divisor: "))
dividendo = int(input("Insira um dividendo: "))
quo = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    quo += 1
    
print(f"O algoritmo da divisão é: {quo}")
 

