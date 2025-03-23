import numpy as np
from queue import PriorityQueue as pq
from collections import deque as dq

Input = open('input.in', 'r')

def calc_h_1(x, y, x_target, y_target): # manhattan distance
    return abs(x_target - x) + abs(y_target - y)

def calc_h_2(x, y, x_target, y_target):
    return max(abs(x_target - x), abs(y_target - y))

class Node(object):
    def __init__(self, f, g, h, x_p, y_p):
        self.f = f
        self.h = h
        self.g = g
        self.x_p = x_p
        self.y_p = y_p
        self.is_in_queue_list = False
        self.is_in_visited_list = False

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
    return not Info.is_in_queue_list  and (not Info.is_in_visited_list or (Info.is_in_visited_list and (Info.f > info.f)))

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
        Map[deque[-1][0]][deque[-1][1]] = 2
        print(deque[-1])
        deque.pop()

def print_map(Map, n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if Map[i][j] == 1:
                print('*', end = ' ')
            elif Map[i][j] == 2:
                print('@', end = ' ')
            else: print('.', end = ' ')
        print()

#         |
#      -- @ --
#         |

dlx = (-1, 0, 1, 0)
dly = (0, 1, 0, -1)

#       \   /
#         @
#       /   \

dcx = (-1, 1, 1, -1)
dcy = (1, 1, -1, -1)

def search(Map, info, x_source, y_source, x_target, y_target, type):
    queue_list = pq(10001)
    queue_list.put(Cell(0, x_source, y_source))
    info[x_source][y_source].is_in_queue_list = True
    info[x_source][y_source].x_p = None
    global gasit
    gasit = False

    while queue_list.not_empty and not gasit:
        first_node = queue_list.get()
        info[first_node.x][first_node.y].is_in_queue_list = False

        dx = dlx
        dy = dly

        cp_type = type

        while cp_type > 0:
            cp_type -= 1
            print(cp_type)
            print(dx)
            print(dy)
            for k in range(0, 4):
                x_succesor = first_node.x + dx[k]
                y_succesor = first_node.y + dy[k]

                if is_target(x_succesor, y_succesor, x_target, y_target):
                    info[x_succesor][y_succesor].x_p = first_node.x
                    info[x_succesor][y_succesor].y_p = first_node.y

                    gasit = True
                    break

                if Map[x_succesor][y_succesor] == 1:
                    continue

                Info = info[x_succesor][y_succesor]

                if Info.is_in_visited_list:
                    continue


                if cp_type == 0:
                    h_succesor = calc_h_1(x_succesor, y_succesor, x_target, y_target) * 10
                    g_succesor = info[first_node.x][first_node.y].g + 10
                else:
                    h_succesor = calc_h_2(x_succesor, y_succesor, x_target, y_target) * 10
                    g_succesor = info[first_node.x][first_node.y].g + 14


                f_succesor = g_succesor + h_succesor

                if Info.is_in_queue_list:
                    if Info.f < f_succesor:
                        continue
                else:
                    queue_list.put(Cell(f_succesor, x_succesor, y_succesor))

                info[x_succesor][y_succesor].x_p = first_node.x
                info[x_succesor][y_succesor].y_p = first_node.y

                info[x_succesor][y_succesor].g = g_succesor
                info[x_succesor][y_succesor].h = h_succesor
                info[x_succesor][y_succesor].f = f_succesor

                info[x_succesor][y_succesor].is_in_queue_list = True
            dx = dcx
            dy = dcy


        info[first_node.x][first_node.y].is_in_visited_list = True

    print("ENDED")

def border(Map, n, m):
    for i in range(0, n + 2):
        Map[i][0] = Map[i][m + 1] = 1
    for j in range(0, m + 2):
        Map[0][j] = Map[n + 1][j] = 1

def init_info():
    info = np.ndarray((n + 2, m + 2), dtype = Node)
    for i in range(0, n + 2):
        for j in range(0, m + 2):
            node = Node(0, 0, 0, 0, 0)
            info[i][j] = node
    return info

def read_input():
    n, m = [int(nr) for nr in Input.readline().split(' ')]
    Map = np.zeros((n + 2, m + 2), dtype = np.int64)
    for i in range(1, n + 1):
        line = Input.readline()
        for j, nr in enumerate(line.split(' ')):
            Map[i][j + 1] = int(nr)
    border(Map, n, m)

    x_source, y_source = [int(nr) for nr in Input.readline().split(' ')]
    x_target, y_target = [int(nr) for nr in Input.readline().split(' ')]

    return Map, n, m, x_source, y_source, x_target, y_target

if __name__ == '__main__':
    info = init_info()

    Map, n, m, x_source, y_source, x_target, y_target = read_input()

    print(Map)

    search(Map, info, x_source, y_source, x_target, y_target, 2)
    redo_path(info, Map, x_target, y_target)
    print_map(Map, n, m)




