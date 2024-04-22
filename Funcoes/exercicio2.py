#2. Crie uma função para calcular a hipotenusa de um triângulo:

#sqrt --> importo ela da library p/ calcular raiz quadrada

from math import sqrt

def hipotenusa(catetoAdjacente, catetoOposto):
    return sqrt(catetoAdjacente + catetoOposto)

catetoAdjacente = float(input("cateto adjacente: "))
catetoOposto = float(input("cateto oposto: "))

print(hipotenusa(catetoAdjacente, catetoOposto))
