#6. Imposto de renda, calcule de acordo com a tabela de progressão:

salario = float(input("Insira sua renda: "))

if (salario < 1900):
   taxa = 0

elif (salario < 2800):
    taxa = 7.5

elif (salario < 3750):
    taxa = 15

elif (salario < 4800):
    taxa = 22.5

elif (salario > 4800):
    taxa = 27.5

else:
    taxa = 27.5
desconto = salario * (taxa / 100)
salario_liquido = salario - desconto 
print(f"{salario_liquido:.2f}")


