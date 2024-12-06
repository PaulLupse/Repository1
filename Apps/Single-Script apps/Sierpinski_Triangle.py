import tkinter as tk
from tkinter import *
from tkinter.ttk import *

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n = 0

window = tk.Tk()
window.title("Sierpinski Triangle")
window.geometry("850x768")
canvas = Canvas(window, height = 732, width= 732, background="white")

def drawPattern():
    canvas.delete("all")
    Sierping(Coord(x=365, y=2),
             Coord(x=2, y=729),
             Coord(x=729, y=729),
            lvl=int(v.get()))

def Sierping(a, b, c, lvl):
    canvas.create_line(a.x, a.y, b.x, b.y, width = 0, fill = "black")
    canvas.create_line(b.x, b.y, c.x, c.y, width=0, fill = "black")
    canvas.create_line(c.x, c.y, a.x, a.y, width=0, fill = "black")

    halfAB = Coord((a.x + b.x)/2, (a.y + b.y)/2)
    halfAC = Coord((a.x + c.x)/2, (a.y + c.y)/2)
    halfBC = Coord((b.x + c.x)/2, (b.y + c.y)/2)

    if lvl > 1 :
        Sierping(a, halfAB, halfAC, lvl - 1)
        Sierping(halfAB, b, halfBC, lvl - 1)
        Sierping(halfAC, halfBC, c, lvl - 1)

valori = {
    "Level 1" : "1",
    "Level 2" : "2",
    "Level 3" : "3",
    "Level 4" : "4",
    "Level 5" : "5",
    "Level 6" : "6",
    "Level 7" : "7",
    "Level 8" : "8"
}

v = StringVar(window, '1')

j = 30
for (text, value) in valori.items():
    Radiobutton(window, text = text, variable = v, value = value).place(x = 5, y = j, anchor = NW)
    j += 20

select = Label(text = "Select level:")
generate = Button(text = "GENERATE", command = drawPattern)
exit = Button(text = "EXIT", command = window.destroy)

select.place(x = 5, y = 10)
generate.place(x = 5, y = 220, anchor = NW)
exit.place(x = 5, y = 250, anchor = NW)

canvas.place(anchor = NW, x = 100, y = 1)
window.mainloop()
