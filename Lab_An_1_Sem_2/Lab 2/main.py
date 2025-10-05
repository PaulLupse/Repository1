
import hashlib
import multiprocessing as multi
from multiprocessing.sharedctypes import Value
import numpy as np


def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verifica(candidat, parola, ):
    if get_hash(''.join(candidat)) == parola:
        print(f'Parolă Găsită: {''.join(candidat)}')
        return True
    else: return False

majuscule = np.array([maj for maj in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'], dtype = str)
minuscule = np.array([maj for maj in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()], dtype = str)
speciale = ('!', '@', '#', '$')

gasit = Value('i', 0)
cnt_apeluri = Value('i', 0)

def backy(k, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri ):
    if gasit.value == 1:
        exit()
    if k == 6:
        if verifica(candidat, parola, ):
            gasit.value = 1
            print(f'Număr apeluri recursive:{cnt_apeluri.value}')
            exit()
    else:
        if cnt_min < 3:
            for Min in minuscule:
                candidat.append(Min)
                backy(k + 1, parola, folosit_nr, cnt_min + 1, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop(); cnt_apeluri.value += 1

        if folosit_nr is False:
            for i in range(0, 10):
                candidat.append(str(i))
                backy(k + 1, parola, True, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop(); cnt_apeluri.value += 1

        if folosit_maj is False:
            for maj in majuscule:
                candidat.append(maj)
                backy(k + 1, parola, folosit_nr, cnt_min, True, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop(); cnt_apeluri.value += 1

        if folosit_spec is False:
            for spec in speciale:
                candidat.append(spec)
                backy(k + 1, parola, folosit_nr, cnt_min, folosit_maj, True, candidat, gasit, cnt_apeluri )
                candidat.pop(); cnt_apeluri.value += 1

def proces(k, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri ):
    cp_k = k
    cp_parola = parola
    cp_folosit_nr = folosit_nr
    cp_cnt_min = cnt_min
    cp_folosit_maj = folosit_maj
    cp_folosit_spec = folosit_spec
    cp_candidat = candidat
    multi.Process(target=backy, args=(
        cp_k, cp_parola, cp_folosit_nr, cp_cnt_min, cp_folosit_maj, cp_folosit_spec, cp_candidat, gasit, cnt_apeluri)).start()

def main():
    global gasit

    # '0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad'

    if __name__ == '__main__':
        k = 0; parola = '0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad'

        candidat = []
        folosit_maj = False
        folosit_nr = False
        folosit_spec = False
        cnt_min = 0

        folosit_nr = True
        for i in range(0, 10):
            candidat.append(str(i))
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_nr = False


        folosit_maj = True
        for maj in majuscule:
            candidat.append(maj)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_maj = False

        cnt_min += 1
        for Min in minuscule:
            candidat.append(Min)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        cnt_min -= 1

        folosit_spec = True
        for spec in speciale:
            candidat.append(spec)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_spec = False

main()