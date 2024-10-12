import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Application")
window.geometry("500x500")

canvas = Canvas(window, bg = "white", height = 485, width = 485)

n = input()
n = int(n)
if n == 1:
    squareL = 150
elif n == 2:
    squareL = 50
elif n == 3:
    squareL = 17
elif n == 4:
    squareL = 5
elif n == 5:
    squareL = 1


#################EndSierp######################

def afismat(m, n):#
    x = y = 1
    for i in range(1, 3**n + 1):
        for j in range(1, 3**n + 1):
            if(m[i][j] == '. '):
                point = canvas.create_rectangle(x, y, x + squareL, y + squareL, fill = "black")
            y += squareL + 1
        y = 1
        x += squareL + 1

M = []

for i in range(3 ** n + 1):  # + 1 pt a permite indexarea liniilor de la 1
    linie = ["0 "] * (3 ** n + 1)  # -//----------------------- coloanelor de la 1
    M.append(linie)

def Sierping(i, j, lvl):
    iMidNW = i - int((3 ** (lvl - 1)) / 2)
    jMidNW = j - int((3 ** (lvl - 1)) / 2)

    for a in range(iMidNW, iMidNW + 3 ** (lvl - 1)):
        for b in range(jMidNW, jMidNW + 3 ** (lvl - 1)):
            M[a][b] = '. '

    if lvl > 1:
        Sierping(i - (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j, lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i, j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j, lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i, j - (3 ** (lvl - 1)), lvl - 1)


Sierping(int((3 ** n) / 2) + 1, int((3 ** n) / 2) + 1, n)

#################EndSierp######################
afismat(M, n)
canvas.location(x = 0, y = 0)
canvas.pack()
window.mainloop()

