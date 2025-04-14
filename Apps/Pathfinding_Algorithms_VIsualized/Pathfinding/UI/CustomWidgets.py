import tkinter as tk
import tkinter.ttk as ttk
import numpy as np

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

class Map(tk.Canvas):
    def __init__(self, master, width, height, map_type, **kwargs):
        super().__init__(master, width = width + 18, height = height + 16, bd = 0, bg = 'black', highlightcolor='gray', highlightbackground='gray')
        self.map_type = map_type
        self.width = int(width)
        self.height = int(height)
        self.square_size = 0
        self.drag_start = (0, 0)
        self.drag_end = (0, 0)
        self.selected = []
        self.prev_selected = 0
        self.first = 0
        self.editing = True
        self.brush_is_active = False
        self.eraser_is_active = False
        self.eraser_size = 5
        self.left_clicked = False
        self.starting_point_id = None
        self.target_point_id = None
        self.mouse_pos = (0, 0)
        self.selection_rectangle_id = None

        self.prev = 0

        if self.map_type == 'matrix':
            self.matrix_size = 0
            self.matrix = np.ndarray((0, 0), dtype = square)
            self.square_id_to_pos = np.zeros((self.matrix_size, 2), dtype = np.int64)
        else:
            ...

        if kwargs:
            self.grid(kwargs)
        else:
            self.pack()

        self.bind('<Button-1>', self.left_click)
        self.bind('<Button-3>', self.start_to_drag)
        self.bind('<ButtonRelease-3>', self.end_drag)


        self.context_menu = tk.Menu(self, tearoff = 0, foreground='black')
        self.context_menu.add_command(label = 'Set to obstacle', command = self.set_to_obstacle)
        self.context_menu.add_command(label = 'Set to normal', command = self.set_to_normal)
        self.context_menu.add_separator()
        self.context_menu.add_command(label = 'Set starting point', command = self.set_to_start)
        self.context_menu.add_command(label = 'Set target point', command = self.set_to_target)

    def init_square_grid(self, matrix_size, square_size):
        self.prev += self.matrix_size ** 2
        self.delete('all')
        self.square_size = square_size
        border_width = 2 * (square_size > 10) + 1 * (square_size <= 10)
        self.config(width = matrix_size * square_size + matrix_size * border_width + (border_width == 1) * 2, height = matrix_size * square_size + matrix_size * border_width + (border_width == 1) * 2)
        self.matrix_size = matrix_size
        self.matrix.resize((matrix_size, matrix_size))
        self.square_id_to_pos.resize((matrix_size ** 2 + 2, 2))

        for i in range(0, matrix_size):
            for j in range(0, matrix_size):
                Square = square(self, 3 + i * square_size + i * border_width, 3 + j * square_size + j * border_width, square_size)
                self.square_id_to_pos[Square.id - self.prev][0] = j
                self.square_id_to_pos[Square.id - self.prev][1] = i
                self.matrix[j][i] = Square

        self.matrix[0][0].set_start()
        self.matrix[matrix_size - 1][matrix_size - 1].set_target()

        self.starting_point_id = self.matrix[0][0].id
        self.target_point_id = self.matrix[matrix_size - 1][matrix_size - 1].id

    def left_click(self, event):
        self.left_clicked = True
        for square_id in self.selected:
            self.itemconfigure(square_id, outline='black')

    def left_click_release(self, event):
        self.left_clicked = False

    def set_to_obstacle(self):
        for square_id in self.selected:
            self.matrix[self.square_id_to_pos[square_id - self.prev][0]][self.square_id_to_pos[square_id - self.prev][1]].set_obstacle()
            self.itemconfigure(square_id, outline='black')

    def set_to_normal(self):
        for square_id in self.selected:
            self.matrix[self.square_id_to_pos[square_id- self.prev][0]][self.square_id_to_pos[square_id- self.prev][1]].set_normal()
            self.itemconfigure(square_id, outline='black')

    def set_to_start(self):
        try:
            square_id = self.selected[0]
            if self.starting_point_id is not None:
                if self.matrix[self.square_id_to_pos[self.starting_point_id- self.prev][0]][self.square_id_to_pos[self.starting_point_id- self.prev][1]].type == 2:
                    self.matrix[self.square_id_to_pos[self.starting_point_id- self.prev][0]][self.square_id_to_pos[self.starting_point_id- self.prev][1]].set_normal()
            self.matrix[self.square_id_to_pos[square_id- self.prev][0]][self.square_id_to_pos[square_id- self.prev][1]].set_start()
            self.itemconfigure(square_id, outline='black')
            self.starting_point_id = square_id
        except:
            square_id = self.selected[0]
            if self.starting_point_id is not None:
                if self.matrix[self.square_id_to_pos[self.starting_point_id - self.prev][0]][
                    self.square_id_to_pos[self.starting_point_id - self.prev][1]].type == 2:
                    self.matrix[self.square_id_to_pos[self.starting_point_id - self.prev][0]][
                        self.square_id_to_pos[self.starting_point_id - self.prev][1]].set_normal()
            self.matrix[self.square_id_to_pos[square_id - self.prev][0]][
                self.square_id_to_pos[square_id - self.prev][1]].set_start()
            self.itemconfigure(square_id, outline='black')
            self.starting_point_id = square_id

    def set_to_target(self):
        try:
            square_id = self.selected[0]
            if self.target_point_id is not None:
                if self.matrix[self.square_id_to_pos[self.target_point_id- self.prev][0]][self.square_id_to_pos[self.target_point_id- self.prev][1]].type == 3:
                    self.matrix[self.square_id_to_pos[self.target_point_id- self.prev][0]][self.square_id_to_pos[self.target_point_id- self.prev][1]].set_normal()
            self.matrix[self.square_id_to_pos[square_id- self.prev][0]][self.square_id_to_pos[square_id- self.prev][1]].set_target()
            self.itemconfigure(square_id, outline='black')
            self.target_point_id = square_id
        except:
            square_id = self.selected[0]
            if self.target_point_id is not None:
                if self.matrix[self.square_id_to_pos[self.target_point_id - self.prev][0]][
                    self.square_id_to_pos[self.target_point_id - self.prev][1]].type == 3:
                    self.matrix[self.square_id_to_pos[self.target_point_id - self.prev][0]][
                        self.square_id_to_pos[self.target_point_id - self.prev][1]].set_normal()
            self.matrix[self.square_id_to_pos[square_id - self.prev][0]][
                self.square_id_to_pos[square_id - self.prev][1]].set_target()
            self.itemconfigure(square_id, outline='black')
            self.target_point_id = square_id

    def resize_selection_square(self, event):
        square = self.find_closest(event.x, event.y, halo = 0)[0]
        self.itemconfigure(square, outline = 'red')
        if (self.prev_selected != square) and (self.prev_selected != self.first):

            self.itemconfigure(self.prev_selected, outline = 'black')
        self.prev_selected = square

    def start_to_drag(self, event):
        self.drag_end = (0, 0)

        self.first = self.find_closest(event.x, event.y, halo = 0)[0]
        self.itemconfigure(self.first, outline='red')

        #self.selection_rectangle_id = self.create_rectangle(event.x, event.y, event.x, event.y, width = 15, outline = 'blue')
        self.bind('<B3-Motion>', self.resize_selection_square)
        for square_id in self.selected:
            self.itemconfigure(square_id, outline='black')
        self.drag_start = (int(event.x), int(event.y))

    def end_drag(self, event):
        self.selected = self.find_overlapping(self.drag_start[0], self.drag_start[1], event.x, event.y)
        self.drag_end = (event.x, event.y)
        self.unbind('<B3-Motion>')
        self.delete(self.selection_rectangle_id)
        for square_id in self.selected:
            self.itemconfigure(square_id, outline = 'blue')

        if len(self.selected) > 1:
            self.context_menu.entryconfig('Set starting point', state ='disabled')
            self.context_menu.entryconfig('Set target point', state ='disabled')
        else:
            self.context_menu.entryconfig('Set starting point', state='normal')
            self.context_menu.entryconfig('Set target point', state='normal')
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def toggle_editing(self):
        if self.editing is True:
            self.editing = False
            self.unbind('<Button-3>')
            self.unbind('<ButtonRelease-3>')
        else:
            self.editing = True
            self.bind('<Button-3>', self.start_to_drag)
            self.bind('<ButtonRelease-3>', self.end_drag)

    def brush(self, event):
        self.left_click(event)
        square = self.find_closest(event.x, event.y)[0]
        self.selected = (square,)
        self.set_to_obstacle()

    def erase(self, event):
        x0, y0 = event.x - (self.eraser_size - 1) * self.square_size, event.y - (self.eraser_size - 1) * self.square_size
        x1, y1 = event.x + (self.eraser_size - 1) * self.square_size, event.y + (self.eraser_size - 1) * self.square_size
        squares = self.find_overlapping(x0, y0, x1, y1)
        self.selected = squares
        self.set_to_normal()

    def toggle_brush(self):
        if self.brush_is_active is False:
            self.brush_is_active = True
            self.unbind('<Button-1>')
            self.bind('<B1-Motion>', self.brush)
            self.bind('<Button-1>', self.brush)
        else:
            self.brush_is_active = False
            self.unbind('<B1-Motion>')
            self.unbind('<Button-1>')
            self.bind('<Button-1>', self.left_click)

    def toggle_eraser(self):
        if self.eraser_is_active is False:
            self.eraser_is_active = True
            self.bind('<B1-Motion>', self.erase)
            self.bind('<Button-1>', self.erase)
        else:
            self.unbind('<B1-Motion>')
            self.eraser_is_active = False
            self.unbind('<Button-1>')

    def reset(self, types):
        for i in range(0, self.matrix_size):
            for j in range(0, self.matrix_size):
                if self.matrix[i][j].type in types:
                    self.matrix[i][j].set_normal()

class square:
    def __init__(self, canvas, x, y, size):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.id = canvas.create_rectangle(x, y, x + size, y + size, fill = 'white', width = 2 * (size > 10) + 1 * (size <= 10))
        self.type = 0

    def set_path(self):
        self.canvas.itemconfigure(self.id, fill = 'blue')
        self.type = 'path'

    def set_visited(self):
        self.canvas.itemconfigure(self.id, fill = 'red')
        self.type = 'visited'

    def set_queued(self):
        self.canvas.itemconfigure(self.id, fill = 'yellow')
        self.type ='queued'

    def set_evaluating(self):
        self.canvas.itemconfigure(self.id, fill = 'orange')
        self.type = 'evaluating'

    def set_obstacle(self):
        self.canvas.itemconfigure(self.id, fill = 'black')
        self.type = 1

    def set_normal(self):
        self.canvas.itemconfigure(self.id, fill = 'white')
        self.type = 0

    def set_start(self):
        self.canvas.itemconfigure(self.id, fill = 'red')
        self.type = 2

    def set_target(self):
        self.canvas.itemconfigure(self.id, fill='green')
        self.type = 3

