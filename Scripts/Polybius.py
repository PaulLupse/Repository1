# Polybius Cipher

from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Polybius Cipher")
win.geometry("320x460")
win.resizable(False,False)

KeyEntryLabel = ttk.Label(text = "ENTER KEY:")
KeyEntry = tk.Text(       win, font = "Courier", width = 5, height = 5)
MsgEntryLabel = ttk.Label(text = "ENTER MESSAGE:")
MsgEntry = st.ScrolledText(       win, font = "Courier", width = 21, height = 10)
CodedMsgOutput = st.ScrolledText( win, font = "Courier", width = 28, height = 10)

KeyEntryLabel.grid( row = 0, column = 0, sticky = N,  padx = 4,  pady = 0)
KeyEntry.grid(      row = 1, column = 0, sticky = N,  padx = 4,  pady = 0, rowspan = 1)
MsgEntryLabel.grid( row = 0, column = 1, sticky = NW, padx = 0,  pady = 0)
MsgEntry.grid(      row = 1, column = 1, sticky = NW, padx = 0,  pady = 0, rowspan = 2)
CodedMsgOutput.grid(row = 3, column = 0, sticky = N,  padx = 10, pady = 4, columnspan = 2)

#Pasghetti

CodedMsg =""
LetterCode = {}
LetterDecode = [["0"] * 6 for _ in range(6)]

# ABCDEFGHIJKLMNOPRSTUVWXYZ

KeyEntry.insert(tk.END, "ABCDEFGHIJKLMNOPRSTUVWXYZ")
CodedMsgOutput.config(state = "disabled")
def encodemsg():
    k = 0
    key = (KeyEntry.get("1.0", END)).upper()
    msg = (MsgEntry.get("1.0", END)).upper()
    global CodedMsg
    for letter in key[:len(key):]:
        LetterCode[ord(letter)] = [str(k // 5), str(k % 5)]
        k += 1
    CodedMsg = ""
    for letter in msg[:len(msg)-1:]:
        CodedMsg = CodedMsg + LetterCode[ord(letter)][0] + LetterCode[ord(letter)][1]
    CodedMsgOutput.config(state = "normal")
    CodedMsgOutput.delete('1.0', END)
    CodedMsgOutput.insert(tk.END, CodedMsg)
    CodedMsgOutput.config(state = "disabled")

def decodemsg():
    key = KeyEntry.get("1.0", END).upper()
    msg = MsgEntry.get("1.0", END).upper()
    k = 0
    EncodedMsg = ''
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            LetterDecode[i][j] = key[k]
            k += 1
            j += 1
        i += 1
    LetterDecode[5][5] = ' '
    for i in range(0, len(msg)-1, 2):
        EncodedMsg = EncodedMsg + LetterDecode[int(msg[i])][int(msg[i+1])]
    CodedMsgOutput.config(state = "normal")
    CodedMsgOutput.delete('1.0', END)
    CodedMsgOutput.insert(tk.END, EncodedMsg)
    CodedMsgOutput.config(state = "disabled")

ButtonFrame = ttk.Frame(win, height = 3, width = 10)

buton0 = ttk.Button(ButtonFrame, command = encodemsg,   text = "ENCODE", width = 8, cursor = 'hand2')
buton1 = ttk.Button(ButtonFrame, command = decodemsg,   text = "DECODE", width = 8, cursor = 'hand2')
buton2 = ttk.Button(ButtonFrame, command = win.destroy, text = "EXIT",   width = 8, cursor = 'hand2')

buton0.pack()
buton1.pack()
buton2.pack()

def disableButtons():
    buton0["state"] = "disabled"
    buton1["state"] = "disabled"
def enableButtons():
    buton0["state"] = "normal"
    buton1["state"] = "normal"

ButtonFrame.grid(row = 2, column = 0, sticky = N)

keyWarningIsActive = 0
keyWarningText = tk.StringVar()
keyWarningText.set("")
keyWarningLabel = tk.Label(textvariable = keyWarningText, font = ("Courier", 8, "bold"), fg = "red", justify=tk.LEFT)
keyWarningLabel.grid(row = 8, column = 0, columnspan = 4, padx = 15)

msgWarningIsActive = 0
msgWarning = tk.StringVar()
msgWarning.set("")
msgWarningLabel = tk.Label(textvariable = msgWarning, font = ("Courier", 8, "bold"), fg = "red", justify=tk.LEFT)
msgWarningLabel.grid(row = 10, column = 0, columnspan = 4, padx = 15)

def Warnings():
    global keyWarningIsActive; global msgWarningIsActive

    if not(KeyEntry.get(1.0, "end-1c").isalpha() or KeyEntry.get(1.0) == '\n'):
        keyWarningText.set("""ENCRYPTION KEY MUST ONLY CONTAIN LETTERS!""")
        keyWarningIsActive = 1
        disableButtons()
    elif len(KeyEntry.get(1.0, "end-1c")) < 25:
        keyWarningText.set("""ENCRYPTION KEY MUST BE AT LEAST
        25 CHARACTERS!""")
        keyWarningIsActive = 1
        disableButtons()
    elif len(set(KeyEntry.get(1.0, "end-1c").upper())) != len(KeyEntry.get(1.0, "end-1c").upper()):
        keyWarningText.set("""ENCRYPTION KEY MUST NOT HAVE 
    DUPLICATE CHARACTERS!""")
        keyWarningIsActive = 1
        disableButtons()
    else:
        keyWarningText.set("")
        keyWarningIsActive = 0

    if not ((MsgEntry.get(1.0, "end-1c").isalpha()
            or MsgEntry.get(1.0, "end-1c").isdigit())
            or MsgEntry.get(1.0) == '\n'):
        msgWarning.set("""MESSAGE MUST ONLY CONTAIN LETTERS 
          OR DIGITS!""")
        msgWarningIsActive = 1
        disableButtons()
    else:
        msgWarning.set("")
        msgWarningIsActive = 0

    if not keyWarningIsActive or not msgWarningIsActive:
        enableButtons()

    if MsgEntry.get(1.0, "end-1c").isalpha():
        buton0["state"] = "normal"
        buton1["state"] = "disabled"
    elif MsgEntry.get(1.0, "end-1c").isdigit():
        buton0["state"] = "disabled"
        buton1["state"] = "normal"

    win.after(200, Warnings)

Warnings()
win.mainloop()