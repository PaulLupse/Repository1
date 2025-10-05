import tkinter as tk
import tkinter.ttk as ttk
import ctypes
try:
    import CustomWidgets as cw
except:
    from . import CustomWidgets as cw

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def enter_product_menu(main_window):
    menu = cw.PopupWindow(main_window)
    menu.resizable(False, False)

    # camp pentru introducerea unui nou produs

    product_name_entry_sv = tk.StringVar(menu, 'Schweppes...')
    product_name_entry = cw.LabeledEntry(menu, "Introdu   numele   produsului:", 'n',
                                         gridding_options={'row' : 0, 'column' : 0, 'padx' : 5, 'pady' : 5},
                                         width = 25, textvariable=product_name_entry_sv)

    product_count_entry_sv = tk.StringVar(menu, '1')
    product_count_entry = cw.LabeledEntry(menu, 'Introdu cantitatea (buc):', 'w',
                                          gridding_options={'row' : 1, 'column' : 0, 'padx' : 5, 'pady' : 0},
                                          width = 3, textvariable = product_count_entry_sv)

    button_frame = tk.Frame(menu)

    add_button = ttk.Button(button_frame, text = 'ADAUGĂ')
    add_button.grid(row = 0, column = 0)

    ok_button = ttk.Button(button_frame, text = 'ÎNAPOI', command = menu.destroy_and_release)
    ok_button.grid(row = 0, column = 1)

    button_frame.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)

    menu.mainloop()

def modify_banknote_stock(main_window):
    menu = cw.PopupWindow(main_window)
    menu.resizable(False, False)

    button_frame = tk.Frame(menu)

    add_button = ttk.Button(button_frame, text='ADAUGĂ')
    add_button.grid(row=0, column=0)

    ok_button = ttk.Button(button_frame, text='ÎNAPOI', command=menu.destroy_and_release)
    ok_button.grid(row=0, column=1)

    button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    menu.mainloop()

def modify_product_stock(main_window):
    menu = cw.PopupWindow(main_window)
    menu.resizable(False, False)

    button_frame = tk.Frame(menu)

    add_button = ttk.Button(button_frame, text='ADAUGĂ')
    add_button.grid(row=0, column=0)

    add_button = ttk.Button(button_frame, text='ȘTERGE')
    add_button.grid(row=0, column=1)

    ok_button = ttk.Button(button_frame, text='ÎNAPOI', command=menu.destroy_and_release)
    ok_button.grid(row=0, column=2)

    button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    menu.mainloop()

def main():
    win = tk.Tk()
    win.resizable(False, False)

    # casa de text pt afisarea cosului de cumparaturi
    cart_textbox = cw.LabeledText(win, "Produsele introduse:", "n", {'row' : 0, 'column' : 1, 'padx' : 5, 'pady' : 5}, width = 15, height = 10)

    # casa de text pt afisarea totalului
    total_textbox = cw.LabeledEntry(win, "Total:", 'w', {'row' : 1, 'column' : 1, 'padx' : 5, 'pady' : 5}, width = 5)

    # rama pentru butoane
    button_frame = tk.Frame()
    button_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

    # buton pt modificarea stocului de bancnote
    modify_banknote_stock_button = ttk.Button(button_frame, text = "MODIFICĂ STOCUL\n    DE BANCNOTE", width = 22)
    ttk.Style().configure('modify_banknote_stock_button', )
    modify_banknote_stock_button['command'] = lambda : enter_product_menu(win)
    modify_banknote_stock_button.pack()

    # buton pt introducerea unui nou produs
    product_entry_menu_button = ttk.Button(button_frame, text = 'INTRODU PRODUS', width = 22)
    product_entry_menu_button['command'] = lambda : enter_product_menu(win)
    product_entry_menu_button.pack()

    #buton pentru efectuarea platii
    payment_button = ttk.Button(button_frame, text = "EFECTUEAZA PLATA", width = 22)
    payment_button.pack()

    # buton pt iesirea din program
    exit_button = ttk.Button(button_frame, text = "IEȘIRE", command = win.destroy, width = 22)
    exit_button.pack()

    win.mainloop()

if __name__ == '__main__':
    main()