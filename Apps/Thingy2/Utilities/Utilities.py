import numpy as np

class Pair:
    def __init__(self, el1, el2):
        self.el1 = el1
        self.el2 = el2

class AdjancecyList:
    def __init__(self):
        ...

class Graph:
    def __init__(self, is_weighted, is_oriented):
        self.is_weighted = is_weighted
        self.is_oriented = is_oriented
        ...