def nrdiv(n):
    d = 2
    nrdiv = 1
    while d <= n:
        if n % d == 0:
            nrdiv += 1
        d += 1
    return nrdiv

def numere_cu_k_divizori(lista, k):
    l = []
    for i in lista:
        if(nrdiv(i) >= k):
            l.append(i)
    return l
print(numere_cu_k_divizori([12, 15, 7, 24, 9], 4))


