#4. Crie uma função para calcular a média de um aluno e dizer se está aprovado ou reprovado:

def aprovacao():
    soma = 0
    
    for qntNota in range(3):
        nota = int(input("numero: "))
        soma += nota
    media = soma / 3
    if media >= 7:
        return("Aprovado" , media)
    return("Reprovado" , media)
    
print(aprovacao())
