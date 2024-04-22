#2. Calcular salário, considerando a tabela de IR(15%), calcule o salário líquido após a dedução:

salario = float(input("Insira seu salário: "))
taxa = int(input("Insira a taxa: "))

desconto = salario * (taxa/100)

salario_liquido = salario - desconto
print(salario_liquido)
