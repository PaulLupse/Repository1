# Polybius Cipher

from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk

win = tk.Tk()
win.title("Polybius Cipher")
win.geometry("350x485")

DisplayCodedMsg = ""

KeyEntryLabel = ttk.Label(text = "ENTER KEY:")
KeyEntry = tk.Text(win, font = "Courier", width = 5, height = 5)
MsgEntryLabel = ttk.Label(text = "ENTER MESSAGE:")
MsgEntry = tk.Text(win, font = "Courier", width = 21, height = 10, )
CodedMsgOutput = tk.Text(win, font = "Courier", width = 27, height = 10)

KeyEntryLabel.place(x = 8, y = 0)
KeyEntry.place(x = 12, y = 20)
MsgEntryLabel.place(x = 80, y = 0)
MsgEntry.place(x = 80, y = 20)

CodedMsgOutput.place(x = 10, y = 250)

CodedMsg =""

LetterCode = {}
LetterDecode = [["0", "0", "0", "0", "0", "0"]] * 6
#LetterDecode[5][0] = 'Z'

# ABCDEFGHIJKLMNOPRSTUVWXYZ
#
#DisplayCodedMsg = [letter for letter in msg]

def encodemsg():
    k = 0
    key = KeyEntry.get("1.0", END)
    msg = MsgEntry.get("1.0", END)
    global CodedMsg
    for letter in key[:len(key):]:
        LetterCode[ord(letter)] = [str(k // 5), str(k % 5)]
        k += 1
    for letter in msg[:len(msg)-1:]:
        CodedMsg = CodedMsg + LetterCode[ord(letter)][0] + LetterCode[ord(letter)][1]
        #print(LetterCode[ord(letter)][0], LetterCode[ord(letter)][1], end = ' ')
    CodedMsgOutput.config(state = "normal")
    CodedMsgOutput.delete('1.0', END)
    CodedMsgOutput.insert(tk.END, CodedMsg)
    CodedMsgOutput.config(state = "disabled")

def decodemsg():
    key = KeyEntry.get("1.0", END)
    msg = MsgEntry.get("1.0", END)
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
    #LetterDecode[5][0] = 'Z'
    for i in range(0, len(msg) - 1, 2):
        EncodedMsg = EncodedMsg + LetterDecode[int(msg[i])][int(msg[i+1])]
    CodedMsgOutput.config(state = "normal")
    CodedMsgOutput.delete('1.0', END)
    CodedMsgOutput.insert(tk.END, EncodedMsg)
    CodedMsgOutput.config(state = "disabled")
    print(LetterDecode)
    print(key)

buton = ttk.Button(win, command = encodemsg, text = "ENCODE", width = 8)
buton.place(x = 15, y = 140)
buton1 = ttk.Button(win, command = decodemsg, text = "DECODE", width = 8)
buton1.place(x = 15, y = 165)
buton2 = ttk.Button(win, command = win.destroy, text = "EXIT", width = 8)
buton2.place(x = 15, y = 190)
win.mainloop()