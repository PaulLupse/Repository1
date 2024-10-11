# Algoritmul lui Lee

from collections import deque
from pathlib import Path

def afismat(m): #afiseaza matricea m
    for i in m:
        for j in i:
            if j == -1:
                print("#", end = ' ')
            else: print(j, end = ' ')
        print()

di = [-1, 0, 1, 0]; dj = [0, 1, 0, -1]

def Lee(istart, jstart):
    coada = deque([[istart, jstart]])
    M[istart][jstart] = 1
    while(bool(coada)):
        front = coada[0]
        ifront = front[0]; jfront = front[1]
        for k in range(4):
            itarget = ifront + di[k]; jtarget = jfront + dj[k]
            if M[itarget][jtarget] == 0:
                M[itarget][jtarget] = M[ifront][jfront] + 1
                coada.append([itarget,jtarget])
        coada.popleft()

path = Path(__file__).with_name("Input.in")
f = open(path, 'r')
n, m = f.readline().split(); n = int(n); m = int(m) # n - nr. linii. m - nr. coloane
M = []

border = [-1] * (n + 2)
M.append(border) # bordare matrice sus

for i in range(0,n):
    linie = []
    for j in f.readline().split():
        if int(j) == 1: # 1 = obstacol
            linie.append(-1) 
        else: linie.append(0)
    linie.insert(0, -1) # bordare linie stanga
    linie.append(-1)    # bordare linie dreapta
    M.append(linie)

M.append(border) #bordare jos
Lee(1, 1)
afismat(M)
