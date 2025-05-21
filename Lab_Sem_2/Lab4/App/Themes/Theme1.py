import tkinter.ttk as ttk

def _buttons_style(style):
    style.configure("TButton", font=("Rockwell", 10))

    style.configure("delete.TButton", background="#f77979")
    style.map('delete.TButton', background=[('active', "#d66969")])

    style.configure("info.TButton", background="#79b8f7")
    style.map('info.TButton', background=[('active', "#6297cc")])

    style.configure("green.TButton", background="#7afa9c")
    style.map('green.TButton', background=[('active', "#64cc80")])

    style.configure("alter.TButton", background="#f79f79")
    style.map('alter.TButton', background=[('active', "#c27d5f")])

    style.configure("black.TButton", background="black", foreground="white")
    style.map('black.TButton', background=[('active', "#292523")])

def theme():

    style = ttk.Style()

    style.theme_use('clam')

    _buttons_style(style)

    style.configure('TLabel', font=("Rockwell", 10))

    return style