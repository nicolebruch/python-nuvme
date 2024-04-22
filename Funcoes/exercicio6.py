#6. Crie uma função que retorne um vetor com os primeiros N quadrados:

def numerosQuadrado(N):
    quadrados = []  
    for i in range(1, N + 1):  
        quadrados.append(i * i) 
    return quadrados
N = int(input("N: "))  

print(numerosQuadrado(N))  
