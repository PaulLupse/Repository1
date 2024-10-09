from collections import deque

def afismat(m): #afiseaza matricea m
    for i in m:
        print(i)

di = [-1, 0, 1, 0]; dj = [0, 1, 0, -1]
def Lee(istart, jstart):
    coada = deque[[istart, jstart]]



f = open(r"C:\Users\Paul\Documents\GitHub\Repository1\Input.in", 'r')
n, m = f.readline().split()
M = []
for i in range(0, int(n)):
    linie = []
    for j in f.readline().split():
        linie.append(int(j))
    linie.insert(0, 1)
    M.append(linie)
