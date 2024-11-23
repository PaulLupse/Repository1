import threading as thrd
import time
import numpy as np

class CDTimer:
    def __init__(self, period):
        self.running = False
        self.period = period
        self.__pperiod = period
        self.__pause = False
        self.__stop = False

    def __run(self):
        while self.__pperiod > 0 and self.__stop is not True:
            if self.__pause is not True:
                self.__pperiod -= 0.01
                time.sleep(0.01)

        self.running = False
        self.__stop = False
        return

    def start_timer(self):
        thrd.Thread(target = self.__run).start()
        self.running = True

    def pause_timer(self):
        self.__pause = True
        self.running = False

    def resume_timer(self):
        self.__pause = False
        self.running = True

    def stop_timer(self):
        self.__stop = True
        self.running = False

class StopWatch:
    def __init__(self):
        self.__start_time = 0
        self.__stop_time = 0
        self.time_passed = 0

    def start_timer(self):
        self.__start_time = time.time()

    def pause_timer(self):
        self.__stop_time = time.time()
        self.time_passed = self.__stop_time - self.__start_time

    def resume_timer(self):
        self.__start_time = time.time()

    def stop_timer(self):
        self.__stop_time = time.time()
        self.time_passed += self.__stop_time - self.__start_time

class Sort:

    @staticmethod
    def BubbleSort(arr):
        arrL = len(arr)
        sorted = False
        j = 0
        while sorted is False:
            sorted = True
            for i in range(0, arrL - 1 - j):
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            j += 1

    @staticmethod
    def StupidSort(arr):
        arrL = len(arr)
        for i in range(0, arrL - 1):
            for j in range(i + 1, arrL):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def SelectionSort(arr):
        arrL = len(arr)
        for i in range(0, arrL - 1):
            imin = i
            for j in range(i + 1, arrL):
                if arr[j] < arr[imin]:
                    imin = j

            arr[imin], arr[i] = arr[i], arr[imin]

    @staticmethod
    def InsertionSort(arr):
        arrL = len(arr)
        arr2 = np.zeros((arrL,), np.int64)
        k = 0
        for number in arr:
            i = k
            while arr2[i-1] > number and i-1 >= 0:
                arr2[i] = arr2[i-1]
                i -= 1
            arr2[i] = number
            k += 1

        for i in range(0, arrL):
            arr[i] = arr2[i]

    def MergeSort(self, arr):
        if len(arr) > 1:
            p = (len(arr))//2
            self.MergeSort(arr[0:p])
            self.MergeSort(arr[p:len(arr)])
            InterclassedArr = Interclass_np(arr[0:p], arr[p:len(arr)])
            k = 0
            for i in range(0, len(arr)):
                arr[i] = InterclassedArr[k]
                k += 1

    def QuickSort(self, arr):
        if len(arr) > 1:
            p = arr[0]
            i = -1; j = len(arr)
            while True:
                while True:
                    i += 1
                    if p <= arr[i]:
                        break

                while True:
                    j -= 1
                    if p >= arr[j]:
                        break

                if i > j:
                    break

                arr[i], arr[j] = arr[j], arr[i]

            self.QuickSort(arr[0:i])
            self.QuickSort(arr[i:len(arr)])

    def HeapSort(self, arr):
        pass


def Interclass_np(arr1, arr2):
    i = 0; arr1L = len(arr1)
    j = 0; arr2L = len(arr2)
    k = 0

    arrk = np.zeros((arr1L + arr2L,), np.int64)

    while i < arr1L and j < arr2L:
        if arr1[i] < arr2[j]:
            arrk[k] = arr1[i]
            i += 1
        else:
            arrk[k] = arr2[j]
            j += 1
        k += 1

    while i < arr1L:
        arrk[k] = arr1[i]
        i += 1
        k += 1
    while j < arr2L:
        arrk[k] = arr2[j]
        j += 1
        k += 1

    return arrk


if __name__ == "__main__":
    a = np.array([1, 6, 5, 7, 1, 9])
    b = np.array([9, 4, 2, 10, 1])

    s = Sort()

    s.MergeSort(a)
    s.MergeSort(b)

    print(a, b)

    print(Interclass_np(a, b))

