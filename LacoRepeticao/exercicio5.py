#5. Exibir os termos da sequência de fibonacci: (Ler um N e exibir até o enésimo termo da sequência)

N = int(input("Insira o valor de N: "))
N1 = 1
N2 = 1

if N <= 2:
    print(1)
else: 
    for fibonacci in range(2, N):
        aux = N1 + N2
        N1 = N2
        N2 = aux
        print(aux)
