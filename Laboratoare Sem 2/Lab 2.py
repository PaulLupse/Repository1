# Merge Sort

from pathlib import Path

fin = open(Path(__file__).with_name("Input.in"))

n = fin.readline(); n = int(n)
v = [int(i) for i in fin.readline().split()]

