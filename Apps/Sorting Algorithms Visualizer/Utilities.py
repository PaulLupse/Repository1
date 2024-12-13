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
                self.__pperiod -= 0.1
                time.sleep(0.1)

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

def Interclass_np(arr1, arr2):
    i = 0; arr1L = len(arr1)
    j = 0; arr2L = len(arr2)
    k = 0

    arrk = np.zeros((arr1L + arr2L,), np.int64)

    changes = []
    comparisons = 1
    while i < arr1L and j < arr2L:
        comparisons += 1
        if arr1[i] < arr2[j]:
            arrk[k] = arr1[i]
            changes.append(i)
            i += 1
        else:
            arrk[k] = arr2[j]
            changes.append(j)
            j += 1
        k += 1

    while i < arr1L:
        comparisons += 1
        arrk[k] = arr1[i]
        changes.append(i)
        i += 1
        k += 1
    while j < arr2L:
        comparisons += 1
        arrk[k] = arr2[j]
        changes.append(j)
        j += 1
        k += 1

    return arrk, comparisons, changes

def CarbonCopy(arr):
    arrCopy = [i for i in arr]
    return arrCopy

def getMax(arr):
    max = arr[0]
    for nr in arr:
        if nr > max:
            max = nr

    return max

def getNumLen(number):
    nrdig = 0
    cpn = number
    while cpn:
        nrdig += 1
        cpn /= 10
    return nrdig

if __name__ == "__main__":
    pass

