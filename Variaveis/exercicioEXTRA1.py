## Extras

#1. Calcular hipotenusa:

#to importando "sqrt", p/ calcular ao quadrado 
from math import sqrt

cateto_adjacente = float(input("Insira o valor do cateto adjacente: "))
cateto_oposto = float(input("Insira o valor do cateto oposto: ")) 

hipotenusa = ((cateto_adjacente * cateto_adjacente) + (cateto_oposto * cateto_oposto))

print(f"O valor da hipotenusa é: {hipotenusa}")