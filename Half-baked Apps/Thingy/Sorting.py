import numpy as np
from collections import deque as dq

class Sort_np:
    array_changes = dq()
    comparisons = 0

    @staticmethod
    def BubbleSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        sorted = False
        j = 0
        while sorted is False:
            sorted = True
            for i in range(0, arrL - 1 - j):
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    array_changes.append([i, i+1])
                comparisons += 1
            j += 1
        return array_changes, comparisons

    @staticmethod
    def StupidSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        for i in range(0, arrL - 1):
            for j in range(i + 1, arrL):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    array_changes.append([i, j])
                comparisons += 1
        return array_changes, comparisons

    @staticmethod
    def SelectionSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        for i in range(0, arrL - 1):
            imin = i
            for j in range(i + 1, arrL):
                if arr[j] < arr[imin]:
                    imin = j
                comparisons += 1

            arr[imin], arr[i] = arr[i], arr[imin]
            array_changes.append([imin, i])
        return array_changes, comparisons

    @staticmethod
    def InsertionSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        arr2 = np.zeros((arrL,), np.int64)
        k = 0
        for number in arr:
            i = k
            comparisons = 1
            while arr2[i-1] > number and i-1 >= 0:
                comparisons += 1
                arr2[i] = arr2[i-1]
                array_changes.append([i, i-1])
                i -= 1
            arr2[i] = number
            k += 1

        for i in range(0, arrL):
            arr[i] = arr2[i]

        return array_changes, comparisons

    @classmethod
    def MergeSort(self, arr, left, right):
        global array_changes
        global comparisons

        self.comparisons += 1
        if right - left > 1:
            p = (right + left) // 2
            self.MergeSort(arr=arr, left=left, right=p)
            self.MergeSort(arr=arr, left=p, right=right)

            i = left
            j = p
            k = 0

            arrk = np.zeros(1001, np.int64)
            indarrk = np.zeros(right - left, np.int64)

            while i < p and j < right:
                self.comparisons += 1
                if arr[i] < arr[j]:
                    arrk[k] = arr[i]
                    indarrk[k] = i
                    i += 1
                else:
                    arrk[k] = arr[j]
                    indarrk[k] = j
                    j += 1
                k += 1

            while i < p:
                self.comparisons += 1
                arrk[k] = arr[i]
                indarrk[k] = i
                i += 1
                k += 1
            while j < right:
                self.comparisons += 1
                arrk[k] = arr[j]
                indarrk[k] = j
                j += 1
                k += 1

            k = 0
            self.array_changes.append([left, right, indarrk])
            for i in range(left, right):
                arr[i] = arrk[k]
                k += 1

            if right == len(arr) and left == 0:
                arr_chng = dq([i for i in self.array_changes]); comps = self.comparisons
                while self.array_changes: self.array_changes.popleft()
                self.comparisons = 0
                return arr_chng, comps

    @classmethod
    def QuickSort(self, arr, left, right):
        if right - left > 1:
            p = arr[left]
            i = left - 1; j = right
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

                self.array_changes.append([i, j])
                arr[i], arr[j] = arr[j], arr[i]

            self.QuickSort(arr, left, i)
            self.QuickSort(arr, i, right)

            if right == len(arr) and left == 0:
                arr_chng = dq([i for i in self.array_changes]); comps = self.comparisons
                while self.array_changes: self.array_changes.pop()
                self.comparisons = 0
                return arr_chng, comps

if __name__ == "__main__":


    pass

