from copy import deepcopy as dp

def isPrime(n):
    if n <= 1: 
        return False
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True

def getPrimes(P,S):
    primes = []
    for i in range(P+1,S+1):
        if isPrime(i):
            primes.append(i)
    return primes
    
def verificar(N,S,lista,disp):
    if sum(lista)==S and len(lista)==N:
        resp.append(lista)
        return
        
    elif (sum(lista)>S) or (sum(lista)<S and len(lista)==N) or (sum(lista)==S and len(lista)<N):
        return
    
    else:
        listaConNumero = dp(lista)
        listaConNumero.append(disp[0])
        listaSinNumero = dp(lista)

        if len(disp[1:])>0:
            verificar(N,S, listaConNumero, disp[1:])
            verificar(N,S, listaSinNumero, disp[1:])
 
 def problema(N,P,S):
    global resp
    resp=[]
    primos = getPrimes(P,S) 
    lista=[]
    verificar(N,S,lista,primos)
    return resp
    
