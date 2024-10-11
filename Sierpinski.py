# Algoritm care genereaza covorul lui Sierpinski reprezentat in matrice patratica

from pathlib import Path

path = Path(__file__).with_name("Output.out")

def afismat(m, n): # afiseaza matricea m
    fOut = open(path, "w") # suprascrie fisierul Output
    for i in range(1, 3**n + 1):
        for j in range(1, 3**n + 1):
            if m[i][j] == -1:
                fOut.write(". ")
            else: fOut.write(str(m[i][j]) + " ")
        fOut.write("\n")

M = []
fIn = open(Path(__file__).with_name("Input.in"), "r")
n = int(fIn.read())

for i in range(3**n + 1):    # + 1 pt a permite indexarea liniilor de la 1
    linie = [0] * (3**n + 1) # -//----------------------- coloanelor de la 1
    M.append(linie)

def Sierping(i, j, lvl):
    iMidNW = i - int((3 ** (lvl - 1)) / 2)
    jMidNW = j - int((3 ** (lvl - 1)) / 2)

    for a in range(iMidNW, iMidNW + 3 ** (lvl - 1)):
        for b in range(jMidNW, jMidNW + 3 ** (lvl - 1)):
            M[a][b] = -1

    if lvl > 1:
        Sierping(i - (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j                   , lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i                   , j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j                   , lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i                   , j - (3 ** (lvl - 1)), lvl - 1)
afismat(M, n)
Sierping(int((3**n)/2) + 1, int((3**n)/2) + 1, n)
afismat(M, n)