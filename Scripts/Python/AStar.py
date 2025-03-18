import numpy as np
from queue import PriorityQueue as pq
from collections import deque as dq

Input = open('input.in', 'r')

def calc_h(x, y, x_target, y_target):
    return abs(x_target - x) + abs(y_target - y)

class Node(object):
    def __init__(self, f, g, h, x_p, y_p):
        self.f = f
        self.h = h
        self.g = g
        self.x_p = x_p
        self.y_p = y_p
        self.is_in_open_list = False
        self.is_in_closed_list = False

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

def isTarget(x_source, y_source, x_target, y_target):
    return x_source == x_target and y_source == y_target

def is_valid_to_push(Info, info):
    return not Info.is_in_open_list  and (not Info.is_in_closed_list or (Info.is_in_closed_list and (Info.f > info.f)))

def redo_path(info, Map, x_start, y_start):
    deque = dq()
    deque.append((x_start, y_start))
    front = deque[-1]
    Info = info[front[0]][front[1]]

    while Info.x_p is not None:
        deque.append((Info.x_p, Info.y_p))
        front = deque[-1]
        Info = info[front[0]][front[1]]

    while deque:
        Map[deque[-1][0]][deque[-1][1]] = 4
        print(deque[-1])
        deque.pop()


dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def search(Map, info, x_source, y_source, x_target, y_target):
    open_list = pq(10001)
    open_list.put(Cell(0, x_source, y_source))
    info[x_source][y_source].is_in_open_list = True
    info[x_source][y_source].x_p = None
    global gasit
    gasit = False

    while open_list.not_empty and not gasit:
        first_node = open_list.get()
        info[first_node.x][first_node.y].is_in_open_list = False

        for k in range(0, 4):
            x_succesor = first_node.x + dx[k]
            y_succesor = first_node.y + dy[k]

            if x_succesor == x_target and y_succesor == y_target:
                info[x_succesor][y_succesor].x_p = first_node.x
                info[x_succesor][y_succesor].y_p = first_node.y

                gasit = True
                break

            if Map[x_succesor][y_succesor] == 1:
                continue

            Info = info[x_succesor][y_succesor]
            g_succesor = info[first_node.x][first_node.y].g + 10
            h_succesor = calc_h(x_succesor, y_succesor, x_target, y_target) * 10
            f_succesor = g_succesor + h_succesor

            if Info.is_in_closed_list:
                continue

            if Info.is_in_open_list:
                if Info.f < f_succesor:
                    continue
            else:
                open_list.put(Cell(f_succesor, x_succesor, y_succesor))


            info[x_succesor][y_succesor].x_p = first_node.x
            info[x_succesor][y_succesor].y_p = first_node.y

            info[x_succesor][y_succesor].g = g_succesor
            info[x_succesor][y_succesor].h = h_succesor
            info[x_succesor][y_succesor].f = f_succesor

            info[x_succesor][y_succesor].is_in_open_list = True


        info[first_node.x][first_node.y].is_in_closed_list = True

    print("ENDED")

def border(Map, n, m):
    for i in range(0, n + 2):
        Map[i][0] = Map[i][m + 1] = 1
    for j in range(0, m + 2):
        Map[0][j] = Map[n + 1][j] = 1

if __name__ == '__main__':
    n, m = [int(nr) for nr in Input.readline().split(' ')]

    Map = np.zeros((n + 2, m + 2), dtype = np.int64)
    info = np.ndarray((n + 2, m + 2), dtype = Node)

    for i in range(0, n + 2):
        for j in range(0, m + 2):
            node = Node(0, 0, 0, 0, 0)
            info[i][j] = node

    for i in range(1, n + 1):
        line = Input.readline()
        for j, nr in enumerate(line.split(' ')):
            Map[i][j + 1] = int(nr)

    x_source, y_source = [int(nr) for nr in Input.readline().split(' ')]
    x_target, y_target = [int(nr) for nr in Input.readline().split(' ')]

    border(Map, n, m)
    print(Map)

    search(Map, info, x_source, y_source, x_target, y_target)
    redo_path(info, Map, x_target, y_target)

    print(Map)




