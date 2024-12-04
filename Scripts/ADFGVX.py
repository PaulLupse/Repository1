# ADFGVX Cipher

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import math
from functools import cmp_to_key

import numpy as np

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# \/ \/ \/ FrontEnd \/ \/ \/

win = tk.Tk()
win.title("ADFGVX Cipher")
#win.geometry("765x300")
win.resizable(False, False)

EncodeKey = StringVar(win, "")

KeyFrame = ttk.Frame(win, height = 2, width = 20)
KeyEntryLabel = ttk.Label(KeyFrame, text = "Enter Key:")
KeyEntry = ttk.Entry(KeyFrame, width = 19, font = "Courier", justify = "center", textvariable = EncodeKey)

KeyMatFrame = ttk.Frame(win, height = 2, width = 20)
KeyMatEntryLabel = ttk.Label(KeyMatFrame, text = "Enter character\n matrix:", justify = 'center')
KeyMatEntry = tk.Text(KeyMatFrame, width = 6, font = ("Courier", 12), height = 6, relief = "solid")

MsgAFrame = ttk.Frame(win, height = 2, width = 20)
MsgAEntryLabel = ttk.Label(MsgAFrame, text = "Enter Message to encode/decode:")
MsgAEntry = tk.Text(MsgAFrame, width = 25, height = 11, font = ("Courier", 12), relief = "solid", wrap = "word")

MsgBFrame = ttk.Frame(win, height = 2, width = 20)
MsgBOutLabel = ttk.Label(MsgBFrame, text = "Encoded/Decoded Message:")
MsgBOut = tk.Text(MsgBFrame, width = 25, height = 11, font = ("Courier", 12), relief = "solid", wrap = "word")
MsgBOut.config(state = "disabled")

TemporaryWarningMessage = StringVar()
TemporaryWarningLabel = Label(fg = "red", textvariable= TemporaryWarningMessage)

WarningMessage = StringVar()
WarningMessageLabel = Label(fg = "red", textvariable= WarningMessage)

# /\ /\ /\ FrontEnd /\ /\ /\

class LetCode(object):
    let = []
    def __init__(self, let1, let2):
        self.let1 = let1
        self.let2 = let2

EncodeKey.set(value = "ACHTUNG")
KeyMatEntry.insert(END, "NA1C3H8TB2OME5WRPD4F6G7I9J0KLQSUVXYZ")

c = ('A', 'D', 'F', 'G', 'V', 'X',)

def compare(col1, col2):
    ord1 = ord(col1[-1]); ord2 = ord(col2[-1])
    if ord1 < ord2:
        return -1
    elif ord1 == ord2:
        return 0
    else: return 1

def compare1(indLetter1, indLetter2):
    if indLetter1[0] < indLetter2[0]:
        return -1
    elif indLetter1[0] == indLetter2[0]:
        return 0
    else: return 1

def compare2(col1, col2):
    ind1 = 0
    ind2 = 0
    while col1[ind1].isalpha():
        ind1 += 1
    while col2[ind2].isalpha():
        ind2+= 1
    ord1 = int(col1[ind1::]); ord2 = int(col2[ind2::])
    if ord1 < ord2:
        return -1
    elif ord1 == ord2:
        return 0
    else: return 1

counter = 0
userInputWarning = False
showingWarning = False
def showWarning():
    global counter
    global showingWarning
    showingWarning = True

    if counter > 0:
        win.after(1000, showWarning)
        counter -= 1
    else:
        TemporaryWarningMessage.set("")
        showingWarning = False

def Encode():
    global userInputWarning

    LettersCode = [LetCode('0', '0') for _ in range(0, 205)]

    KeyMatString =  KeyMatEntry.get(1.0, END).upper()
    MsgToEncode =   MsgAEntry.get(1.0, END).upper()

    EarlyEncodedMsg = ""
    MsgToEncode = MsgToEncode.replace(" ", "")
    MsgToEncode = MsgToEncode.replace("\n", "")

    if len(MsgToEncode) >= len(EncodeKey.get())//2:
        k = 0
        for i in range(0, 6):
            for j in range(0, 6):
                LettersCode[ord(KeyMatString[k])] = LetCode(c[i], c[j])
                k += 1

        for letter in MsgToEncode:
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
        #EncodedMsg.strip(" ")

        MsgBOut.config(state="normal")
        MsgBOut.delete('1.0', END)
        MsgBOut.insert(tk.END, EncodedMsg)
        MsgBOut.config(state="disabled")
    else:
        userInputWarning = True
        showWarning()
        TemporaryWarningMessage.set(
            "LENGTH OF MESSAGE TO ENCODE MUST BE AT LEAST HALF THE LENGTH OF THE ENCRYPTION KEY!")

