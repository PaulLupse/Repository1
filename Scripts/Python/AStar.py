Input = open('input.in', 'r')

class node():
    def __init__(self, ):

n = 0; m = 0
Map = []

def search(Map):
    ...

if __name__ == '__main__':
    global Map

    n, m = [int(nr) for nr in Input.readline().split(' ')]

    for i in range(0, n):
        Map.append([])
        line = Input.readline()
        for nr in line.split(' '):
                Map.append(int(nr))



