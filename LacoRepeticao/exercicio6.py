#6. Ler 3 notas de N alunos e exibir média da turma:

numeroAlunos = int(input("Insira o numero de alunos: "))
total = 0

for alunos in range(numeroAlunos):
    for notas in range(3):
        total =+ float(input (f"{alunos + 1}º aluno, {notas + 1}º nota:"))

print(f"Média da turma: {total / (3 * numeroAlunos)}")