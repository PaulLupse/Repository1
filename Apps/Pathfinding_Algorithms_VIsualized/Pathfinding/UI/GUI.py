import time
import tkinter as tk
import tkinter.ttk as ttk
import ctypes
import threading as thrd
import tkinter.messagebox as msgbox

from . import CustomWidgets
from ..Algorithms.AStar import Asearch
from ..Algorithms.Lee import lee
import numpy as np
ctypes.windll.shcore.SetProcessDpiAwareness(1)

algo_halt = False
algo_stop = False

def stop_algo(buttons_to_disable, buttons_to_enable):
    global algo_stop
    algo_stop = True
    disable_buttons(buttons_to_disable)
    normalize_buttons(buttons_to_enable)

def resume_algo(buttons_to_disable, buttons_to_enable):
    global algo_halt
    algo_halt = False
    disable_buttons(buttons_to_disable)
    normalize_buttons(buttons_to_enable)

def pause_algo(buttons_to_disable, buttons_to_enable):
    global algo_halt
    algo_halt = True
    disable_buttons(buttons_to_disable)
    normalize_buttons(buttons_to_enable)

def Exit(win):
    win.destroy()
    exit()

def disable_buttons(buttons):
    for button in buttons:
        button['state'] = 'disabled'

def hide_buttons(buttons):
    for button in buttons:
        button['state'] = 'hidden'

def normalize_buttons(buttons):
    for button in buttons:
        button['state'] = 'normal'

def toggle_map_editing(map, buttons):
    if map.editing is True:
        for button in buttons:
            button['state'] = 'disabled'
    else:
        for button in buttons:
            button['state'] = 'normal'
    map.toggle_editing()

def toggle_obstacle_brush(map, buttons):
    if map.brush_is_active is True:
        for button in buttons:
            button['state'] = 'normal'
    else:
        for button in buttons:
            button['state'] = 'disabled'
    map.toggle_brush()

def toggle_eraser(map, buttons):
    if map.eraser_is_active is True:
        for button in buttons:
            button['state'] = 'normal'
    else:
        for button in buttons:
            button['state'] = 'disabled'
    map.toggle_eraser()

def matrix_translate(map):
    l = int(map.matrix_size)
    matrix = np.ndarray((l, l), dtype=np.int64)
    global x_start, y_start, x_target, y_target
    x_start, y_start, x_target, y_target = None, None, None, None
    for i in range(0, l):
        for j in range(0, l):
            if map.matrix[i][j].type == 2:
                x_start, y_start = i, j
                matrix[i][j] = 0
            elif map.matrix[i][j].type == 3:
                x_target, y_target = i, j
                matrix[i][j] = 0
            else: matrix[i][j] = int(map.matrix[i][j].type)

    return matrix, x_start, y_start, x_target, y_target

def generate_map(map, type, size, cell_size):
    if type == 'Grid':
        map.init_square_grid(int(size), int(cell_size))

def start_algo(map, buttons_to_disable, buttons_to_enable, delay, algorithm, *args):
    disable_buttons(buttons_to_disable)
    normalize_buttons(buttons_to_enable)

    matrix, x_start, y_start, x_target, y_target=  matrix_translate(map)
    if x_start == None or x_target == None:
        if x_start == None:
            msgbox.showerror("Grid error", "Select starting point!")
        if x_target == None:
            msgbox.showerror("Grid error", "Select target point!")
        disable_buttons(buttons_to_enable)
        normalize_buttons(buttons_to_disable)
    else:
        if algorithm == 'A*':
            changes_queue, path_queue = Asearch(matrix, x_start + 1, y_start + 1, x_target + 1, y_target + 1, args[0])
        else:
            changes_queue, path_queue = lee(matrix, x_start + 1, y_start + 1, x_target + 1, y_target + 1, args[0])
        thrd.Thread(target = algo_thrd, args = (map, changes_queue, path_queue, buttons_to_disable, buttons_to_enable, delay)).start()

