import numpy as np
import random

class game_matrix:

    def __init__(self, shape):

        self._shape = shape
        print(shape)
        self._matrix = np.zeros((shape[0]+6, shape[1]+6), dtype = np.int8)
        self._destroyed = dict()

        for i in range(0, shape[1]):
            self._destroyed[i] = 0

    # genereaza o matrice random
    def generate_matrix(self):

        matrix_shape = self._shape
        for i in range(0, matrix_shape[0]):
            for j in range(0, matrix_shape[1]):
                self._matrix[i][j] = random.randrange(1, 5)

    # matrix = np.ndarray
    def set_matrix(self, matrix):

        for i in range(0, matrix.shape[0]):
            for j in range(0, matrix.shape[1]):
                self._matrix[i][j] = matrix[i][j]

    def coord_is_ok(self, x, y):
        if x < self._shape[0] and y < self._shape[1]:
            return True
        return False

    def swap(self, x1, y1, x2, y2):
        self._matrix[x1][y1], self._matrix[x2][y2] = self._matrix[x2][y2], self._matrix[x1][y1]

    def search_pattern_5line(self):

        matrix_shape = self._shape
        i = 0
        pct_cnt = 0
        while i < matrix_shape[0]:
            j = 0
            while j < matrix_shape[1]:
                if self._matrix[i][j] == self._matrix[i][j+1] == self._matrix[i][j+2] == self._matrix[i][j+3] == self._matrix[i][j+4] != 0:
                    pct_cnt += 50
                    self._matrix[i][j] = self._matrix[i][j+1] = self._matrix[i][j+2] = self._matrix[i][j+3] = self._matrix[i][j+4] = 0
                    self._destroyed[j] += 1
                    self._destroyed[j+1] += 1
                    self._destroyed[j+2] += 1
                    self._destroyed[j+3] += 1
                    self._destroyed[j+4] += 1
                    j += 4
                elif self._matrix[i][j] == self._matrix[i+1][j] == self._matrix[i+2][j] == self._matrix[i+3][j] == self._matrix[i+4][j] != 0:
                    pct_cnt += 50
                    self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = self._matrix[i + 3][j] = self._matrix[i + 4][j] = 0
                    self._destroyed[j] += 5
                j+=1
            i+=1

        return pct_cnt

    def search_pattern_4line(self):

        matrix_shape = self._shape
        i = 0
        pct_cnt = 0
        while i < matrix_shape[0]:
            j = 0
            while j < matrix_shape[1]:
                if self._matrix[i][j] == self._matrix[i][j + 1] == self._matrix[i][j + 2] == self._matrix[i][j + 3]  != 0:
                    pct_cnt += 10
                    self._matrix[i][j] = self._matrix[i][j + 1] = self._matrix[i][j + 2] = self._matrix[i][j + 3] = 0
                    self._destroyed[j] += 1
                    self._destroyed[j + 1] += 1
                    self._destroyed[j + 2] += 1
                    self._destroyed[j + 3] += 1
                    j += 3
                elif self._matrix[i][j] == self._matrix[i + 1][j] == self._matrix[i + 2][j] == self._matrix[i + 3][j] != 0:
                    pct_cnt += 10
                    self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = self._matrix[i + 3][j] = 0
                    self._destroyed[j] += 4
                j += 1
            i += 1


        return pct_cnt

    def search_pattern_3line(self):

        matrix_shape = self._shape
        i = 0
        pct_cnt = 0
        while i < matrix_shape[0]:
            j = 0
            while j < matrix_shape[1]:
                if self._matrix[i][j] == self._matrix[i][j + 1] == self._matrix[i][j + 2] != 0:
                    pct_cnt += 5
                    self._matrix[i][j] = self._matrix[i][j + 1] = self._matrix[i][j + 2] = 0
                    self._destroyed[j] += 1
                    self._destroyed[j + 1] += 1
                    self._destroyed[j + 2] += 1
                    j += 2
                elif self._matrix[i][j] == self._matrix[i + 1][j] == self._matrix[i + 2][j] != 0:
                    pct_cnt += 5
                    self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = 0
                    self._destroyed[j] += 3
                j += 1
            i += 1


        return pct_cnt

    def search_potential_pattern_5line(self):

        swap_cnt = 0
        pct_cnt = 0

        shape = self._shape
        i = 0
        while i < shape[0]:
            j = 0
            while j < shape[1]:

                swapped = False

                if self._matrix[i][j] == self._matrix[i][j+1] == self._matrix[i][j+3] == self._matrix[i][j+4] != 0:
                    if self.coord_is_ok(i-1, j+2):
                        if self._matrix[i-1][j+2] == self._matrix[i][j]:
                            swap_cnt += 1; swapped = True
                            self.swap(i, j+2, i-1, j+2)

                    elif self.coord_is_ok(i+1, j+2):
                        if self._matrix[i + 1][j + 2] == self._matrix[i][j]:
                            swap_cnt += 1; swapped = True
                            self.swap(i, j + 2, i + 1, j + 2)

                    if swapped:
                        self._matrix[i][j] = self._matrix[i][j + 1] = self._matrix[i][j + 2] = self._matrix[i][j + 3] = \
                        self._matrix[i][j + 4] = 0
                        self._destroyed[j] += 1
                        self._destroyed[j + 1] += 1
                        self._destroyed[j + 2] += 1
                        self._destroyed[j + 3] += 1
                        self._destroyed[j + 4] += 1


                        print(i, ' ', j, ' ', i, ' ', j+4)

                        j += 4

                        pct_cnt += 50

                elif self._matrix[i][j] == self._matrix[i + 1][j] == self._matrix[i + 3][j] == self._matrix[i + 4][j] != 0:
                    if self.coord_is_ok(i+2, j-1):
                        if self._matrix[i+2][j-1] == self._matrix[i][j]:
                            swap_cnt += 1; swapped = True
                            self.swap(i+2, j, i+2, j-1)
                    elif self.coord_is_ok(i+2, j-1):
                        if self._matrix[i+2][j+1] == self._matrix[i][j]:
                            swap_cnt += 1; swapped = True
                            self.swap(i+2, j, i+2, j+1)

                    if swapped:
                        pct_cnt += 50
                        self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = self._matrix[i + 3][j] = self._matrix[i + 4][j] = 0
                        print(i, ' ', j, ' ', i+4, ' ', j)
                        self._destroyed[j] += 5

                if swapped:
                    self.gravitate()
                    self.fill()

                j += 1

            i+= 1

        return pct_cnt, swap_cnt

    def search_potential_pattern_4line(self):

        swap_cnt = 0
        pct_cnt = 0

        shape = self._shape
        i = 0
        while i < shape[0]:
            j = 0
            while j < shape[1]:

                swapped = False

                # 0 0 0 0 0 0
                # 0 1 0 1 1 0
                # 0 0 0 0 0 0

                if self._matrix[i][j] == self._matrix[i][j + 2] == self._matrix[i][j + 3]  != 0:

                    # 0 0 1 0 0 0
                    # 0 1 0 1 1 0
                    # 0 0 0 0 0 0

                    if self.coord_is_ok(i-1,j+1):
                        if self._matrix[i-1][j+1] == self._matrix[i][j]:
                            self.swap(i-1, j+1, i, j)
                            swap_cnt += 1; swapped = True

                    # 0 0 0 0 0 0
                    # 0 1 0 1 1 0
                    # 0 0 1 0 0 0

                    elif self.coord_is_ok(i+1,j+1):
                        if self._matrix[i + 1][j + 1] == self._matrix[i][j]:
                            self.swap(i + 1, j + 1, i, j)
                            swap_cnt += 1; swapped = True

                    if swapped:
                        pct_cnt += 10
                        self._matrix[i][j] = self._matrix[i][j + 1] = self._matrix[i][j + 2] = self._matrix[i][j + 3] = 0
                        self._destroyed[j] += 1
                        self._destroyed[j + 1] += 1
                        self._destroyed[j + 2] += 1
                        self._destroyed[j + 3] += 1


                        print(i, ' ', j, ' ', i, ' ', j+3)

                        j += 3

                # 0 0 0 0 0 0
                # 0 1 1 0 1 0
                # 0 0 0 0 0 0

                elif self._matrix[i][j] == self._matrix[i][j + 1] == self._matrix[i][j + 3]  != 0:

                    # 0 0 0 1 0 0
                    # 0 1 1 0 1 0
                    # 0 0 0 0 0 0

                    if self.coord_is_ok(i-1,j+2):
                        if self._matrix[i-1][j+2] == self._matrix[i][j]:
                            self.swap(i-1, j+2, i, j)
                            swap_cnt += 1; swapped = True

                    # 0 0 0 0 0 0
                    # 0 1 1 0 1 0
                    # 0 0 0 1 0 0

                    elif self.coord_is_ok(i+1,j+2):
                        if self._matrix[i + 1][j + 2] == self._matrix[i][j]:
                            self.swap(i + 1, j + 2, i, j)
                            swap_cnt += 1; swapped = True
                    if swapped:
                        pct_cnt += 10
                        self._matrix[i][j] = self._matrix[i][j + 1] = self._matrix[i][j + 2] = self._matrix[i][j + 3] = 0
                        self._destroyed[j] += 1
                        self._destroyed[j + 1] += 1
                        self._destroyed[j + 2] += 1
                        self._destroyed[j + 3] += 1

                        print(i, ' ', j, ' ', i+3, ' ', j)
                        j += 3

                # 0 0 0
                # 0 1 0
                # 0 0 0
                # 0 1 0
                # 0 1 0
                # 0 0 0

                elif self._matrix[i][j] == self._matrix[i + 2][j] == self._matrix[i + 3][j] != 0:

                    # 0 0 0
                    # 0 1 0
                    # 1 0 0
                    # 0 1 0
                    # 0 1 0
                    # 0 0 0

                    if self.coord_is_ok(i+1, j-1):
                        if self._matrix[i+1][j-1] == self._matrix[i][j]:
                            self.swap(i+1, j, i+1, j-1)
                            swap_cnt += 1; swapped = True

                    # 0 0 0
                    # 0 1 0
                    # 0 0 1
                    # 0 1 0
                    # 0 1 0
                    # 0 0 0

                    elif self.coord_is_ok(i+1, j+1):
                        if self._matrix[i+1][j+1] == self._matrix[i][j]:
                            self.swap(i+1, j, i+1, j+1)
                            swap_cnt += 1; swapped = True

                    if swapped:
                        pct_cnt += 10
                        self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = self._matrix[i + 3][j] = 0
                        self._destroyed[j] += 4

                # 0 0 0
                # 0 1 0
                # 0 1 0
                # 0 0 0
                # 0 1 0
                # 0 0 0

                elif self._matrix[i][j] == self._matrix[i + 1][j] == self._matrix[i + 3][j] != 0:

                    # 0 0 0
                    # 0 1 0
                    # 0 1 0
                    # 1 0 0
                    # 0 1 0
                    # 0 0 0

                    if self.coord_is_ok(i+2, j-1):
                        if self._matrix[i][j] == self._matrix[i+2][j-1]:
                            self.swap(i+2, j, i+2, j-1)
                            swap_cnt += 1; swapped = True

                    # 0 0 0
                    # 0 1 0
                    # 0 1 0
                    # 0 0 1
                    # 0 1 0
                    # 0 0 0

                    if self.coord_is_ok(i+2, j+1):
                        if self._matrix[i][j] == self._matrix[i+2][j+1]:
                            self.swap(i+2, j, i+2, j+1)
                            swap_cnt += 1; swapped = True

                    if swapped:
                        pct_cnt += 10
                        self._matrix[i][j] = self._matrix[i + 1][j] = self._matrix[i + 2][j] = self._matrix[i + 3][j] = 0
                        self._destroyed[j] += 4

                if swapped:
                    self.gravitate()
                    self.fill()

                j += 1
            i += 1

        return pct_cnt, swap_cnt

    def search_potential_pattern_3line(self):

        pct_cnt = 0
        swap_cnt = 0
        shape = self._shape

        i = 0
        while i < shape[0]-2:
            j = 0
            while j < shape[1]:
                swapped = False
                for k in range(0, 4):

                    if self.coord_is_ok(i-1, j+k):
                        self.swap(i, j+k, i-1, j+k); swapped = True
                        if not self.check_3_line(i, j, 0):
                            self.swap(i, j+k, i - 1, j+k)
                            swapped = False

                    if self.coord_is_ok(i + 1, j+k):
                        self.swap(i, j+k, i + 1, j+k)
                        swapped = True
                        if not self.check_3_line(i, j, 0):
                            self.swap(i, j+k, i + 1, j+k)
                            swapped = False

                    if swapped:

                        for k in range(0, 4):
                            self._matrix[i][j+k] = 0

                        pct_cnt += 1
                        swap_cnt += 1

                        self.gravitate()
                        self.fill()

                        break

                j += 1
            i+= 1

        i = 0
        while i < shape[0]:
            j = 0

            while j < shape[1]-2:
                swapped = False
                for k in range(0, 4):

                    if self.coord_is_ok(i + k, j - 1):
                        self.swap(i + k, j, i + k, j - 1)
                        swapped = True
                        if not self.check_3_line(i + k, j - 1, 1):
                            self.swap(i + k, j, i + k, j - 1)
                            swapped = False

                    if self.coord_is_ok(i + k, j + 1):
                        self.swap(i + k, j, i + k, j + 1)
                        swapped = True
                        if not self.check_3_line(i + k, j + 1, 1):
                            self.swap(i + k, j, i + k, j + 1)
                            swapped = False

                    if swapped:

                        for k in range(0, 4):
                            self._matrix[i][j+k] = 0

                        pct_cnt += 1
                        swap_cnt += 1

                        self.gravitate()
                        self.fill()

                        break


                j += 1
            i += 1

        return pct_cnt, swap_cnt

    def check_3_line(self, x, y, dir):

        if dir == 0:
            return self._matrix[x][y] == self._matrix[x][y+1] == self._matrix[x][y+2] != 0
        return self._matrix[x][y] == self._matrix[x+1][y] == self._matrix[x+2][y] != 0

    def gravitate(self):

        for col in range(0, self._shape[1]):
            has_zeros = False
            for line in range(self._shape[0]-1, -1, -1):

                if self._matrix[line][col] != 0 and has_zeros:
                    k = line+1
                    while self._matrix[k][col] == 0 and k < self._shape[1]:
                        k += 1
                    self._matrix[k-1][col] = self._matrix[line][col]
                    self._matrix[line][col] = 0
                    has_zeros += 1
                elif self._matrix[line][col] == 0:
                    has_zeros = True

    def fill(self):

        for col in range(0, self._shape[1]):

            line = 0
            while self._matrix[line][col] == 0 and line < self._shape[0]:
                self._matrix[line][col] = random.randrange(1, 5)
                line += 1

    def print(self):
        for col in range(0, self._shape[1]*2):
            print("=", end='')
        print()
        for line in range(0, self._shape[0]):
            for col in range(0, self._shape[1]):
                if self._matrix[line][col] == 0:
                    print('#', end=' ')
                else:
                    print(self._matrix[line][col], end=' ')
            print()
        for col in range(0, self._shape[1]*2):
            print("=", end='')
        print()

