#1. Calcular áreas:

  # b) Calcular área de círculo: (dica, importe a constante PI)

raio = float(input("Raio: "))
area_circulo = raio ** 2 * 3.14 

print(area_circulo)

#Forma p/ importar o PI, sem precisar inserir o valor dele

from math import pi 
raio = float(input("Raio: "))
area = raio * raio 
print(f"Área: {area}")