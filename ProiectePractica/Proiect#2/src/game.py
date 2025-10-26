from src.game_matrix import game_matrix

class game:
    def __init__(self, _id, _matrix = None, matrix_shape = (11, 11)):

        self.game_id = _id
        self.matrix = game_matrix(matrix_shape)
        self.matrix.generate_matrix()

        print(f"Game {_id} started.")

        new_points = cnt_points = self.matrix.search_pattern_5line() + self.matrix.search_pattern_4line() + self.matrix.search_pattern_3line()
        while new_points != 0:
            self.matrix.gravitate()
            self.matrix.fill()
            new_points = self.matrix.search_pattern_5line() + self.matrix.search_pattern_4line() + self.matrix.search_pattern_3line()
            cnt_points += new_points
            print(cnt_points)

        print(cnt_points)
        self.matrix.print()

        new_points = 1
        cnt_swaps = 0

        while new_points != 0 and cnt_points < 10000:
            print("swap")
            new_points, new_swaps = self.matrix.search_potential_pattern_5line()
            cnt_points += new_points
            cnt_swaps += new_swaps
            new_points, new_swaps = self.matrix.search_potential_pattern_4line()
            cnt_points += new_points
            cnt_swaps += new_swaps
            new_points, new_swaps = self.matrix.search_potential_pattern_3line()
            cnt_points += new_points
            cnt_swaps += new_swaps
            new_points = self.matrix.search_pattern_5line() + self.matrix.search_pattern_4line() + self.matrix.search_pattern_3line()
            self.matrix.gravitate()
            self.matrix.fill()
            cnt_points += new_points

            self.matrix.print()

        self.matrix.print()
        print(cnt_points, cnt_swaps)