def Decode():
    global userInputWarning

    KeyMat = KeyMatEntry.get(1.0, END).upper()
    MsgToDecode = MsgAEntry.get(1.0, END).upper()

    MsgToDecode = MsgToDecode.replace("\n", "")
    MsgToDecode = MsgToDecode.strip(" ")

    EncodedMat = [coloana for coloana in MsgToDecode.split(" ")]

    if len(EncodedMat) == len(EncodeKey.get()):
        indKey = []
        for i in range (0, len(EncodeKey.get())):
            indKey.append((EncodeKey.get()[i], i))

        indKey.sort(key = cmp_to_key(compare1))

        for i in range(0, len(EncodedMat)):
            EncodedMat[i] += str(indKey[i][1])

        EncodedMat.sort(key = cmp_to_key(compare2))

        for i in range(0, len(EncodedMat)):
            ind = 0
            while EncodedMat[i][ind].isalpha():
                ind+=1

            EncodedMat[i] = EncodedMat[i][0:ind]

        EarlyDecodedMsg = ""

        MaxColLength = max([len(column) for column in EncodedMat])
        for i in range(0, MaxColLength):
            for j in range(0, len(EncodeKey.get())):
                if i < len(EncodedMat[j]):
                    EarlyDecodedMsg += EncodedMat[j][i]

        KeyMat = KeyMat[0:-1:]

        LetterCodeMat = np.array([letter for letter in KeyMat])
        LetterCodeMat = LetterCodeMat.reshape(6, 6)

        DecodedMsg = ""

        for i in range(0, len(EarlyDecodedMsg), 2):
            DecodedMsg += LetterCodeMat[c.index(EarlyDecodedMsg[i])][c.index(EarlyDecodedMsg[i+1])]

        MsgBOut.config(state="normal")
        MsgBOut.delete('1.0', END)
        MsgBOut.insert(tk.END, DecodedMsg)
        MsgBOut.config(state="disabled")
    else:
        userInputWarning = True
        TemporaryWarningMessage.set(
            "WORD COUNT IN MESSAGE TO DECODE MUST BE EQUAL TO THE LENGTH OF THE ENCRYPTION KEY!")

def ResetKeyMat():
    KeyMatEntry.delete(1.0, END)
    KeyMatEntry.insert(END, "NA1C3H8TB2OME5WRPD4F6G7I9J0KLQSUVXYZ")

# \/ \/ \/ FrontEnd \/ \/ \/

ButtonFrame = ttk.Frame(win, width = 10, height = 3)
EncodeButton = ttk.Button(ButtonFrame, text = "ENCODE", command = Encode, width = 15, cursor = "hand2")
DecodeButton = ttk.Button(ButtonFrame, text = "DECODE", command = Decode, width = 15, cursor = "hand2")
ResetKeyMatButton = ttk.Button(ButtonFrame, text = "RESET MATRIX", command = ResetKeyMat, width = 15, cursor = "hand2")
ExitButton = ttk.Button(ButtonFrame,   text = "EXIT", command = win.destroy, width = 15, cursor = "hand2")

MsgAEntryLabel.pack()
MsgAEntry.pack()

KeyEntryLabel.pack()
KeyEntry.pack()

KeyMatEntryLabel.pack()
KeyMatEntry.pack()

EncodeButton.pack(pady = 2)
DecodeButton.pack(pady = 2)
ResetKeyMatButton.pack(pady = 2)
ExitButton.pack(pady = 2)

MsgBOutLabel.pack()
MsgBOut.pack()



MsgAFrame.grid(   row = 0, column = 0, rowspan = 2,    padx = 15, pady = 10, sticky = N)
KeyFrame.grid(    row = 0, column = 1, columnspan = 2, padx = 0, pady = 10, sticky = N)
KeyMatFrame.grid( row = 1, column = 1,                 padx = 0,  pady = 0,  sticky = N)
ButtonFrame.grid( row = 1, column = 2,                 padx = 0, pady = 0,  sticky = W)
MsgBFrame.grid(   row = 0, column = 3, rowspan = 2,    padx = 15, pady = 10, sticky = N)
TemporaryWarningLabel.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 2, sticky = N)
WarningMessageLabel.grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 2, sticky = N)

# /\ /\ /\ FrontEnd /\ /\ /\

def disableButtons():
    EncodeButton["state"] = "disabled"
    DecodeButton["state"] = "disabled"
def enableButtons():
    EncodeButton["state"] = "normal"
    DecodeButton["state"] = "normal"

encodeOK = True
keyWarning = False
def RestrictionsAndWarnings():
    global counter
    global userInputWarning
    global encodeOK

    msg = MsgAEntry.get(1.0, END).upper()
    msg = msg.replace("\n", "")
    msg = msg.replace(" ", "")
    if not(msg.isalpha()):
        encodeOK = False
    else:
        encodeOK = True
        for letter in msg:
            if letter not in c:
                encodeOK = False

    if userInputWarning is True:
        userInputWarning = False
        counter = 5
        if not showingWarning:
            showWarning()

    win.after(200, RestrictionsAndWarnings)

def ButtonCheck(event):
    print("ACTIVATED")

    if len(KeyMatEntry.get(1.0, 'end-1c')) != 36:
        WarningMessage.set("CHARACTER MATRIX MUST BE EXACTLY 36 CHARACTERS!")
        disableButtons()
    elif len(set(KeyMatEntry.get(1.0, "end-1c").upper())) != len(KeyMatEntry.get(1.0, "end-1c").upper()):
        WarningMessage.set("""CHARACTER MATRIX MUST NOT HAVE DUPLICATE CHARACTERS!""")
        disableButtons()
    elif not(KeyMatEntry.get(1.0, "end-1c").isalnum() or KeyMatEntry.get(1.0) == '\n'):
        WarningMessage.set("""CHARACTER MATRIX MUST ONLY CONTAIN LETTERS AND NUMBERS!""")
        disableButtons()
    else:
        WarningMessage.set("")
        if encodeOK is False:
            DecodeButton["state"] = "disabled"
            EncodeButton["state"] = "normal"
        else:
            enableButtons()

win.bind("<KeyPress>", ButtonCheck)
#win.bind("<KeyRelease>", ButtonCheck)

RestrictionsAndWarnings()
win.mainloop()