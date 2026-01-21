from src.game_matrix import GameMatrix

import datetime

# clasa ce implementeaza jocul Candy Crush Automatizat
class Game:
    def __init__(self, game_id, matrix = None, matrix_shape = (11, 11)):

        # jocul este reprezentat prin intermediul unui obiect de tip GameMatrix
        self.matrix = GameMatrix(matrix_shape)
        self.matrix_shape = matrix_shape
        self.game_id = game_id

        # daca nu a fost introdusa o matrice predefinita, se genereaza o matrice de joc
        if matrix is None:
            self.matrix.generate_matrix()
        else:
            self.matrix.set_matrix(matrix)

    # metoda ce determina rularea jocului, luand ca parametru tinta de puncte
    def play(self, target):

        print(f"Jocul {self.game_id} început la: {datetime.datetime.now()}.", end=' ')

        # la inceputul fiecarui joc, efectuam o cautare cascada a tuturor formatiunilor deja formate initial
        # punctele rezultate din aceasta cautare sunt adunate la punctele totale
        cnt_points = self.matrix.search_patterns(0, target)
        cnt_swaps = 0

        new_points = 1 # initial new_points are valoarea 1 ca sa putem intra in while
        while new_points != 0  and cnt_points < target:

            # cautam toate formele potentiale de tip linie de 5, care ofera 50p
            new_points, new_swaps = self.matrix.search_potential_pattern_5_line(cnt_points, target)
            cnt_points += new_points
            cnt_swaps += new_swaps
            if new_swaps:
                continue

            # cautam toate formele potentiale de tip L, care ofera 20p
            new_points, new_swaps = self.matrix.search_potential_pattern_L(cnt_points, target)
            cnt_points += new_points
            cnt_swaps += new_swaps
            if new_swaps:
                continue

            # cautam toate formele potentiale de tip linie de 4, care ofera 10p
            new_points, new_swaps = self.matrix.search_potential_pattern_4_line(cnt_points, target)
            cnt_points += new_points
            cnt_swaps += new_swaps
            if new_swaps:
                continue

            # cautam toate formele potentiale de tip linie de 3, care ofera 5p
            new_points, new_swaps = self.matrix.search_potential_pattern_3_line(cnt_points, target)
            cnt_points += new_points
            cnt_swaps += new_swaps
            if new_swaps:
                continue

        # obs: este omisa cautarea formelor de tip T deoarece (in momentul scrierii acestui comentariu) acestea ofera
        # doar 30p, desi implica o forma de tip linie de 5
        # astfel este inutil sa mai verificam

        if cnt_points >= target:
            print("Terminare: " +  "\033[92m{}\033[00m".format("Țintă atinsă."))
        else:
            print("Terminare: " +  "\033[91m{}\033[00m".format("Fără mișcări."))

        return cnt_points, cnt_swaps