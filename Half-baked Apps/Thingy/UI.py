import tkinter as tk
import tkinter.ttk as ttk
import threading as thrd
import time
import random
import Sorting

# Application Front End

win = tk.Tk()
win.geometry("700x550")
win.title("Sorting Algorithms Visualised")
win.resizable(False, False)
#win.configure(background='#999999')

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
    def __init__(self, master, row, column, elementwidth, screenL, ComboBox, ElNumComboBox, Mediator):
        self.ComboBox = ComboBox
        self.ElNumComboBox = ElNumComboBox
        self.screenL = screenL
        self.elementWidth = elementwidth
        self.mediator = Mediator

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
        Mediator.disable_button('shuffle')
        Mediator.disable_button('reset')
        Mediator.disable_button('sort')

        shuffle_indexes = [i for i in range(0, len(self.element_list) - 1)]
        random.shuffle(shuffle_indexes)
        thrd.Thread(target = self.shuffling_thread, args = (shuffle_indexes, )).start()

    def sort(self):
        Mediator.disable_button('set')
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
            swap_dq, comparisons = Sorting.Sort_np.MergeSort(indexes, 0, len(indexes))
            thrd.Thread(target=self.merge_sorting_thread, args=(swap_dq,)).start()
        else:
            swap_dq = 0
            match type:
                case 'Stupid Sort':
                    swap_dq, comparisons = Sorting.Sort_np.StupidSort(indexes)
                case 'Bubble Sort':
                    swap_dq, comparisons = Sorting.Sort_np.BubbleSort(indexes)
                case 'Selection Sort':
                    swap_dq, comparisons = Sorting.Sort_np.SelectionSort(indexes)
                case 'Insertion Sort':
                    swap_dq, comparisons = Sorting.Sort_np.InsertionSort(indexes)
                case 'Quick Sort':
                    swap_dq, comparisons = Sorting.Sort_np.QuickSort(indexes, 0, len(indexes))
            thrd.Thread(target=self.sorting_thread, args=(swap_dq,)).start()

    def merge_sorting_thread(self, swap_dq):

        while swap_dq:
            if self.stop_sorting is True:
                break
            if self.pause_sorting is False:

                left = swap_dq[0][0]
                right = swap_dq[0][1]

                obj_arr_coords = [self.canvas.coords(self.element_list[k].shape) for k in swap_dq[0][2]]

                k = 0
                for i in range(left, right):
                    self.canvas.itemconfig(self.element_list[i].shape, fill='red')
                    self.overwrite_element(i, obj_arr_coords[k])
                    time.sleep(0.005)
                    self.canvas.itemconfig(self.element_list[i].shape, fill='white')
                    k += 1
                swap_dq.popleft()
            else: time.sleep(0.005)

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
                self.canvas.itemconfig(swap[1], fill = 'red')
                self.swp(swap[1], swap[0])
                swap_dq.popleft()
                time.sleep(1/l)
                self.canvas.itemconfig(swap[1], fill='white')
            else: time.sleep(1/l)
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
        Mediator.enable_button('shuffle')
        Mediator.enable_button('reset')
        Mediator.enable_button('sort')

    def final_touch_thread(self):
        l = len(self.element_list)
        for element in self.element_list:
            self.canvas.itemconfig(element.shape, fill = "green")
            time.sleep(1/l)
        for element in self.element_list:
            self.canvas.itemconfig(element.shape, fill = "white")

        Mediator.enable_button('set')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')

        Mediator.disable_button('pause')
        Mediator.disable_button('stop')
        Mediator.disable_button('resume')

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

        Mediator.enable_button('set')
        Mediator.enable_button('shuffle')
        Mediator.enable_button('sort')
        Mediator.enable_button('reset')
        self.stop_sorting = True
        self.pause_sorting = True

    def reset(self):
        l = len(self.element_list)
        for i in range(0, l):
            self.overwrite_element(i, self.init_coords[i])
        Mediator.disable_button('reset')

    def set_element_number(self):
        elNum = self.ElNumComboBox.comboBox.get()
        if elNum in self.ElNumComboBox.comboBox['values']:
            self.__erase_elements()
            self.elementWidth = self.screenL // int(elNum)
            self.__init_elements()

