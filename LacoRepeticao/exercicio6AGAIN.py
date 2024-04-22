#6. Ler X notas de N estudantes e exibir a media da turma:

numeroEstudante = int(input("Insira o numero de alunos: "))
notasEstudante = int(input("Insira o numero de alunos: "))
soma = 0

for estudante in range(numeroEstudante):
    for nota in range(notasEstudante):
        soma += float(input(f"{estudante + 1}º estudante, {nota + 1}º nota: "))

print(f"Média da turma: {soma / (notasEstudante * numeroEstudante)}")