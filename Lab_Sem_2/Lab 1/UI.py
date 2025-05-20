import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
import threading as thrd
import ctypes
import main

import tkinter.messagebox as msgbox

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def validare_int(intigar):
    try:
        int(intigar)
        return 1
    except:
        return 0

cnpuri = []
def genereaza_persoane(Var, lista_butoane):
    thrd.Thread(target=genereaza_persoane_thrd, args = (Var, lista_butoane)).start()

def genereaza_persoane_thrd(Var, lista_butoane):
    for buton in lista_butoane:
        buton['state'] = 'disabled'

    Var.set("Se generează persoanele ...")
    global cnpuri
    cnpuri = main.creare_persoane()
    Var.set("Se dispersează cnp-urile ...")
    main.disperseaza()
    Var.set('')

    for buton in lista_butoane:
        buton['state'] = 'normal'

    print(lista_butoane)

def selecteaza(Var, entry, output_scrolled_text, lista_butoane):

    thrd.Thread(target=selecteaza_thrd, args = (Var, entry, output_scrolled_text, lista_butoane,)).start()

def selecteaza_thrd(Var, entry, output_scrolled_text, lista_butoane):
    if not validare_int(entry.get()):
        msgbox.showerror("Valoare numerică incorectă", "Introduceți o valoare validă!")
        return

    Var.set("Se selectează persoanele ...")

    for buton in lista_butoane:
        buton['state'] = 'disabled'

    lista = main.selecteaza_aleator(int(entry.get()))

    Var.set("Se afișează persoanele ...")
    output_scrolled_text.configure(state = 'normal')
    output_scrolled_text.delete('1.0', tk.END)

    i = 1
    for Persoana in lista:
        output_scrolled_text.insert(tk.INSERT, str(f'{i}. {Persoana[0]}, cnp: {Persoana[1]}, pași efectuați: {Persoana[2]}.\n'))
        i += 1

    Var.set('')
    output_scrolled_text.configure(state='disabled')

    for buton in lista_butoane:
        buton['state'] = 'normal'

def cauta_persoana(entry, output_scrolled_text):
    if not validare_int(entry.get()):
        msgbox.showerror("Valoare numerică incorectă", "Introduceți o valoare validă!")
        return

    nume, pasi = main.cauta_persoana(int(entry.get()))

    output_scrolled_text.configure(state='normal')
    output_scrolled_text.delete('1.0', tk.END)

    output_scrolled_text.insert(tk.INSERT, str(f'{nume.strip()}, pași efectuați: {pasi}.'))

    output_scrolled_text.configure(state='disabled')

if __name__ == "__main__":
    win = tk.Tk()
    win.title("Algoritm Hash Table")
    win.resizable(False, False)

    var = tk.StringVar()

    Label_Alege_Tipul_De_Operatie = tk.Label(win, text = 'Alegeti tipul de operatie:')
    Label_Alege_Tipul_De_Operatie.grid(row = 0, column = 0, padx = 10, pady = 5)

    Label_Output = tk.Label(win, text = 'Persoana/persoanele cautate:')
    Label_Output.grid(row = 0, column = 1, padx = 10, pady = 5)

    Output = scrolledtext.ScrolledText(win, wrap = tk.WORD, width = 70, height = 8)
    Output.grid(row = 1, column = 1, padx = 10)
    Output.configure(state='disabled')

    Tab_Control = ttk.Notebook(win)

    Tab_Selectie_Aleatoare = ttk.Frame(Tab_Control)
    Tab_Selectie_Directa = ttk.Frame(Tab_Control)

    Buton_Selectare_Persoane_Aleator = ttk.Button(Tab_Selectie_Aleatoare, text="SELECTEAZĂ PERSOANE", width=22)
    Buton_Cauta_Persoana = ttk.Button(Tab_Selectie_Directa, text="CAUTĂ", width=10)

    lista_butoane = (Buton_Selectare_Persoane_Aleator, Buton_Cauta_Persoana)

    ########## tab-ul pt selectia aleatoare ##############

    Tab_Control.add(Tab_Selectie_Aleatoare, text=' Selecție Aleatoare ')

    Label_Entry_nr_persoane = tk.Label(Tab_Selectie_Aleatoare, text = "Introduceți numărul de\n persoane pentru selecție:")
    Label_Entry_nr_persoane.pack(pady = 2)

    Entry_nr_persoane = ttk.Entry(Tab_Selectie_Aleatoare, width = 10)
    Entry_nr_persoane.pack(pady = 5)


    Buton_Selectare_Persoane_Aleator['command'] = lambda arg0 = var, arg1 = Entry_nr_persoane, arg2 = Output, arg3 = lista_butoane : selecteaza(arg0, arg1, arg2, arg3)
    Buton_Selectare_Persoane_Aleator.pack(pady = 5)


    #######tab-ul pt selectia directa a unui cnp##########


    Tab_Control.add(Tab_Selectie_Directa, text=' Selecție Directă   ')

    Label_Entry_cnp = ttk.Label(Tab_Selectie_Directa, text = "Introduceți cnp-ul:")
    Label_Entry_cnp.pack(pady = 10)

    Entry_Cnp = ttk.Entry(Tab_Selectie_Directa, width = 13)
    Entry_Cnp.pack(pady = 5)

    Buton_Cauta_Persoana.pack(pady = 5)
    Buton_Cauta_Persoana['command'] = lambda arg1 = Entry_Cnp, arg2 = Output : cauta_persoana(arg1, arg2)

    Label_Operatiune_In_Desfasurare = tk.Label(win, textvariable=var)
    Label_Operatiune_In_Desfasurare.grid(row=2, column=0, columnspan=2, pady=10)

    Tab_Control.grid(row = 1, column = 0, padx = 10)

    genereaza_persoane(var, lista_butoane)

    Buton_Exit = ttk.Button(win, text='IEȘIRE', command=win.destroy, width=10)
    Buton_Exit.grid(row=2, column=0, padx=5, pady=5)

    win.mainloop()