class ImprovedComboBox:
    def __init__(self, master, values):
        self.StringVariable = tk.StringVar()
        self.comboBox = ttk.Combobox(master = master, textvariable = self.StringVariable)
        self.values = values
        self.comboBox['values'] = values

        self.comboBox.bind('<KeyPress>', self.Search)
        self.comboBox.bind('<KeyRelease>', self.Search)

        self.comboBox.pack()

    def Search(self, event):
        searchValue = event.widget.get()
        goodValues = []
        if searchValue == '' or searchValue == " ":
            goodValues = self.values
        else:
            goodValues = [name for name in self.values if searchValue.lower() in name.lower()]

        self.comboBox['values'] = goodValues

ElNumComboBoxFrame = ttk.Frame(win)

ElNumComboBoxVariable = tk.StringVar()
ElNumComboBoxLabel = ttk.Label(ElNumComboBoxFrame, text = "Set number of elements:")
ElNumComboBoxLabel.pack()
ElNumComboBox = ImprovedComboBox(ElNumComboBoxFrame, ('8', '16', '32', '64', '128', '256', '512'))
ElNumComboBox.comboBox.set('256')

SortComboBoxFrame = tk.Frame(win)
SortComboBoxLabel = ttk.Label(SortComboBoxFrame, text = "Choose sorting algorithm")
SortComboBoxLabel.pack()

SortComboBox = ImprovedComboBox(SortComboBoxFrame, ('Stupid Sort', 'Bubble Sort', 'Selection Sort',
                                                            'Insertion Sort', 'Merge Sort', 'Quick Sort'))
SortComboBox.comboBox.set('Stupid Sort')
SortComboBoxFrame.grid(row = 0, column = 1, rowspan = 2)

Mediator = Mediator(None)
sortingScreen = sortingScreen(win, 0, 0, 2, 512, SortComboBox, ElNumComboBox, Mediator)

SetElNumButton = ttk.Button(ElNumComboBoxFrame, text = "SET", command = sortingScreen.set_element_number, width = 22)
SetElNumButton.pack(pady = 2)

ElNumComboBoxFrame.grid(row = 2, column = 1, rowspan = 3)

ButtonFrame = tk.Frame(win)

ShuffleButton = ttk.Button(ButtonFrame, text = "SHUFFLE",        command = sortingScreen.shuffle,     width = 20)
ResetButton =   ttk.Button(ButtonFrame, text = "RESET",          command = sortingScreen.reset,       width = 20)
SortButton =    ttk.Button(ButtonFrame, text = "SORT",           command = sortingScreen.sort,        width = 20)
PauseButton =   ttk.Button(ButtonFrame, text = "PAUSE SORTING",  command = sortingScreen.pause_sort,  width = 20)
ResumeButton =  ttk.Button(ButtonFrame, text = "RESUME SORTING", command = sortingScreen.resume_sort, width = 20)
StopButton =    ttk.Button(ButtonFrame, text = "STOP SORTING",   command = sortingScreen.stop_sort,   width = 20)
ExitButton =    ttk.Button(ButtonFrame, text = "EXIT",           command = win.destroy,               width = 20)

Mediator.buttons = {'set'    :SetElNumButton,
                     'shuffle':ShuffleButton,
                     'reset'  :ResetButton,
                     'sort'   :SortButton,
                     'pause'  :PauseButton,
                     'resume' :ResumeButton,
                     'stop'   :StopButton}

ResetButton['state'] = 'disabled'
PauseButton['state'] = 'disabled'
ResumeButton['state'] = 'disabled'
StopButton['state'] = 'disabled'

ShuffleButton.pack()
ResetButton.pack()
SortButton.pack()
PauseButton.pack()
ResumeButton.pack()
StopButton.pack()
ExitButton.pack()

ButtonFrame.grid(row = 5, column = 1, rowspan = 7)

win.mainloop()

if __name__ == "__main__":
    pass
