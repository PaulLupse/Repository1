import numpy as np
from collections import deque as dq

def print_map(Map):
    import os
    os.system('cls')
    n = Map.shape[0]
    m = Map.shape[1]
    for i in range(0, n):
        for j in range(0, m):
            if Map[i][j] == 1:
                print('*', end = ' ')
            elif Map[i][j] == 2:
                print('@', end = ' ')
            else: print('.', end = ' ')
        print()

def border(Map, n, m):
    bordered_map = np.zeros((n + 2, m + 2), dtype = np.int64)
    for i in range(0, n + 2):
        bordered_map[i][0] = bordered_map[i][m + 1] = 1
    for j in range(0, m + 2):
        bordered_map[0][j] = bordered_map[n + 1][j] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            bordered_map[i][j] = Map[i - 1][j - 1]

    return bordered_map

def read_input(Input):
    n, m = [int(nr) for nr in Input.readline().split(' ')]
    Map = np.zeros((n, m), dtype = np.int64)
    for i in range(0, n):
        line = Input.readline()
        for j, nr in enumerate(line.split(' ')):
            Map[i][j] = int(nr)
    border(Map, n, m)

    x_source, y_source = [int(nr) for nr in Input.readline().split(' ')]
    x_target, y_target = [int(nr) for nr in Input.readline().split(' ')]

    return Map, n, m, x_source, y_source, x_target, y_target

def redo_path(info, Map, x_start, y_start):
    deque = dq()
    path = dq()
    deque.append((x_start, y_start))
    front = deque[-1]
    Info = info[front[0]][front[1]]

    while Info.x_p is not None:
        deque.append((Info.x_p, Info.y_p))
        front = deque[-1]
        Info = info[front[0]][front[1]]

    while deque:
        Map[deque[-1][0]][deque[-1][1]] = 2
        #print(deque[-1])
        path.append(deque[-1])
        deque.pop()

    return path