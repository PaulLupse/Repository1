import numpy as np

class bancnote:
    def __init__(self):
        self.lista_bancnote = []

def rest(stoc_bancnote, Rest):

    dp = np.zeros((Rest + 1,), dtype=np.int64)
    Bancnote = np.ndarray((Rest + 1,), dtype = bancnote)
    for i in range(0, Rest + 1):
        Bancnote[i] = bancnote()

    for cost in range(1, Rest + 1):
        dp[cost] = 10000000000
        for key, value in stoc_bancnote.items():
            if value and int(key) <= cost:
                if dp[cost] > dp[cost - int(key)] + 1:
                    dp[cost] = dp[cost - int(key)] + 1
                    Bancnote[cost].lista_bancnote.clear()
                    for b in Bancnote[cost - int(key)].lista_bancnote:
                        Bancnote[cost].lista_bancnote.append(b)
                    Bancnote[cost].lista_bancnote.append(int(key))
    #print(dp)

    if dp[Rest] == 10000000000:
        return -1
    else: return dp[Rest],  Bancnote[Rest].lista_bancnote

def main():
    stoc_bancnote = {'50':3,
                     '20':4,
                     '10':0,
                     '5':0,
                     '1':10}

    print(rest(stoc_bancnote, 160))


if __name__ == '__main__':
    main()