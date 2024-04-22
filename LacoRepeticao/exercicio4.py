#4. Exibir a quantidade de habitantes de uma cidade: (Ler uma população inicial, taxa de crescimento e tempo de estimativa)

populacaoInicial = int(input("Insira valor da população inicial: "))
taxaCrescimento = int(input("Insira taxa de crescimento: "))
tempoEstimativa = int(input("Insira tempo de estimativa: "))
taxaCrescimento = taxaCrescimento / 100

for infos in range(tempoEstimativa):
    populacaoInicial = populacaoInicial + (populacaoInicial * taxaCrescimento)
    print(f"População inicial no {infos + 1}º ano: {populacaoInicial}")
    print(f"População final: {int(populacaoInicial)}")