def algo_thrd(Map, changes_queue, path_queue, buttons_to_disable, buttons_to_enable, delay):
    grid = Map.matrix
    global algo_stop, algo_halt
    while changes_queue:
        if algo_stop:
            algo_stop = False
            return
        if not algo_halt:
            change = changes_queue[0]
            if change[0] == 'queued':
                grid[change[1] - 1][change[2] - 1].set_queued()
            elif change[0] == 'evaluating':
                grid[change[1] - 1][change[2] - 1].set_evaluating()
            else:
                grid[change[1] - 1][change[2] - 1].set_visited()
            changes_queue.popleft()
            time.sleep(delay)
        else: time.sleep(0.1)

    while path_queue:
        if not algo_halt:
            change = path_queue[-1]
            grid[change[0] - 1][change[1] - 1].set_path()
            path_queue.pop()
            time.sleep(float(delay))
        else: time.sleep(0.1)

    reset_map(Map, ('visited', 'queued', 'evaluating'), (), ())

    normalize_buttons(buttons_to_disable)
    disable_buttons(buttons_to_enable)

def reset_map(map, square_types, buttons_to_disable, buttons_to_enable):
    thrd.Thread(target = map.reset, args = (square_types,)).start()
    normalize_buttons(buttons_to_enable)
    disable_buttons(buttons_to_disable)

