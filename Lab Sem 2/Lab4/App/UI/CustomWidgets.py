import tkinter as tk
import tkinter.ttk as ttk
from ..Themes import Theme1
from ..Routes import Books
import tkinter.messagebox as msgbox

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

class CustomTable(ttk.Treeview):

    def __init__(self, master, **options):
        super().__init__(master, **options)

        self.fields = options['columns']

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Rockwell", 10))

        for field in options['columns']:
            self.heading(field, text=field)

    def show_catalog(self):

        self._clear()
        catalog_data = Books.get_all_books()[0]
        for book in catalog_data:
            self._insert_row(book)

    # type(data) == dict
    def _insert_row(self, data):

        if not type(data) == dict:
            raise TypeError('data must be a dictionary')
        self.insert('', 'end', values=[value for value in data.values()])

    def _clear(self):

        for children in self.get_children():
            self.delete(children)

class EntryWindow(tk.Toplevel):

    def __init__(self, master, fields, operation):
        super().__init__(master)

        # button_commands key == button name
        # button_commands value == lambda function

        style = Theme1.theme()

        self.field_entries = []
        self.fields_number = self._init_fields(fields)

    def _disable_root(self):

        # blockeaza interactiunea cu fereastra principala,
        # pana ce fereastra pop-up este activa
        master = self.master
        self.transient(master)
        self.grab_set()
        master.wait_window(self)

    def _init_fields(self, fields):
        index = 0
        fields_frame = tk.Frame(self)
        for index, field in enumerate(fields):
            field_entry = LabeledEntry(fields_frame, field + ':', 'w', 20, index, 0, 5, 1)
            self.field_entries.append(field_entry)
        fields_frame.grid(row = 0, column = 0, padx=1, pady=1, columnspan = 100)
        return index

    def _get_data(self):

        data = {}
        for field in self.field_entries:
            field_value = field.get()
            data[field.label_text.replace(' ', '_')[:-1:]] = field_value
        print(data)
        return data

class DataEntryWindow(EntryWindow):

    def __init__(self, master, fields, operation):
        super().__init__(master, fields, operation)

        add_button = ttk.Button(self, text='Confirm', style = 'green.TButton')
        if operation == 'add':
            add_button['command'] = lambda:self._send_data('add')
        else:
            add_button['command'] = lambda:self._send_data('update')
        add_button.grid(row = self.fields_number + 1, column = 0, padx=5, pady=5)

        exit_button = ttk.Button(self, text="Return", command=self.destroy, style = 'black.TButton')
        exit_button.grid(row = self.fields_number + 1, column = 1, padx=5, pady=5)

        self._disable_root()
        self.mainloop()

    def _send_data(self, operation):

        data = self._get_data()
        response = None
        if operation == 'add':
            response = Books.add_book(data)
        else:
            response = Books.update_book(data)

        if response[1] > 299:
            msgbox.showerror("Eroare", response[0])
        else:
            msgbox.showinfo("Informatie", response[0])

