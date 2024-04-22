#4. Calcular quantidade de cédulas: (relativamente difícil)

valor = int(input("Insira valor da cédula: "))

notas_200 = valor // 200
resto = valor % 200

notas_100 = valor // 100
resto = valor % 100

notas_50 = valor // 50
resto = valor % 50

notas_20 = valor // 20
resto = valor % 20

notas_10 = valor // 10
resto = valor % 10

notas_5 = valor // 5 
resto = valor % 5

notas_2 = valor // 2
resto = valor % 2

nota_1 = resto 

print(f"Notas de 200:{notas_200}")
print(f"Notas de 100:{notas_100}")
print(f"Notas de 50:{notas_50}")
print(f"Notas de 20:{notas_20}")
print(f"Notas de 10:{notas_10}")
print(f"Notas de 50:{notas_5}")
print(f"Notas de 1:{nota_1}")