def main():
    win = tk.Tk()
    win.title("Pathfinding Algorithms Visualized")
    win.resizable(False, False)


    map_type_selection_frame = tk.Frame(win)

    map_type_label = tk.Label(map_type_selection_frame, text = 'Choose map type:')
    map_type_label.pack(anchor = 'w')

    map_type_combobox_variable = tk.StringVar(map_type_selection_frame,'Grid')
    map_type_combobox = ttk.Combobox(map_type_selection_frame, textvariable = map_type_combobox_variable, width = 13)
    map_type_combobox['values'] = ('Grid')

    map_type_combobox.pack(anchor = 'w')

    map_type_selection_frame.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = 'w')

    # GENERAL OPTIONS

    maps_options_tab_control = ttk.Notebook(win)
    matrix_options_tab = ttk.Frame(maps_options_tab_control)
    graph_options_tab = ttk.Frame(maps_options_tab_control)
    maps_options_tab_control.add(matrix_options_tab, text = 'Grid Options')
    maps_options_tab_control.add(graph_options_tab, text = 'Labyrinth Options')

    maps_options_tab_control.tab(1, state = 'disabled')

    generation_settings_frame = ttk.LabelFrame(matrix_options_tab, text = 'Map generation')

    grid_size_label = ttk.Label(generation_settings_frame, text = 'Grid size:')
    grid_size_label.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = 'w')

    grid_size_var = tk.StringVar(generation_settings_frame, '10')
    grid_size_entry = ttk.Entry(generation_settings_frame, width = 5, textvariable=grid_size_var)
    grid_size_entry.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = 'w')

    square_size_label = ttk.Label(generation_settings_frame, text='Cell size:')
    square_size_label.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = 'w')

    square_size_var = tk.StringVar(generation_settings_frame, '60')
    square_size_entry = ttk.Entry(generation_settings_frame, width=5, textvariable=square_size_var)
    square_size_entry.grid(row=1, column=1, padx=2, pady=2, sticky = 'w')

    generation_settings_frame.grid(row = 0, column = 0, columnspan = 1, padx = 40, pady = 5)

    # END OPTIONS

    # PARTICULAR OPTIONS

    movement_type_label = tk.Label(matrix_options_tab, text = 'Movement Type:')
    movement_type_label.grid(row = 1, column = 0, columnspan = 1, padx = 2)
    movement_type_radiobuttons_shared_value = tk.StringVar(matrix_options_tab, '1')
    ttk.Radiobutton(matrix_options_tab, text = '4 Directions', variable = movement_type_radiobuttons_shared_value, value = '1').grid(row = 2, column = 0, columnspan = 1, padx = 2)
    ttk.Radiobutton(matrix_options_tab, text = '8 Directions', variable = movement_type_radiobuttons_shared_value, value = '2').grid(row = 3, column = 0, columnspan = 1, padx = 2)

    algo_selection_frame = tk.Frame(matrix_options_tab)
    algo_selection_label = tk.Label(algo_selection_frame, text='Algorithm:')
    algo_selection_label.pack()
    algo_selection_combobox = CustomWidgets.ImprovedComboBox(algo_selection_frame, values=('A*', 'Lee'), width=12,
                                                             pack=True)
    algo_selection_frame.grid(row = 4, column = 0, padx = 10, pady = 5)

    delay_entry_frame = tk.Frame(matrix_options_tab)
    delay_entry_label = tk.Label(delay_entry_frame, text = "Delay (in seconds):")
    delay_entry_var = tk.StringVar(matrix_options_tab, '0.1')
    delay_entry = ttk.Entry(delay_entry_frame, textvariable=delay_entry_var, width = 15)

    delay_entry_label.pack()
    delay_entry.pack()
    delay_entry_frame.grid(row = 5, column = 0, padx = 10, pady = 5)

    maps_options_tab_control.grid(row = 2, column = 0, padx = 10, pady = 5)

    # END OPTIONS

    # MAP

    map_frame = tk.Frame(win)
    map = CustomWidgets.Map(map_frame, 900, 900, 'matrix', row = 0, column = 0, columnspan = 300)

    map_frame.grid(row = 0, column = 2, rowspan = 50, columnspan = 1)

    brush_button = ttk.Button(map_frame, text = "TOGGLE OBSTACLE BRUSH")
    eraser_button = ttk.Button(map_frame, text="TOGGLE OBSTACLE ERASER")

    brush_button['command'] = lambda : toggle_obstacle_brush(map, (eraser_button,))
    eraser_button['command'] = lambda : toggle_eraser(map, (brush_button,))

    brush_button.grid(row = 1, column = 1, sticky = 'w')
    eraser_button.grid(row=1, column=2, sticky='w')

    edit_button = ttk.Button(map_frame, text = "TOGGLE EDITING")
    edit_button['command'] = lambda : toggle_map_editing(map, (brush_button, eraser_button))

    edit_button.grid(row = 1, column = 0, sticky = 'w')

    map.init_square_grid(10, 60)
    #CustomWidgets.square(map, 2, 2, 20)

    # END MAP

    # BUTTONS

    button_frame = tk.Frame(win)
    button_frame.grid(row=3, column=0)

    generate_button = ttk.Button(button_frame, text='GENERATE MAP', width=22)
    generate_button.pack()

    start_algo_button = ttk.Button(button_frame, text = "START ALGORITHM", width = 22)
    start_algo_button.pack()

    reset_map_button = ttk.Button(button_frame, text = "RESET MAP", width = 22)
    reset_map_button.pack()

    algo_halt_button = ttk.Button(button_frame, text = "PAUSE", width = 22)
    algo_halt_button.pack()

    algo_resume_button = ttk.Button(button_frame, text="RESUME", width=22)
    algo_resume_button.pack()

    algo_stop_button = ttk.Button(button_frame, text="STOP", width=22)
    algo_stop_button.pack()

    disable_buttons((algo_stop_button, algo_resume_button, algo_halt_button))

    exit_button = ttk.Button(button_frame, text='EXIT', width=22)

    generate_button['command'] = lambda: generate_map(map, map_type_combobox.get(), grid_size_entry.get(), square_size_entry.get())
    start_algo_button['command'] = lambda : start_algo(map, (brush_button, eraser_button, edit_button, generate_button, start_algo_button, reset_map_button),
                                                       (algo_halt_button, algo_resume_button, algo_stop_button), float(delay_entry_var.get()), algo_selection_combobox.get(), int(movement_type_radiobuttons_shared_value.get()))

    reset_map_button['command'] = lambda : reset_map(map, ('visited', 'evaluating', 'queued', 'path'), (reset_map_button,), (start_algo_button,))

    exit_button['command'] = lambda arg=win: Exit(arg)
    algo_stop_button['command'] = lambda : stop_algo((algo_stop_button, algo_resume_button, algo_halt_button),
                                                     (brush_button, eraser_button, edit_button, generate_button, reset_map_button))

    algo_halt_button['command'] = lambda : pause_algo((algo_halt_button,), (algo_resume_button,))
    algo_resume_button['command'] = lambda : resume_algo((algo_resume_button,), (algo_halt_button,))

    exit_button.pack()

    # END BUTTONS

    win.mainloop()

main()