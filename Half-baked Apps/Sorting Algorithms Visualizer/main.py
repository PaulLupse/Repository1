import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import threading as thrd
import time
import random
import Sorting

import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Application Front End

win = tk.Tk()
win.geometry("700x550")
win.title("Sorting Algorithms Visualised")
win.resizable(False, False)

class Mediator:
    def __init__(self, buttons):
        self.buttons = buttons
    def disable_button(self, button_name):
        self.buttons[button_name]['state'] = 'disabled'
    def enable_button(self, button_name):
        self.buttons[button_name]['state'] = 'normal'

class element:
    def __init__(self, master, x, screenL, elementWidth, border):
        self.master = master
        if border == False:
            self.shape = master.create_rectangle(x + 2, screenL + 2, elementWidth + x + 2, screenL - x - elementWidth + 2 , fill="white", outline='')
        else:
            self.shape = master.create_rectangle(x + 2, screenL + 2, elementWidth + x + 2, screenL - x - elementWidth + 2, fill="white")

class sortingScreen:
    def __init__(self, master, row, column, elementwidth, screenL, ComboBox, ElNumComboBox, DelayEntry, Mediator):
        self.ComboBox = ComboBox
        self.ElNumComboBox = ElNumComboBox
        self.DelayEntry = DelayEntry
        self.screenL = screenL
        self.elementWidth = elementwidth
        self.mediator = Mediator
        self.delay = 0
        self.sorting = False
        self.shuffling = False
        self.colored = [0] * 613
        self.master = master

        self.canvas = tk.Canvas(master, bg = "black", bd = 0, width = screenL, height = screenL)
        self.canvas.grid(row=row, column=column, padx=10, pady=10, rowspan = 20)

        self.element_list = []
        self.init_coords = []

        self.pause_sorting = False
        self.stop_sorting = False

        self.__init_elements()

    def __init_elements(self):
        for i in range(0, self.screenL + 3, self.elementWidth):
            Element = element(self.canvas, i, self.screenL, self.elementWidth, (self.elementWidth > 2))
            self.element_list.append(Element)
            self.init_coords.append(self.canvas.coords(Element.shape))

    def swp(self, el1_index, el2_index):
        el1_coords = self.canvas.coords(self.element_list[el1_index].shape)
        el2_coords = self.canvas.coords(self.element_list[el2_index].shape)

        self.canvas.coords(self.element_list[el1_index].shape, el1_coords[0], el2_coords[1], el1_coords[2], el1_coords[3])
        self.canvas.coords(self.element_list[el2_index].shape, el2_coords[0], el1_coords[1], el2_coords[2], el2_coords[3])

    def overwrite_element(self, el1_index, el2_coords):
        el1_coord = self.canvas.coords(self.element_list[el1_index].shape)
        self.canvas.coords(self.element_list[el1_index].shape, el1_coord[0], el2_coords[1], el1_coord[2], el1_coord[3])

    def shuffle(self):
        Mediator.disable_button('set')
        Mediator.disable_button('worstcase')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')

        self.shuffling = True

        shuffle_indexes = [i for i in range(0, len(self.element_list) - 1)]
        random.shuffle(shuffle_indexes)
        thrd.Thread(target = self.shuffling_thread, args = (shuffle_indexes, )).start()

    def sort(self):
        l = len(self.element_list)
        self.sorting = True

        Mediator.disable_button('set')
        Mediator.disable_button('worstcase')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')
        Mediator.disable_button('resume')

        Mediator.enable_button('pause')
        Mediator.enable_button('stop')

        type = self.ComboBox.comboBox.get()
        indexes = [len(self.element_list) - self.canvas.coords(i.shape)[1]//self.elementWidth for i in self.element_list]
        comparisons = 0
        if type == 'Merge Sort':
            if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
            swap_dq, comparisons = Sorting.Sort_np.MergeSort(indexes, 0, len(indexes))
            thrd.Thread(target=self.merge_sorting_thread, args=(swap_dq,)).start()
        else:
            swap_dq = 0
            match type:
                case 'Stupid Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.StupidSort(indexes)
                case 'Bubble Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.BubbleSort(indexes)
                case 'Selection Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.SelectionSort(indexes)
                case 'Double Selection Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.DoubleSelectionSort(indexes)
                case 'Insertion Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.InsertionSort(indexes)
                case 'Quick Sort':
                    if DelayEntry.get() in 'Def': self.delay = (1/(l*10))
                    swap_dq, comparisons = Sorting.Sort_np.QuickSort(indexes, 0, len(indexes) - 1)
            thrd.Thread(target=self.sorting_thread, args=(swap_dq,)).start()

    def merge_sorting_thread(self, swap_dq):

        while swap_dq:
            if self.stop_sorting is True:
                break
            if self.pause_sorting is False:

                left = swap_dq[0][0]
                right = swap_dq[0][1]
                type = swap_dq[0][3]

                if type in 'set':
                    obj_arr_coords = [self.canvas.coords(self.element_list[k].shape) for k in swap_dq[0][2]]

                    k = 0
                    for i in range(left, right):
                        thrd.Thread(target=self.change_colour_thread, args=(i, 'red', 0.02)).start()
                        self.overwrite_element(i, obj_arr_coords[k])
                        time.sleep(self.delay)
                        k += 1
                else:
                    thrd.Thread(target=self.change_colour_thread, args=(swap_dq[0][0], 'red', 0.01,)).start()
                    thrd.Thread(target=self.change_colour_thread, args=(swap_dq[0][1], 'red', 0.01,)).start()
                    time.sleep(self.delay)
                swap_dq.popleft()

            else: time.sleep(0.05)

        if self.stop_sorting is False:
            thrd.Thread(target=self.final_touch_thread).start()
        else:
            self.stop_sorting = False
            self.pause_sorting = False

    def sorting_thread(self, swap_dq):
        l = len(self.element_list)
        while swap_dq:
            if self.stop_sorting is True:
                break
            if self.pause_sorting is False:
                swap = swap_dq[0]

                thrd.Thread(target = self.change_colour_thread, args = (swap[0], 'red', 0.01,)).start()
                thrd.Thread(target=self.change_colour_thread, args=(swap[1], 'red', 0.01,)).start()

                if swap[2] == 'swap':
                    self.swp(swap[1], swap[0])

                swap_dq.popleft()
                time.sleep(self.delay)

            else: time.sleep(0.005)
        if self.stop_sorting is False:
            thrd.Thread(target=self.final_touch_thread).start()
        else:
            self.stop_sorting = False
            self.pause_sorting = False

    def shuffling_thread(self, indexes):
        l = len(self.element_list)
        for i in range(0, len(self.element_list) - 1):
            self.swp(i, indexes[i])
            time.sleep(1 / l)

        Mediator.enable_button('set')
        Mediator.enable_button('worstcase')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('reset')
        Mediator.enable_button('sort')

        self.shuffling = False

    def final_touch_thread(self):
        l = len(self.element_list)
        for element in self.element_list:
            self.canvas.itemconfig(element.shape, fill = "green")
            time.sleep(1/l)
        for element in self.element_list:
            self.canvas.itemconfig(element.shape, fill = "white")

        Mediator.enable_button('worstcase')
        Mediator.enable_button('set')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')

        Mediator.disable_button('pause')
        Mediator.disable_button('stop')
        Mediator.disable_button('resume')
        self.sorting = False

    def change_colour_thread(self, el_index, color, delay):
        self.colored[el_index] += 1
        self.canvas.itemconfig(self.element_list[el_index].shape, fill = color)
        time.sleep(delay)
        if self.colored[el_index] == 1:
            self.canvas.itemconfig(self.element_list[el_index].shape, fill='white')
        self.colored[el_index] -= 1

    def pause_sort(self):
        self.pause_sorting = True
        Mediator.enable_button('resume')
        Mediator.disable_button('pause')

    def resume_sort(self):
        self.pause_sorting = False
        Mediator.disable_button('resume')
        Mediator.enable_button('pause')

    def __erase_elements(self):
        self.canvas.delete('all')
        self.element_list.clear()
        self.init_coords.clear()

    def stop_sort(self):
        Mediator.disable_button('stop')
        Mediator.disable_button('pause')
        Mediator.disable_button('resume')

        Mediator.enable_button('worstcase')
        Mediator.enable_button('set')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('reset')
        Mediator.enable_button('showall')
        self.stop_sorting = True
        self.pause_sorting = True

    def reset(self):
        l = len(self.element_list)
        for i in range(0, l):
            self.overwrite_element(i, self.init_coords[i])
        Mediator.disable_button('reset')

    def set_number_of_elements(self):
        elNum = self.ElNumComboBox.comboBox.get()
        if elNum in self.ElNumComboBox.comboBox['values']:
            self.__erase_elements()
            self.elementWidth = self.screenL // int(elNum)
            self.__init_elements()

    def set_delay(self):
        delay = self.DelayEntry.get()
        try:
            if delay != 'Def':
                delay = float(delay)
                if delay <= 100000:
                    self.delay = float(delay) / 1000
                else:
                    delay = 100000
                    self.DelayEntry.set('100000')
                    self.delay = float(delay) / 1000
        except:
            msgbox.showerror("Delay input error", "Enter a correct value!")


    def show_all_algorithms(self):
        Mediator.disable_button('worstcase')
        Mediator.disable_button('set')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')
        Mediator.disable_button('resume')
        Mediator.disable_button('showall')

        Mediator.enable_button('pause')
        Mediator.enable_button('stop')

        thrd.Thread(target = self.show_all_algorithms_thread).start()

    def show_all_algorithms_thread(self):
        self.shuffle()
        self.ComboBox.comboBox.set('Stupid Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else: break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else: break

        time.sleep(1)
        self.shuffle()
        self.ComboBox.comboBox.set('Bubble Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else:
                break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else: break

        time.sleep(1)
        self.shuffle()
        self.ComboBox.comboBox.set('Selection Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else:
                break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else: break

        time.sleep(1)
        self.shuffle()
        self.ComboBox.comboBox.set('Double Selection Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else:
                break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else:
                break

        time.sleep(1)
        self.shuffle()

        self.ComboBox.comboBox.set('Insertion Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else:
                break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else: break
        time.sleep(1)
        self.shuffle()
        self.ComboBox.comboBox.set('Merge Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else: break
        time.sleep(1)

        self.sort()

        while True:
            if self.sorting == True:
                time.sleep(0.1)
            else: break
        time.sleep(1)
        self.shuffle()
        self.ComboBox.comboBox.set('Quick Sort')

        while True:
            if self.shuffling == True:
                time.sleep(0.1)
            else: break
        time.sleep(1)

        self.sort()

        Mediator.enable_button('set')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('showall')

        Mediator.disable_button('pause')
        Mediator.disable_button('stop')
        Mediator.disable_button('resume')
        
    def set_elements_to_worst_case(self):
        elNum = self.ElNumComboBox.comboBox.get()
        if elNum in self.ElNumComboBox.comboBox['values']:
            self.__erase_elements()
            self.elementWidth = self.screenL // int(elNum)
            self.__init_elements()

        l = len(self.element_list)
        if l > 255: l -= 1

        for i in range(0, l//2):
            self.swp(i, l - i - 2)

class ImprovedComboBox:
    def __init__(self, master, values, width, pack):
        self.StringVariable = tk.StringVar()
        self.comboBox = ttk.Combobox(master = master, textvariable = self.StringVariable, width = width)
        self.values = values
        self.comboBox['values'] = values

        self.comboBox.bind('<KeyPress>', self.Search)
        self.comboBox.bind('<KeyRelease>', self.Search)

        if pack is True:
            self.comboBox.pack()

    def Search(self, event):
        searchValue = event.widget.get()
        goodValues = []
        if searchValue == '' or searchValue == " ":
            goodValues = self.values
        else:
            goodValues = [name for name in self.values if searchValue.lower() in name.lower()]

        self.comboBox['values'] = goodValues

# \/\/\/ OPTIONS \/\/\/

OptionsFrame = ttk.Frame(win)

ElNumComboBoxVariable = tk.StringVar()
ElNumComboBoxLabel = ttk.Label(OptionsFrame, text = "Set number of elements:")
ElNumComboBoxLabel.grid(row = 3, column = 0, columnspan = 2)
ElNumComboBox = ImprovedComboBox(OptionsFrame, ('8', '16', '32', '64', '128', '256', '512'), 3, False)
ElNumComboBox.comboBox.set('256')

SortComboBoxLabel = ttk.Label(OptionsFrame, text = "Choose sorting algorithm")
SortComboBoxLabel.grid(row = 0, column = 0, columnspan = 2)

SortComboBox = ImprovedComboBox(OptionsFrame, ('Stupid Sort', 'Bubble Sort', 'Selection Sort',
                                                            'Double Selection Sort', 'Insertion Sort',
                                                            'Merge Sort', 'Quick Sort'), 20, False)
SortComboBox.comboBox.grid(row = 1, column = 0, columnspan = 2)
SortComboBox.comboBox.set('Quick Sort')

DelayEntryTextVar = tk.StringVar()
DelayEntry = ttk.Entry(OptionsFrame, width = 6, textvariable=DelayEntryTextVar)
DelayEntryTextVar.set('Def')


Mediator = Mediator(None)
sortingScreen = sortingScreen(win, 0, 0, 2, 512, SortComboBox, ElNumComboBox, DelayEntry, Mediator)

ElNumSetButton = ttk.Button(OptionsFrame, text = "SET", command = sortingScreen.set_number_of_elements, width = 15)
ElNumSetButton.grid(row = 4, column = 1)
ElNumComboBox.comboBox.grid(row = 4, column = 0)

DelayLabel = ttk.Label(OptionsFrame, text = 'Set delay (in miliseconds):')
DelayEntrySetButton = ttk.Button(OptionsFrame, text = "SET", command = sortingScreen.set_delay, width = 15)

DelayLabel.grid(row = 5, column = 0, columnspan = 2)
DelayEntry.grid(row = 6, column = 0)
DelayEntrySetButton.grid(row = 6, column = 1)

OptionsFrame.grid(row = 0, column = 1, rowspan = 5)

# /\/\/\ OPTIONS /\/\/\

ButtonFrame = tk.Frame(win)

ShuffleButton = ttk.Button(ButtonFrame,      text = "SHUFFLE",           command = sortingScreen.shuffle,     width = 20)
ResetButton =   ttk.Button(ButtonFrame,      text = "RESET",             command = sortingScreen.reset,       width = 20)
SortButton =    ttk.Button(ButtonFrame,      text = "SORT",              command = sortingScreen.sort,        width = 20)
PauseButton =   ttk.Button(ButtonFrame,      text = "PAUSE SORTING",     command = sortingScreen.pause_sort,  width = 20)
ResumeButton =  ttk.Button(ButtonFrame,      text = "RESUME SORTING",    command = sortingScreen.resume_sort, width = 20)
StopButton =    ttk.Button(ButtonFrame,      text = "STOP SORTING",      command = sortingScreen.stop_sort,   width = 20)
ExitButton =    ttk.Button(ButtonFrame,      text = "EXIT",              command = win.destroy,               width = 20)
WorstCaseButton=ttk.Button(ButtonFrame,      text = "SET TO WORST CASE", command = sortingScreen.set_elements_to_worst_case, width = 20)
ShowAllSortsButton = ttk.Button(ButtonFrame, text = "SHOW ALL SORTS",    command = sortingScreen.show_all_algorithms, width = 20)

Mediator.buttons = {'set'       :ElNumSetButton,
                     'shuffle'  :ShuffleButton,
                     'reset'    :ResetButton,
                     'sort'     :SortButton,
                     'pause'    :PauseButton,
                     'resume'   :ResumeButton,
                     'stop'     :StopButton,
                     'showall'  :ShowAllSortsButton,
                     'worstcase':WorstCaseButton}

ResetButton['state']  = 'disabled'
PauseButton['state']  = 'disabled'
ResumeButton['state'] = 'disabled'
StopButton['state']   = 'disabled'

WorstCaseButton.pack()
ShuffleButton.pack()
ResetButton.pack()
SortButton.pack()
ShowAllSortsButton.pack()
PauseButton.pack()
ResumeButton.pack()
StopButton.pack()
ExitButton.pack()

ButtonFrame.grid(row = 5, column = 1, rowspan = 9)


win.mainloop()

if __name__ == "__main__":
    pass