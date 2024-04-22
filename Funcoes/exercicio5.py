#5. Use a função do exercício 4 para calcular a média de N alunos:

def media():
    numeroAlunos = int(input("numero de alunos: "))
    total = 0

    for aluno in range(numeroAlunos):
        somaNota = 0
        for notas in range(3):
            nota = int(input("nota: "))
            somaNota += nota
        total += somaNota / 3  

    media = total / numeroAlunos  
    return media

print(media())


