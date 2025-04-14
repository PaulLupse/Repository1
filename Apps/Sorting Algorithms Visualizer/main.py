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
win.title("Sorting Algorithms Visualized")
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
        if border is False:
            self.shape = master.create_rectangle(x + 2, screenL + 2, elementWidth + x + 2, screenL - x - elementWidth + 2 , fill="white", outline='')
        else:
            self.shape = master.create_rectangle(x + 2, screenL + 2, elementWidth + x + 2, screenL - x - elementWidth + 2, fill="white")

class sortingScreen:
    def __init__(self, master, row, column, elementwidth, screenL, ComboBox, elNumComboBox, delay_entry, mediator):
        self.ComboBox = ComboBox
        self.ElNumComboBox = elNumComboBox
        self.DelayEntry = delay_entry
        self.screenL = screenL
        self.elementWidth = elementwidth
        self.mediator = mediator
        self.delay = 0.5
        self.sorting = False
        self.shuffling = False
        self.colored = [0] * 613
        self.master = master

        self.canvas = tk.Canvas(master, bg = "black", bd = 0, width = screenL + 1, height = screenL + 1)
        self.canvas.grid(row=row, column=column, padx=10, pady=10, rowspan = 20)

        self.element_list = []
        self.init_coords = []

        self.pause_sorting = False
        self.stop_sorting = False

        self.__init_elements()

    def __init_elements(self):
        for i in range(0, self.screenL, self.elementWidth):
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
        Mediator.disable_button('set'); Mediator.disable_button('delayset')
        Mediator.disable_button('worstcase')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')
        Mediator.disable_button('showall')

        self.shuffling = True

        shuffle_indexes = [int(i) for i in range(0, len(self.element_list))]
        random.shuffle(shuffle_indexes)

        thrd.Thread(target = self.shuffling_thread, args = (shuffle_indexes, )).start()

    def __decolor_all(self, elementsToDecolor):
        for key in list(elementsToDecolor):
            self.canvas.itemconfig(self.element_list[key].shape, fill='white')
            del elementsToDecolor[key]

    def __decolor_tick(self, elementsToDecolor):
        for key in list(elementsToDecolor):
            elementsToDecolor[key] -= self.delay
            if elementsToDecolor[key] <= 0:
                self.canvas.itemconfig(self.element_list[key].shape, fill='white')
                del elementsToDecolor[key]

    def sort(self):
        l = len(self.element_list)
        self.sorting = True

        Mediator.disable_button('set'); Mediator.disable_button('delayset')
        Mediator.disable_button('worstcase')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')
        Mediator.disable_button('showall')
        Mediator.disable_button('resume')

        Mediator.enable_button('pause')
        Mediator.enable_button('stop')

        Type = self.ComboBox.comboBox.get()

        add = 0
        if l > 255:
            add = 1

        indexes = [int(len(self.element_list) - self.canvas.coords(i.shape)[1]//self.elementWidth) + add for i in self.element_list]
        swap_dq = 0

        match Type:
            case 'Stupid Sort':
                swap_dq = Sorting.Sort_np.StupidSort(indexes)
            case 'Bubble Sort':
                swap_dq = Sorting.Sort_np.BubbleSort(indexes)
            case 'Cocktail Shaker Sort':
                swap_dq = Sorting.Sort_np.CocktailShakerSort(indexes)
            case 'Odd-Even Sort':
                swap_dq = Sorting.Sort_np.OddEvenSort(indexes)
            case 'Selection Sort':
                swap_dq = Sorting.Sort_np.SelectionSort(indexes)
            case 'Double Selection Sort':
                swap_dq = Sorting.Sort_np.DoubleSelectionSort(indexes)
            case 'Insertion Sort':
                swap_dq = Sorting.Sort_np.InsertionSort(indexes)
            case 'Merge Sort':
                swap_dq = Sorting.Sort_np.MergeSort(indexes, 0, len(indexes))
            case 'Quick Sort':
                swap_dq = Sorting.Sort_np.QuickSort(indexes, 0, len(indexes) - 1)
            case 'Radix Sort (LSD)':
                swap_dq = Sorting.Sort_np.RadixSortLSD(indexes)
            case 'Radix Sort (MSD)':
                if l > 99: pos = 3
                elif l > 9: pos = 2
                else: pos = 1
                swap_dq = Sorting.Sort_np.RadixSortMSD(indexes, 0, len(indexes) - 1, pos)
            case 'Heap Sort':
                swap_dq = Sorting.Sort_np.HeapSort(indexes)
            case 'Bogo Sort':
                thrd.Thread(target=self.sorting_thread, args=(swap_dq, indexes, )).start()

        #self.sorting_thread(swap_dq, indexes)
        if Type != 'Bogo Sort': thrd.Thread(target=self.sorting_thread, args=(swap_dq, indexes,)).start()

    def sorting_thread(self, swap_dq, indexes):
        if self.delay >= 0.02:
            decolorDelay = self.delay
        elif self.delay >= 0.01:
            decolorDelay = self.delay * 2
        elif self.delay >= 0.001:
            decolorDelay = self.delay * 10
        else:
            decolorDelay = self.delay * 20

        l = len(self.element_list)

        elementsToDecolor = {}

        sortType = self.ComboBox.comboBox.get()
        if sortType == 'Bogo Sort':
            for step in Sorting.Sort_np.BogoSort(indexes):
                if self.stop_sorting is True:
                    self.__decolor_all(elementsToDecolor)
                    break

                if self.pause_sorting is False:
                    if step[2] == 'sorted':
                        break

                    self.__decolor_tick(elementsToDecolor)

                    if step[2] == 'comparison':
                        self.canvas.itemconfig(self.element_list[step[0]].shape, fill='red')
                        self.canvas.itemconfig(self.element_list[step[1]].shape, fill='red')

                        elementsToDecolor[step[0]] = decolorDelay
                        elementsToDecolor[step[1]] = decolorDelay

                    else:
                        self.__set(step[3])

                    time.sleep(self.delay)
                else:
                    while self.pause_sorting is True and self.stop_sorting is False:
                        time.sleep(0.05)

        elif sortType == 'Merge Sort' or 'Radix Sort' in sortType:
            while swap_dq:

                if self.stop_sorting is True:
                    self.__decolor_all(elementsToDecolor)
                    Mediator.enable_button('reset')
                    break

                if self.pause_sorting is False:
                    self.__decolor_tick(elementsToDecolor)

                    left = swap_dq[0][0]
                    right = swap_dq[0][1]
                    Type = swap_dq[0][2]

                    if Type == 'set':
                        if 'Radix Sort' in sortType :
                            obj_arr_coords = [self.canvas.coords(k.shape) for k in self.element_list[left:right + 1]]

                        else: obj_arr_coords = [self.canvas.coords(self.element_list[k].shape) for k in swap_dq[0][3]]

                        k = 0
                        i = left
                        while i < right:
                            if self.stop_sorting is True:
                                self.__decolor_all(elementsToDecolor)
                                Mediator.enable_button('reset')
                                break
                            if self.pause_sorting is False:
                                self.__decolor_tick(elementsToDecolor)

                                if 'Radix Sort' in sortType:
                                    self.canvas.itemconfig(self.element_list[swap_dq[0][3][k]].shape, fill='green')
                                    self.overwrite_element(swap_dq[0][3][k], obj_arr_coords[k])
                                    elementsToDecolor[swap_dq[0][3][k]] = decolorDelay
                                else:
                                    self.canvas.itemconfig(self.element_list[i].shape, fill= 'green')
                                    self.overwrite_element(i, obj_arr_coords[k])
                                    elementsToDecolor[i] = decolorDelay

                                time.sleep(self.delay)
                                k += 1
                                i += 1
                            else: time.sleep(0.05)
                    else:
                        if sortType == 'Radix Sort':
                            self.canvas.itemconfig(self.element_list[left].shape, fill='red')
                            elementsToDecolor[left] = decolorDelay

                        else:
                            self.canvas.itemconfig(self.element_list[left].shape, fill='red')
                            self.canvas.itemconfig(self.element_list[right].shape, fill='red')

                            elementsToDecolor[left] = decolorDelay
                            elementsToDecolor[right] = decolorDelay

                    time.sleep(self.delay)
                    swap_dq.popleft()
                else: time.sleep(0.05)

        else:
            while swap_dq:
                if self.stop_sorting is True:
                    self.__decolor_all(elementsToDecolor)
                    break

                if self.pause_sorting is False:
                    self.__decolor_tick(elementsToDecolor)

                    el1 = swap_dq[0][0]
                    el2 = swap_dq[0][1]
                    Type = swap_dq[0][2]

                    if Type == 'swap':
                        self.canvas.itemconfig(self.element_list[el1].shape, fill='green')
                        self.canvas.itemconfig(self.element_list[el2].shape, fill='green')
                        self.swp(el1, el2)
                    elif Type == 'setArray':
                        self.__set(el1)
                    else:
                        self.canvas.itemconfig(self.element_list[el1].shape, fill='red')
                        self.canvas.itemconfig(self.element_list[el2].shape, fill='red')


                    elementsToDecolor[el1] = decolorDelay

                    elementsToDecolor[el2] = decolorDelay

                    swap_dq.popleft()
                    time.sleep(self.delay)

                else: time.sleep(0.005)

            if elementsToDecolor:
                self.__decolor_all(elementsToDecolor)

        if elementsToDecolor:
            self.__decolor_all(elementsToDecolor)

        if self.stop_sorting is False:
            thrd.Thread(target=self.final_touch_thread).start()
        else:
            self.stop_sorting = False
            self.pause_sorting = False

        return 0

    def shuffling_thread(self, indexes):
        l = len(self.element_list)
        for i in range(0, len(self.element_list) - 1):
            self.swp(i, indexes[i])
            time.sleep(1 / l)

        Mediator.enable_button('set'); Mediator.enable_button('delayset')
        Mediator.enable_button('worstcase')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('reset')
        Mediator.enable_button('sort')
        Mediator.enable_button('showall')

        self.shuffling = False

        return 0

    def final_touch_thread(self):
        l = len(self.element_list)
        for Element in self.element_list:
            self.canvas.itemconfig(Element.shape, fill ="green")
            time.sleep(1/l)
        for Element in self.element_list:
            self.canvas.itemconfig(Element.shape, fill ="white")

        Mediator.enable_button('worstcase')
        Mediator.enable_button('set'); Mediator.enable_button('delayset')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('showall')

        Mediator.disable_button('pause')
        Mediator.disable_button('stop')
        Mediator.disable_button('resume')
        self.sorting = False

        return 0

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
        Mediator.enable_button('set'); Mediator.enable_button('delayset')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('reset')
        Mediator.enable_button('showall')
        self.stop_sorting = True
        self.pause_sorting = True

    def __set(self, arr):
        l = len(self.element_list)
        for i in range(0, l):
            self.overwrite_element(i, self.init_coords[int(arr[i]) - 1])

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
        if self.elementWidth > 2:
            self.canvas.config(width = self.screenL + 1, height = self.screenL + 1)
        else: self.canvas.config(width = self.screenL, height = self.screenL)

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
        Mediator.disable_button('set'); Mediator.disable_button('delayset')
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')
        Mediator.disable_button('resume')
        Mediator.disable_button('showall')

        Mediator.enable_button('pause')
        Mediator.enable_button('stop')

        thrd.Thread(target = self.show_all_algorithms_thread).start()

    def show_all_algorithms_thread(self):
        pass

        '''Mediator.enable_button('set'); Mediator.enable_button('delayset')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('showall')

        Mediator.disable_button('pause')
        Mediator.disable_button('stop')
        Mediator.disable_button('resume')'''
        
    def set_elements_to_worst_case(self):
        elNum = self.ElNumComboBox.comboBox.get()
        if elNum in self.ElNumComboBox.comboBox['values']:
            self.__erase_elements()
            self.elementWidth = self.screenL // int(elNum)
            self.__init_elements()

        l = len(self.element_list)


        for i in range(0, l//2):
            self.swp(i, l - i - 1)

        if self.elementWidth > 2:
            self.canvas.config(width = self.screenL + 1, height = self.screenL + 1)
        else: self.canvas.config(width = self.screenL, height = self.screenL)

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
ElNumComboBox.comboBox.set('16')

SortComboBoxLabel = ttk.Label(OptionsFrame, text = "Choose sorting algorithm:")
SortComboBoxLabel.grid(row = 0, column = 0, columnspan = 2)

SortComboBox = ImprovedComboBox(OptionsFrame, ('Stupid Sort',
                                                      'Bubble Sort',
                                                      'Cocktail Shaker Sort',
                                                      'Odd-Even Sort',
                                                      'Selection Sort',
                                                      'Double Selection Sort',
                                                      'Insertion Sort',
                                                      'Merge Sort',
                                                      'Quick Sort',
                                                      'Radix Sort (LSD)',
                                                      'Radix Sort (MSD)',
                                                      'Heap Sort',
                                                      'Bogo Sort',), 20, False)

SortComboBox.comboBox.grid(row = 1, column = 0, columnspan = 2)
SortComboBox.comboBox.set('Stupid Sort')

DelayEntryTextVar = tk.StringVar()
DelayEntry = ttk.Entry(OptionsFrame, width = 6, textvariable=DelayEntryTextVar)
DelayEntryTextVar.set('500')


Mediator = Mediator(None)
sortingScreen = sortingScreen(win, 0, 0, 32, 512, SortComboBox, ElNumComboBox, DelayEntry, Mediator)

ElNumSetButton = ttk.Button(OptionsFrame, text = "SET", command = sortingScreen.set_number_of_elements, width = 15)
ElNumSetButton.grid(row = 4, column = 1)
ElNumComboBox.comboBox.grid(row = 4, column = 0)

DelayLabel = ttk.Label(OptionsFrame, text = 'Set delay (in miliseconds):')
DelayEntrySetButton = ttk.Button(OptionsFrame, text = "SET", command = sortingScreen.set_delay, width = 15)

DelayLabel.grid(row = 5, column = 0, columnspan = 2)
DelayEntry.grid(row = 6, column = 0)
DelayEntrySetButton.grid(row = 6, column = 1)

OptionsFrame.grid(row = 0, column = 1, rowspan = 5, padx = 10, pady = 10)

# /\/\/\ OPTIONS /\/\/\

# \/\/\/ BUTTONS \/\/\/

ButtonFrame = tk.Frame(win)

ShuffleButton = ttk.Button(ButtonFrame,      text = "SHUFFLE",           command = sortingScreen.shuffle,                   width = 20)
ResetButton =   ttk.Button(ButtonFrame,      text = "RESET",             command = sortingScreen.reset,                     width = 20)
SortButton =    ttk.Button(ButtonFrame,      text = "SORT",              command = sortingScreen.sort,                      width = 20)
PauseButton =   ttk.Button(ButtonFrame,      text = "PAUSE SORTING",     command = sortingScreen.pause_sort,                width = 20)
ResumeButton =  ttk.Button(ButtonFrame,      text = "RESUME SORTING",    command = sortingScreen.resume_sort,               width = 20)
StopButton =    ttk.Button(ButtonFrame,      text = "STOP SORTING",      command = sortingScreen.stop_sort,                 width = 20)
ExitButton =    ttk.Button(ButtonFrame,      text = "EXIT",              command = win.destroy,                             width = 20)
WorstCaseButton=ttk.Button(ButtonFrame,      text = "SET TO WORST CASE", command = sortingScreen.set_elements_to_worst_case,width = 20)
ShowAllSortsButton = ttk.Button(ButtonFrame, text = "SHOW ALL SORTS",    command = sortingScreen.show_all_algorithms,       width = 20)

Mediator.buttons = {'set'       :ElNumSetButton,
                     'shuffle'  :ShuffleButton,
                     'reset'    :ResetButton,
                     'sort'     :SortButton,
                     'pause'    :PauseButton,
                     'resume'   :ResumeButton,
                     'stop'     :StopButton,
                     'showall'  :ShowAllSortsButton,
                     'worstcase':WorstCaseButton,
                     'delayset' :DelayEntrySetButton}

ResetButton['state']  = 'disabled'
PauseButton['state']  = 'disabled'
ResumeButton['state'] = 'disabled'
StopButton['state']   = 'disabled'

WorstCaseButton.pack()
ShuffleButton.pack()
ResetButton.pack()
SortButton.pack()
#ShowAllSortsButton.pack()
PauseButton.pack()
ResumeButton.pack()
StopButton.pack()
ExitButton.pack()

ButtonFrame.grid(row = 5, column = 1, rowspan = 9)

# /\/\/\ BUTTONS /\/\/\

if __name__ == '__main__':
    win.mainloop()


