#1. Crie uma função pra calcular a área de um triângulo:

base = float(input("base: "))
altura = float(input("altura: "))

def areaTriangulo(base,altura):
    return((base * altura) / 2)
print(areaTriangulo(base,altura))


