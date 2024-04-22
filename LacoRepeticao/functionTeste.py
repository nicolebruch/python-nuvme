#É impar ou par com function (Java) == def (Python)

def ehPar (N):
    if (N % 2 ==  0):
        return "eh par"    
    else:
        return "eh impar"
    
N = int(input("Insira um número: "))
print(ehPar(N))
    
    