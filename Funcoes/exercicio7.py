#7. Crie uma função que retorne uma lista com os N primeiros termos de fibonacci:

def termosFibonacci(N):
    fibonnaci = []
    N1 = 1
    N2 = 1 
    for m in range(2, N):
        aux = N1 + N2
        fibonnaci.append(aux)
        N1 = N2
        N2 = aux
    return fibonnaci

N = int(input("N: "))
print(termosFibonacci(N))