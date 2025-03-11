import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import threading as thrd
import time
import random

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Application Front End

win = tk.Tk()
win.title("Thingy2")
win.resizable(False, False)



win.mainloop()