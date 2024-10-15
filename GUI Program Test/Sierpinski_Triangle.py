import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = int(input())

window = tk.Tk()
window.title("Sierpinski Triangle")
window.geometry("768x768")

canvas = Canvas(window, height = 732, width= 732, background="white")

def Sierping(a, b, c, lvl):
    canvas.create_line(a.x, a.y, b.x, b.y, width = 0, fill = "black")
    canvas.create_line(b.x, b.y, c.x, c.y, width=0, fill = "black")
    canvas.create_line(c.x, c.y, a.x, a.y, width=0, fill = "black")

    halfAB = Coord((a.x + b.x)/2, (a.y + b.y)/2)
    halfAC = Coord((a.x + c.x)/2, (a.y + c.y)/2)
    halfBC = Coord((b.x + c.x)/2, (b.y + c.y)/2)

    if(lvl > 1):
        Sierping(a, halfAB, halfAC, lvl - 1)
        Sierping(halfAB, b, halfBC, lvl - 1)
        Sierping(halfAC, halfBC, c, lvl - 1)

Sierping(Coord(x = 365,y = 2),Coord(x = 2, y = 729) , Coord(x = 729,y = 729), lvl = n)

canvas.pack()
window.mainloop()
