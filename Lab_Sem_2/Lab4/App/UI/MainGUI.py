import tkinter as tk
import tkinter.ttk as ttk

from . import CustomWidgets
from ..Themes import Theme1

def spawn_data_entry(root, fields, operation, table):
    pop_up = CustomWidgets.DataEntryWindow(root, fields, operation, table)


def main():

    # <fereastra principala>
    window = tk.Tk()
    window.resizable(False, False)

    toolstyle = Theme1.theme()

    # <rama pentru butoane>
    # butoanele sunt puse intr-o rama, care este asezata in fereastra principala
    buttons_frame = tk.LabelFrame(window, text='Gestionare date',highlightbackground='black',font =('Rockwell',10))

    add_book_button = ttk.Button(buttons_frame, text="Add book", style = 'alter.TButton', width = 22)
    delete_book_button = ttk.Button(buttons_frame, text="Delete book", style = 'delete.TButton', width = 22)
    update_book_button = ttk.Button(buttons_frame, text="Modify book", style = 'alter.TButton', width = 22)
    view_catalog_button = ttk.Button(buttons_frame, text="Display catalog", style = 'info.TButton', width=22)
    exit_button = ttk.Button(buttons_frame, text="Exit", command = window.destroy, style = 'black.TButton', width=22)

    # adaugam functionalitate butoanelor
    view_catalog_button['command'] = lambda: table.show_catalog()
    add_book_button['command'] = lambda:spawn_data_entry(window, ['title', 'author', 'year published', 'stock', 'price'], 'add', table)
    update_book_button['command'] = lambda:spawn_data_entry(window, ['id','title', 'author', 'year published', 'stock', 'price'], 'update', table)
    delete_book_button['command'] = lambda: spawn_data_entry(window, ['id'], 'delete', table)

    view_catalog_button.pack(padx=2, pady=2)
    add_book_button.pack(padx = 2, pady = 2)
    update_book_button.pack(padx=2, pady=2)
    delete_book_button.pack(padx = 2, pady = 2)
    exit_button.pack(padx = 2, pady = 2)

    # <rama pentru butoane/>

    # <rama pentru tablea de afisare a datelor din fisierul json>

    table_frame = tk.LabelFrame(window, text='Vizualizare date',font =('Rockwell',10))
    table = CustomWidgets.CustomTable(table_frame, columns = ['id', 'title', 'author', 'year_published', 'stock', 'price'], show ='headings',
                                      height=7)

    table.pack(side = 'left')

    # <rama pentru tablea de afisare a datelor din fisierul json/>

    buttons_frame.grid(row=0, column=0, padx = 5, pady = 5)
    table_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
    window.mainloop()
    # <fereastra principala/>

if __name__ == "__main__":
    main()