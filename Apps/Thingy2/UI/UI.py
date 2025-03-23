import tkinter as tk
import tkinter.ttk as ttk
import ctypes
import CustomWidgets

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def Exit(win):
    win.destroy()
    exit()

def main():
    win = tk.Tk()
    win.title("A* Algorithm Visualized")
    win.resizable(False, False)





    heuristic_selection_frame = tk.Frame()
    heuristic_selection_label = tk.Label(heuristic_selection_frame, text = "Heuristic calculation type:")

    heuristic_selection_label.pack()

    radiobuttons_shared_value = tk.StringVar(heuristic_selection_frame, '1')
    ttk.Radiobutton(heuristic_selection_frame, text = "Exact", variable = radiobuttons_shared_value, value = '1').pack(anchor = 'w')
    ttk.Radiobutton(heuristic_selection_frame, text = "Approximate", variable = radiobuttons_shared_value, value = '2').pack(anchor = 'w')

    heuristic_selection_frame.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')



    map_type_selection_frame = tk.Frame(win)

    map_type_label = tk.Label(map_type_selection_frame, text = 'Choose map type:')
    map_type_label.pack(anchor = 'w')

    map_type_combobox_variable = tk.StringVar(map_type_selection_frame,'Matrix')
    map_type_combobox = ttk.Combobox(map_type_selection_frame, textvariable = map_type_combobox_variable, width = 13)
    map_type_combobox['values'] = ('Matrix', 'Graph')

    map_type_combobox.pack(anchor = 'w')

    map_type_selection_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'w')



    maps_options_tab_control = ttk.Notebook(win)
    matrix_options_tab = ttk.Frame(maps_options_tab_control)
    graph_options_tab = ttk.Frame(maps_options_tab_control)
    maps_options_tab_control.add(matrix_options_tab, text = 'Matrix Options')
    maps_options_tab_control.add(graph_options_tab, text = 'Graph Options')

    maps_options_tab_control.tab(1, state = 'disabled')


    number_of_cells_label = ttk.Label(matrix_options_tab, text = 'Number Of Cells:')
    number_of_cells_label.grid(row = 0, column = 0, padx = 2, pady = 2)

    number_of_cells_combobox_variable = tk.StringVar(matrix_options_tab, '16')
    number_of_cells_combobox = ttk.Combobox(matrix_options_tab, textvariable = number_of_cells_combobox_variable, width = 4)
    number_of_cells_combobox['values'] = (3, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256)
    number_of_cells_combobox.grid(row = 0, column = 1, padx = 2, pady = 2)



    movement_type_label = tk.Label(matrix_options_tab, text = 'Movement Type:')
    movement_type_label.grid(row = 1, column = 0, columnspan = 2, sticky = 'w', padx = 2)
    movement_type_radiobuttons_shared_value = tk.StringVar(matrix_options_tab, '1')
    ttk.Radiobutton(matrix_options_tab, text = '4 Directions', variable = movement_type_radiobuttons_shared_value, value = '1').grid(row = 2, column = 0, columnspan = 2, sticky = 'w', padx = 2)
    ttk.Radiobutton(matrix_options_tab, text = '8 Directions', variable = movement_type_radiobuttons_shared_value, value = '2').grid(row = 3, column = 0, columnspan = 2, sticky = 'w', padx = 2)


    maps_options_tab_control.grid(row = 2, column = 0, padx = 10, pady = 5)



    exit_button = ttk.Button(text = 'EXIT')
    exit_button['command'] = lambda arg = win : Exit(arg)

    exit_button.grid(row = 3, column = 0, padx = 10, pady = 10)

    map = CustomWidgets.Map(win, 900, 900)
    map.grid(row = 0, column = 1, rowspan = 50)

    win.mainloop()

main()