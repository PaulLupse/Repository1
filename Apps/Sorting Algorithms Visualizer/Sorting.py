import numpy as np
from collections import deque as dq
from Utilities import getMax as max
from Utilities import binary
from random import shuffle

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
                array_changes.append([i, i + 1, 'comparison'])
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    array_changes.append([i, i+1, 'swap'])
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
                array_changes.append([i, j, 'comparison'])
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    array_changes.append([i, j, 'swap'])
                comparisons += 1
        return array_changes, comparisons

    @staticmethod
    def CocktailShakerSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        sorted = False
        j = 0
        while sorted is False:
            sorted = True
            for i in range(j, arrL - 1 - j):
                array_changes.append([i, i + 1, 'comparison'])
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    array_changes.append([i, i + 1, 'swap'])
                comparisons += 1

            if sorted is False:
                for i in range(arrL - 1 - j, j, -1):
                    array_changes.append([i, i - 1, 'comparison'])
                    if arr[i] < arr[i - 1]:
                        sorted = False
                        arr[i], arr[i - 1] = arr[i - 1], arr[i]
                        array_changes.append([i, i - 1, 'swap'])
                    comparisons += 1
            j += 1
        return array_changes, comparisons

    @staticmethod
    def OddEvenSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        sorted = False
        while sorted is False:
            sorted = True
            for i in range(1, arrL - 1, 2):
                array_changes.append([i, i + 1, 'comparison'])
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    array_changes.append([i, i + 1, 'swap'])
                comparisons += 1

            for i in range(0, arrL - 1, 2):
                array_changes.append([i, i + 1, 'comparison'])
                if arr[i] > arr[i + 1]:
                    sorted = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    array_changes.append([i, i + 1, 'swap'])
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
                array_changes.append([imin, j, 'comparison'])
                if arr[j] < arr[imin]:
                    imin = j
                comparisons += 1

            arr[imin], arr[i] = arr[i], arr[imin]
            array_changes.append([imin, i, 'swap'])
        return array_changes, comparisons

    @staticmethod
    def DoubleSelectionSort(arr):
        array_changes = dq()
        comparisons = 0
        arrL = len(arr)
        i = 0
        j = arrL - 1
        while i < j:
            imin = i
            imax = i
            min = arr[i]
            max = arr[i]
            for k in range(i , j + 1, 1):
                array_changes.append([imax, k, 'comparison'])
                if arr[k] > max:
                    imax = k
                    max = arr[k]
                elif arr[k] < min:
                    array_changes.append([imin, k, 'comparison'])
                    imin = k
                    min = arr[k]

                comparisons += 1

            arr[imin], arr[i] = arr[i], arr[imin]
            array_changes.append([imin, i, 'swap'])

            if arr[imin] == max:
                arr[imin], arr[j] = arr[j], arr[imin]
                array_changes.append([imin, j, 'swap'])
            else:
                arr[imax], arr[j] = arr[j], arr[imax]
                array_changes.append([imax, j, 'swap'])

            i += 1
            j -= 1
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
            for i in range(k, 0, -1):
                array_changes.append([i, i, 'comparison'])
                if arr2[i-1] < number:
                    break
                comparisons += 1
                arr2[i] = arr2[i-1]
                array_changes.append([i, i-1, 'swap'])
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
                self.array_changes.append([i, j, 'comparison', None])
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
            self.array_changes.append([left, right, 'set', indarrk])
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
        if left < right:

            mid = (left + right) // 2
            arr[left], arr[mid] = arr[mid], arr[left]
            self.array_changes.append([left, mid, 'swap'])

            i = left; j = right; d = 0
            while i < j:

                self.array_changes.append([i, j, 'comparison'])

                if arr[i] > arr[j]:

                    arr[i], arr[j] = arr[j], arr[i]
                    d = 1 - d

                    self.array_changes.append([i, j, 'swap'])

                i += d
                j -= 1 - d

            self.QuickSort(arr, left, i - 1)
            self.QuickSort(arr, i + 1, right)


            if right == len(arr) - 1 and left == 0:
                arr_chng = dq([i for i in self.array_changes]); comps = self.comparisons
                while self.array_changes: self.array_changes.pop()
                self.comparisons = 0
                return arr_chng, comps

    @staticmethod
    def __digitCountSort(arr, exp):
        arrL = len(arr)
        count = np.zeros(10, int)
        output = np.zeros(arrL, int)
        outputIndexes = np.zeros(arrL, int)

        for i in range(0, arrL):
            count[(int(arr[i]) // exp) % 10] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        i = len(output) - 1
        while i >= 0:
            index = int(arr[i] // exp)
            outputIndexes[len(output) - 1 - i] = count[index % 10] - 1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        return output, outputIndexes

    @classmethod
    def __heapify(self, arr, arrL, index):
        largest = index
        left = index * 2 + 1
        right = index * 2 + 2

        if left < arrL and arr[left] > arr[largest]:
            yield [largest, left, 'comparison']
            largest = left

        if right < arrL and arr[right] > arr[largest]:
            yield [largest, right, 'comparison']
            largest = right

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            yield [largest, index, 'swap']
            for el in self.__heapify(arr, arrL, largest):
                yield el
        else: yield [None, None]

    @classmethod
    def RadixSortLSD(self, arr):
        array_changes = dq()
        comparisons = 0

        arrL = len(arr)
        arrMax = max(arr)
        exp = 1

        while arrMax//exp > 0:
            countedArr, outputIndexes = self.__digitCountSort(arr, exp)
            outputIndexes = np.flip(outputIndexes, 0)
            for i in range(0, arrL):
                arr[i] = countedArr[i]
                array_changes.append([i, i, 'comparison'])
            array_changes.append([0, arrL, 'set', outputIndexes])
            exp *= 10
            print(arr[len(arr) - 2:])

        return array_changes, comparisons

    @classmethod
    def RadixSortMSD(self, arr, left, right, pos):
        if right <= left or pos < 1: return

        count = np.zeros(12, int)
        temp = np.zeros(right - left + 10, int)

        for i in range(left, right + 1):
            digit = (arr[i] // (10 ** (pos - 1))) % 10
            try:
                count[int(digit)] += 1
            except: print(digit, arr[i], pos)

        for i in range(1, 11):
            count[i] += count[i - 1]

        tempIndexes = np.zeros(right - left + 1, int)

        k = 0
        i = right
        while i >= left:
            digit = (arr[i] // (10 ** (pos - 1))) % 10
            temp[count[int(digit)] - 1] = arr[i]
            tempIndexes[k] = left + count[int(digit)] - 1
            k += 1
            count[int(digit)] -= 1
            i -= 1

        k = 0
        for i in range(left, right + 1):
            arr[i] = temp[k]
            k += 1
            self.array_changes.append([i, i, 'comparison'])

        tempIndexes = np.flip(tempIndexes, 0)
        self.array_changes.append([left, right + 1, 'set', tempIndexes])

        for r in range(10):
            self.RadixSortMSD(arr, left + count[r], left + count[r + 1] - 1, pos - 1)

        if right == len(arr) - 1 and left == 0:
            arr_chng = dq([i for i in self.array_changes])
            comps = self.comparisons
            while self.array_changes: self.array_changes.pop()
            self.comparisons = 0
            return arr_chng, comps

    @staticmethod
    def BogoSort(arr):
        sorted = False
        while not sorted:
            sorted = True
            i = 0
            while i < len(arr) - 1:
                yield [i, i + 1, 'comparison']

                if arr[i] > arr[i + 1]:
                    shuffle(arr)
                    yield [None, None, 'setArray', arr]
                    sorted = False
                    i = 0
                else:
                    i += 1

        yield [None, None, 'sorted', None]

    @classmethod
    def HeapSort(self, arr):
        array_changes = dq()

        arrL = len(arr)

        for i in range(arrL // 2 - 1, -1, -1):
            for el in self.__heapify(arr, arrL, i):
                if el[0] is not None: array_changes.append(el)

        for i in range(arrL - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            array_changes.append([0, i, 'swap', None])
            for el in self.__heapify(arr, i, 0):
                if el[0] is not None: array_changes.append(el)

        return array_changes, 0

if __name__ == "__main__":

    arr = np.array(range(256, 0, -1))
    arr1 = np.array(range(256, 0, -1))

    sort = Sort_np

    arr_chng, a = sort.RadixSortMSD(arr, 0, len(arr) - 1, 3)

    while arr_chng:
        if arr_chng[0][2] == 'set':
            arr1[arr_chng[0][0]], arr1[arr_chng[0][1]] = arr1[arr_chng[0][1]], arr1[arr_chng[0][0]]
        arr_chng.popleft()

    print(arr1)

    pass
