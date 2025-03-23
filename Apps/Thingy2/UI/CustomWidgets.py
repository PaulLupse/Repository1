import tkinter as tk
import tkinter.ttk as ttk
import numpy as np

class ImprovedComboBox:
    def __init__(self, master, values, width, pack):
        self.StringVariable = tk.StringVar()
        self.comboBox = ttk.Combobox(master = master, textvariable = self.StringVariable, width = width)
        self.values = values
        self.comboBox['values'] = values

        self.comboBox.bind('<KeyPress>', self.Search)
        self.comboBox.bind('<KeyRelease>', self.Search)

        if pack is True:
            self.comboBox.pack()

    def Search(self, event):
        searchValue = event.widget.get()
        goodValues = []
        if searchValue == '' or searchValue == " ":
            goodValues = self.values
        else:
            goodValues = [name for name in self.values if searchValue.lower() in name.lower()]

        self.comboBox['values'] = goodValues

class Map(tk.Canvas):
    def __init__(self, master, width, height, map_type, visited_colour, queued_color):
        super().__init__(master, width = width, height = height)
        self.map_type = map_type

        if self.map_type == 'matrix':
            self.matrix_size = 3
            self.matrix = np.ndarray((3, 3), dtype = np.int64)
        else:
            ...


