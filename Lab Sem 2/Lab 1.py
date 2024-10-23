#insertion sort

from pathlib import Path

pin = Path(__file__).with_name("Input.in")

fin = open(pin, "r")

n = fin.readline(); n = int(n) # lungimea sirului de sortat
v = [] # sirul de sortat

k = 0

for nr in fin.readline().split():
    nr = int(nr)
    i = k
    while(i > 0 and nr < v[i - 1]):
        i -= 1
    v.insert(i, nr)
    k += 1

print(v[:n:])