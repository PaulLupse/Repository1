# ADFGVX Cipher

import numpy as np
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
import math
from functools import cmp_to_key

# \/ \/ \/ FrontEnd \/ \/ \/

win = tk.Tk()
win.title("ADFGVX Cipher")
win.geometry("950x300")
win.resizable(False, False)

EncodeKey = StringVar(win, "")

KeyFrame = ttk.Frame(win, height = 2, width = 20)
KeyEntryLabel = ttk.Label(KeyFrame, text = "Enter Key:")
KeyEntry = ttk.Entry(KeyFrame, width = 19, font = "Courier", justify = "center", textvariable = EncodeKey)

KeyMatFrame = ttk.Frame(win, height = 2, width = 20)
KeyMatEntryLabel = ttk.Label(KeyMatFrame, text = "Enter character matrix:")
KeyMatEntry = tk.Text(KeyMatFrame, width = 6, font = ("Courier", 15), height = 6, relief = "solid")

MsgAFrame = ttk.Frame(win, height = 2, width = 20)
MsgAEntryLabel = ttk.Label(MsgAFrame, text = "Enter Message to encode/decode:")
MsgAEntry = tk.Text(MsgAFrame, width = 25, height = 11, font = ("Courier", 12), relief = "solid")

MsgBFrame = ttk.Frame(win, height = 2, width = 20)
MsgBOutLabel = ttk.Label(MsgBFrame, text = "Encoded/Decoded Message:")
MsgBOut = tk.Text(MsgBFrame, width = 25, height = 11, font = ("Courier", 12), relief = "solid", wrap = "word")
MsgBOut.config(state = "disabled")

# /\ /\ /\ FrontEnd /\ /\ /\

class LetCode(object):
    def __init__(self, let1, let2):
        self.let1 = let1
        self.let2 = let2

EncodeKey.set(value = "PRIVACY")
KeyMatEntry.insert(END, "NA1C3H8TB2OME5WRPD4F6G7I9J0KLQSUVXYZ")

c = ('A', 'D', 'F', 'G', 'V', 'X',)

def compare(col1, col2):
    ord1 = ord(col1[-1]); ord2 = ord(col2[-1])
    if ord1 < ord2:
        return -1
    elif ord1 == ord2:
        return 0
    else: return 1

def Encode():
    LettersCode = [LetCode('0', '0') for _ in range(0, 205)]

    KeyMatString =  KeyMatEntry.get(1.0, END)
    MsgToEncode =   MsgAEntry.get(1.0, END)

    EarlyEncodedMsg = ""
    MsgToEncode = MsgToEncode.replace(" ", "")

    k = 0
    for i in range(0, 6):
        for j in range(0, 6):
            LettersCode[ord(KeyMatString[k])] = LetCode(c[i], c[j])
            k += 1

    for letter in MsgToEncode[:-1:]:
        l1 = LettersCode[ord(letter)].let1
        l2 = LettersCode[ord(letter)].let2
        EarlyEncodedMsg += l1 + l2

    EncodedMat = []
    lkey = len(EncodeKey.get()); lmsg = len(EarlyEncodedMsg)
    MaxColLength = math.ceil(lmsg / lkey)
    for j in range(0, lkey):
        column = ''
        for i in range(0, MaxColLength):
            index = i*lkey + j
            if index < lmsg:
                column += EarlyEncodedMsg[index]
        column += EncodeKey.get()[j]
        EncodedMat.append(column)

    EncodedMat.sort(key = cmp_to_key(compare))

    for i in range(lkey):
        EncodedMat[i] = EncodedMat[i][0:-1]

    EncodedMsg = " ".join(EncodedMat)

    MsgBOut.config(state="normal")
    MsgBOut.delete('1.0', END)
    MsgBOut.insert(tk.END, EncodedMsg)
    MsgBOut.config(state="disabled")

    print(EarlyEncodedMsg)
    print(EncodedMat)
    print(EncodedMsg)

def Decode():


# \/ \/ \/ FrontEnd \/ \/ \/

ButtonFrame = ttk.Frame(win, width = 10, height = 3)
EncodeButton = ttk.Button(ButtonFrame, text = "ENCODE", command = Encode)
DecodeButton = ttk.Button(ButtonFrame, text = "DECODE")
ExitButton = ttk.Button(ButtonFrame, text = "EXIT", command = win.destroy, width = 11)

MsgAEntryLabel.pack()
MsgAEntry.pack()
MsgAFrame.grid(row = 0, column = 0, padx = 20, pady = 10, rowspan = 2)

KeyEntryLabel.pack()
KeyEntry.pack()
KeyFrame.grid(row = 0, column = 1, columnspan = 2, sticky = N, padx = 20, pady = 10)

KeyMatEntryLabel.pack()
KeyMatEntry.pack()
KeyMatFrame.grid(row = 1, column = 1,  sticky = N, padx = 0, pady = 10, rowspan = 3)

ButtonFrame.grid(row = 1, column = 2, rowspan = 1, padx = 10)
EncodeButton.pack()
DecodeButton.pack()
ExitButton.pack()

MsgBOutLabel.pack()
MsgBOut.pack()
MsgBFrame.grid(row = 0, column = 3, padx = 20, pady = 10, rowspan = 2)

win.mainloop()

# /\ /\ /\ FrontEnd /\ /\ /\

#ATTACKAT1200AM