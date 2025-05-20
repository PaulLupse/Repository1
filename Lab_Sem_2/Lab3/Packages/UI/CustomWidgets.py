import tkinter.ttk as ttk
import tkinter as tk

class ImprovedComboBox(ttk.Combobox):
    def __init__(self, master, values, width, pack):
        self.StringVariable = tk.StringVar(master, values[0])
        super().__init__(master, width = width, textvariable=self.StringVariable)
        self['values'] = values

        self.bind('<KeyPress>', self.Search)
        self.bind('<KeyRelease>', self.Search)

        if pack is True:
            self.pack()

    def Search(self, event):
        searchValue = event.widget.get()
        goodValues = []
        if searchValue == '' or searchValue == " ":
            goodValues = self['values']
        else:
            goodValues = [name for name in self['values'] if searchValue.lower() in name.lower()]

        self['values'] = goodValues

class LabeledEntry(ttk.Entry):
    def __init__(self, master, label_text, label_position, gridding_options, **options):
        self.frame = tk.Frame(master)
        super().__init__(self.frame, **options)
        self.label = tk.Label(self.frame, text = label_text)

        if label_position == 'n':
            self.grid(row = 1, column = 0)
            self.label.grid(row = 0, column = 0)
        elif label_position == 'w':
            self.grid(row = 0, column = 1)
            self.label.grid(row = 0, column = 0)
        elif label_position == 's':
            self.grid(row = 0, column = 0)
            self.label.grid(row = 1, column = 0)
        else:
            self.grid(row = 0, column = 0)
            self.label.grid(row = 0, column = 1)

        self.frame.grid(gridding_options)

class LabeledText(tk.Text):
    def __init__(self, master, label_text, label_position, gridding_options, **options):
        self.frame = tk.Frame(master)
        super().__init__(self.frame, **options)
        self.label = tk.Label(self.frame, text = label_text, justify = 'center', wraplength=300)

        if label_position == 'n':
            self.grid(row = 1, column = 0)
            self.label.grid(row = 0, column = 0)
        elif label_position == 'w':
            self.grid(row = 0, column = 1)
            self.label.grid(row = 0, column = 0)
        elif label_position == 's':
            self.grid(row = 0, column = 0)
            self.label.grid(row = 1, column = 0)
        else:
            self.grid(row = 0, column = 0)
            self.label.grid(row = 0, column = 1)

        self.frame.grid(gridding_options)

class PopupWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.grab_set()

    def destroy_and_release(self):
        self.grab_release()
        self.destroy()
