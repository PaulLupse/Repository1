import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Application")
window.geometry("768x768")

canvas = Canvas(window, bg = "black", height = 730, width = 730)

n = input()
n = int(n)

def Sierping(i, j, lvl):
    half = (3**(lvl - 1))//2
    i1 = i - half; j1 = j - half; i2 = i + half + 1; j2 = j + half + 1

    point = canvas.create_rectangle(i1, j1, i2, j2, fill="white", outline="")
    if lvl > 6-n+1:
        Sierping(i - (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j, lvl - 1)
        Sierping(i - (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i, j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j + (3 ** (lvl - 1)), lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j, lvl - 1)
        Sierping(i + (3 ** (lvl - 1)), j - (3 ** (lvl - 1)), lvl - 1)
        Sierping(i, j - (3 ** (lvl - 1)), lvl - 1)

Sierping(i = 366, j = 366, lvl = 6)
canvas.location(x = 0, y = 0)
canvas.pack()
window.mainloop()

