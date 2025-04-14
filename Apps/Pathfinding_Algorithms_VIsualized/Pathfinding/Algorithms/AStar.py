import numpy as np
from queue import PriorityQueue as pq
from collections import deque as dq
from math import sqrt
try:
    import Shared
except: from . import Shared

def calc_h_1(x, y, x_target, y_target): # manhattan distance
    X = abs(x_target - x)
    Y = abs(y_target - y)
    return X + Y

def calc_h_2(x, y, x_target, y_target):
    return sqrt((x_target - x)**2 + (y_target - y)**2)

class Node(object):
    def __init__(self, f, g, h, x_p, y_p):
        self.f = f
        self.h = h
        self.g = g
        self.x_p = x_p
        self.y_p = y_p
        self.is_queued = False
        self.is_visited = False

class Cell:
    def __init__(self, f, x, y):
        self.f = f
        self.x = x
        self.y = y
    def __lt__(self, obj):
        return self.f < obj.f
    def __le__(self, obj):
        return self.f <= obj.f
    def __eq__(self, obj):
        return self.f == obj.f
    def __ne__(self, obj):
        return self.f != obj.f
    def __gt__(self, obj):
        return self.f > obj.f
    def __ge__(self, obj):
        return self.f >= obj.f

def is_target(x_source, y_source, x_target, y_target):
    return x_source == x_target and y_source == y_target

def is_valid_to_push(Info, info):
    return not Info.is_queued  and (not Info.is_visited or (Info.is_visited and (Info.f > info.f)))

# when type == 1

#         |
#      -- @ --
#         |

dlx = (-1, 0, 1, 0)
dly = (0, 1, 0, -1)

# when type == 2

#       \   /
#         @
#       /   \

dcx = (-1, 1, 1, -1)
dcy = (1, 1, -1, -1)

def Asearch(Map, x_source, y_source, x_target, y_target, Type):
    changes_queue = dq()
    n = int(sqrt(Map.size))

    map = Utilities.border(Map, n, n)

    info = init_info(n, n)

    print(x_source, y_source)

    queue_list = pq(10001)
    queue_list.put(Cell(0, x_source, y_source))
    info[x_source][y_source].x_p = None
    global gasit
    gasit = False

    while queue_list.not_empty and not gasit:
        first_node = queue_list.get()

        changes_queue.append(('evaluating', first_node.x, first_node.y))

        dx = dlx
        dy = dly

        cp_type = Type

        while cp_type > 0:
            cp_type -= 1
            for k in range(0, 4):
                x_succesor = first_node.x + dx[k]
                y_succesor = first_node.y + dy[k]

                if is_target(x_succesor, y_succesor, x_target, y_target):
                    info[x_succesor][y_succesor].x_p = first_node.x
                    info[x_succesor][y_succesor].y_p = first_node.y

                    gasit = True
                    break

                if map[x_succesor][y_succesor] == 1:
                    continue

                Info = info[x_succesor][y_succesor]

                if Info.is_visited:
                    continue


                if cp_type == 0:
                    h_succesor = calc_h_1(x_succesor, y_succesor, x_target, y_target) * 10
                    g_succesor = info[first_node.x][first_node.y].g + 10
                else:
                    h_succesor = calc_h_1(x_succesor, y_succesor, x_target, y_target) * 10
                    g_succesor = info[first_node.x][first_node.y].g + 14


                f_succesor = g_succesor + h_succesor

                if Info.is_queued:
                    if Info.f <= f_succesor:
                        continue
                else:
                    queue_list.put(Cell(f_succesor, x_succesor, y_succesor))

                info[x_succesor][y_succesor].x_p = first_node.x
                info[x_succesor][y_succesor].y_p = first_node.y

                info[x_succesor][y_succesor].g = g_succesor
                info[x_succesor][y_succesor].h = h_succesor
                info[x_succesor][y_succesor].f = f_succesor

                info[x_succesor][y_succesor].is_queued = True; changes_queue.append(('queued', x_succesor, y_succesor))
            dx = dcx
            dy = dcy


        info[first_node.x][first_node.y].is_visited = True; changes_queue.append(('visited', first_node.x, first_node.y))


    path = Utilities.redo_path(info, map, x_target, y_target)
    Utilities.print_map(map)
    return changes_queue, path

def init_info(n, m):
    info = np.ndarray((n + 1, m + 1), dtype = Node)
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            info[i][j] = Node(0, 0, 0, 0, 0)
    return info

if __name__ == '__main__':
    Input = open('input.in', 'r')

    matrix, n, m, x_source, y_source, x_target, y_target = Utilities.read_input(Input)

    Asearch(matrix, x_source, y_source, x_target, y_target, 1)




