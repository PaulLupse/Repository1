from ..Utilities import DictUtilities

INF = 1000000000000

import numpy as np

def rest(banknotes_stock, Rest):
    class banknotes_used:
        def __init__(self):
            self.banknotes = {}

    nr_b_used = np.zeros((Rest + 1,), dtype = np.int64)
    b_used = np.ndarray((Rest + 1,), dtype = banknotes_used)

    for i in range(0, Rest + 1):
        b_used[i] = banknotes_used()

    for cost in range(1, Rest + 1):
        nr_b_used[cost] = INF
        for banknote, stock in banknotes_stock.items():
            if (stock > 0) and (banknote <= cost):
                try:
                    b_used[cost - banknote].banknotes[banknote]
                except:
                    b_used[cost - banknote].banknotes[banknote] = 0

                if (nr_b_used[cost] > nr_b_used[cost - banknote] + 1) and (banknotes_stock[banknote] - b_used[cost - banknote].banknotes[banknote] - 1 >= 0):
                    nr_b_used[cost] = nr_b_used[cost - banknote] + 1

                    b_used[cost].banknotes.clear()
                    b_used[cost].banknotes = DictUtilities.carbon_copy(b_used[cost - banknote].banknotes)
                    b_used[cost].banknotes[banknote] += 1

    if nr_b_used[Rest] == INF:
        return None, None
    else:
        for b, stock in b_used[Rest].banknotes.items():
            banknotes_stock[b] -= stock
        return nr_b_used[Rest], b_used[Rest].banknotes