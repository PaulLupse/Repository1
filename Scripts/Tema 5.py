pasi = 0

def cautare_binara(arr, start, stop, val):
    global pasi
    pivot = (start + stop)//2
    if start <= stop:
        pasi += 1
        if arr[pivot] == val:
            return pivot
        elif val < arr[pivot]:
            return cautare_binara(arr, start, pivot - 1, val)
        else: return cautare_binara(arr, pivot + 1, stop, val)
    return -1


def cauta_pacient(pacienti, id_pacient):
    global pasi

    n = len(pacienti)
    i = 1
    st = 0
    pasi = 0
    while i <= n and pacienti[i] < id_pacient:
        pasi += 1
        st = i
        i *= 2

    index = 0
    if not(st == 0 and pacienti[st] == id_pacient):
        index = cautare_binara(pacienti, st, min(st * 2, n - 1), id_pacient)

    if index != -1:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția {index} după {pasi} pași de căutare.")
    else: print(f"Dosarul pacientului cu numărul de identificare {id_pacient} nu a fost găsit. Total pași efectuați: {pasi}.")


cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1100)
cauta_pacient([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1000)
cauta_pacient(range(1, 1000000, 7), 7778)
cauta_pacient(range(1, 1000000, 7), 1234567)
