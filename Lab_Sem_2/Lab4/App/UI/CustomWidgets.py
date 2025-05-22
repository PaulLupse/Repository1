import tkinter as tk
import tkinter.ttk as ttk
from ..Themes import Theme1
from ..Routes import Books
import tkinter.messagebox as msgbox

# clasa pentru widget entry cu o eticheta

class LabeledEntry(ttk.Entry):
    def __init__(self, master, label_text, label_position, entry_width, frame_row, frame_column, padx, pady):

        style = Theme1.theme()

        self.frame = tk.Frame(master)
        self.label = ttk.Label(self.frame, text = label_text)
        self.label_text = label_text
        self.frame.grid(row = frame_row, column = frame_column, padx = padx, pady = pady, sticky = 'w')
        super().__init__(self.frame, width = entry_width, justify = "center")

        if label_position == 'n':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 1, column = 0)
        if label_position == 's':
            self.label.grid(row = 1, column = 0)
            self.grid(row = 0, column = 0)
        if label_position == 'w':
            self.label.grid(row = 0, column = 0)
            self.grid(row = 0, column = 1)
        if label_position == 'e':
            self.label.grid(row = 0, column = 1)
            self.grid(row = 0, column = 0)

# clasa pentru tabela cu functionalitati custom
class CustomTable(ttk.Treeview):

    def __init__(self, master, **options):
        super().__init__(master, **options)

        self.fields = options['columns']

        self.tag_configure('even_row', background='#dedcfc')
        self.tag_configure('odd_row', background='#ffffff')

        # folosim tema clam
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Rockwell", 10)) # seteaza fontul heading-urilor

        # bara de derulare verticala
        vertical_scrollbar = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        vertical_scrollbar.pack(side = 'right', fill='y')
        self.configure(yscrollcommand=vertical_scrollbar.set)

        # bara de derulare orizontala
        horizontal_scrollbar = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        horizontal_scrollbar.pack(side='bottom', fill='x')
        self.configure(xscrollcommand=horizontal_scrollbar.set)

        # seteaza heading-urile si coloanele
        for field in options['columns']:
            self.heading(field, text=field, command = lambda f=field:self._treeview_sort_column(f))
            self.column(field, anchor='center', stretch=False, width = 100)


    # afiseaza pe tabela toate datele din catalog
    def show_catalog(self):

        self._clear()
        catalog_data = Books.get_all_books()[0]
        for index, book in enumerate(catalog_data):
            self._insert_row(book, self._get_tag(index))

    # afiseaza un rand in tabela, dupa ultimul rand adaugat
    def _insert_row(self, data, tag):

        if not type(data) == dict:
            raise TypeError('data must be a dictionary')

        self.insert('', 'end', values=[value for value in data.values()], tags = (tag,))

    # sterge datele din tabela
    def _clear(self):

        for children in self.get_children():
            self.delete(children)

    @staticmethod
    def _get_tag(index):

        if index % 2 == 0:
            tag = 'even_row'
        else:
            tag = 'odd_row'

        return tag

    def _treeview_sort_column(self, column):

        print(column)

        # lista care memoreaza o pereche de date: valoarea coloanei cartii si cartea respectiva
        # self.set returneaza valoarea campului column a cartii book
        l = [(self.set(book, column), self.set(book)) for book in self.get_children()]

        # sorteaza dupa valoarea coloanei
        l = sorted(l, key = lambda x:x[0])

        self._clear()
        # rearanjeaza cartile in pozitia sortata
        for index, (order, book) in enumerate(l):
            self._insert_row(book, self._get_tag(index))

class EntryWindow(tk.Toplevel):

    def __init__(self, master, fields, table):
        super().__init__(master)

        style = Theme1.theme()

        self.table = table
        self.field_entries = []
        self.fields_number = self._init_fields(fields)

    # blockeaza interactiunea cu fereastra principala,
    # pana ce fereastra pop-up este activa
    def _disable_root(self):

        master = self.master
        self.transient(master)
        self.grab_set()
        master.wait_window(self)

    # initializeaza campurile de intrare a datelor
    # si returneaza numarul de campuri initializate
    def _init_fields(self, fields):
        index = 0
        fields_frame = tk.Frame(self)
        for index, field in enumerate(fields):
            field_entry = LabeledEntry(fields_frame, field + ':', 'w', 20, index, 0, 5, 1)
            self.field_entries.append(field_entry)
        fields_frame.grid(row = 0, column = 0, padx=1, pady=1, columnspan = 100)
        return index

    # returneaza datele introduse in campurile de intrare
    def _get_data(self):

        data = {}
        for field in self.field_entries:
            field_value = field.get()
            data[field.label_text.replace(' ', '_')[:-1:]] = field_value
        return data

# subclasa a EntryWindow, ajustata pentru introducerea datelor
# necesare gestionarii bazei de date, prin API (Rute)
class DataEntryWindow(EntryWindow):

    def __init__(self, master, fields, operation, table):
        super().__init__(master, fields, table)

        self.operation = operation

        add_button = ttk.Button(self, text='Confirm', style = 'green.TButton')
        add_button['command'] = lambda:self._send_data()
        add_button.grid(row = self.fields_number + 1, column = 0, padx=5, pady=5)

        exit_button = ttk.Button(self, text="Return", command=self.destroy, style = 'black.TButton')
        exit_button.grid(row = self.fields_number + 1, column = 1, padx=5, pady=5)

        self._disable_root()
        self.mainloop()

    # trimite cereri la API si returneaza raspunsurile
    def _send_data(self):

        data = self._get_data()
        response = None
        if self.operation == 'add': # trimite cerere de adaugare a unei carti
            response = Books.add_book(data)
        elif self.operation == 'update': # trimite cerere de modificare a unei carti existente
            response = Books.update_book(data)
        elif self.operation == 'delete': # trimite cerere de stergere a unei carti existente
            response = Books.delete_book(data['id'])
        if response[1] > 299: # daca este returnata o eroare
            msgbox.showerror("Eroare", response[0]) # este afisata eroarea
        else: # altfel
            msgbox.showinfo("Informatie", response[0]) # este afisat raspunsul de confirmare
            self.table.show_catalog()


if __name__ == '__main__':

    root = tk.Tk()
    ct = CustomTable(root,  columns = ['id', 'title', 'author', 'year published', 'stock', 'price'], show ='headings',
                                      height=7)

