from collections import deque as dq
import numpy as np

try:
    import Shared
except: from . import Shared

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
dci = (-1, 1, 1, -1)
dcj = (1, 1, -1, -1)

class info:
    def __init__(self, x_p, y_p):
        self.x_p = x_p
        self.y_p = y_p
        self.x_p = self.y_p = 0
        self.is_visited = False

def lee(matrix, x_start, y_start, x_target, y_target, Type): # matrix takes np.ndarray as input (indexed from 0)
    info = init_parents(matrix.shape[0], matrix.shape[1])

    matrix = Shared.border(matrix, matrix.shape[0], matrix.shape[1])

    queue = dq()
    changes_queue = dq()
    info[x_start][y_start].x_p = None
    info[x_start][y_start].is_visited = True
    queue.append((x_start, y_start))

    while queue:
        front = queue[0]; changes_queue.append(('evaluating', front[0], front[1]))
        x_front = front[0]; y_front = front[1]
        dx, dy = di, dj
        cptype = Type
        while cptype:
            for k in range(4):
                x_succesor = x_front + dx[k]; y_succesor = y_front + dy[k]
                if matrix[x_succesor][y_succesor] == 0:
                    if info[x_succesor][y_succesor].is_visited is False:
                        info[x_succesor][y_succesor].x_p, info[x_succesor][y_succesor].y_p = front[0], front[1]
                        info[x_succesor][y_succesor].is_visited = True; changes_queue.append(('queued', x_succesor, y_succesor))
                        queue.append([x_succesor,y_succesor])
            dx, dy = dci, dcj
            cptype -= 1


        changes_queue.append(('visited', front[0], front[1]))
        queue.popleft()

    path_queue = Shared.redo_path(info, matrix, x_target, y_target)
    Shared.print_map(matrix)

    return changes_queue, path_queue

def init_parents(n, m):
    parent = np.ndarray((n + 2, m + 2), dtype = info)
    for i in range(0, n + 2):
        for j in range(0, m + 2):
            parent[i][j] = info(0, 0)
    return parent

def main():
    Input = open('input.in', 'r')

    matrix, n, m, x_start, y_start, x_target, y_target = Shared.read_input(Input)

    lee(matrix, x_start, y_start, x_target, y_target, 2)

if __name__ == '__main__':
    main()
