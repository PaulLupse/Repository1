import hashlib
import multiprocessing as multi
from multiprocessing.sharedctypes import Value
import numpy as np
import Hashing

def get_hash(password):
    return Hashing.sha_256(password)

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
    if gasit.value == 1: # daca alte procese au gasit un cadidat valid
        exit() # se opreste procesul

    if k == 6: # daca am ajuns la al 6-lea caracter din candidat, verificam daca este parola
        if verifica(candidat, parola, ):
            gasit.value = 1
            print(f'Număr apeluri recursive:{cnt_apeluri.value}')
            exit()
    else:
        if cnt_min < 3: # daca sunt mai putin de 3 minuscule in candidat, adaugam un caracter minuscul
            for Min in minuscule: # incercam toate minusculele
                candidat.append(Min); cnt_apeluri.value += 1
                backy(k + 1, parola, folosit_nr, cnt_min + 1, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop()

        if folosit_nr is False:  # daca nu este folosita o cifra, adaugam o cifra
            for i in range(0, 10): # incercam toate cele 10 cifre
                candidat.append(str(i)); cnt_apeluri.value += 1
                backy(k + 1, parola, True, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop()

        if folosit_maj is False: # daca nu este folosita o majuscula, adaugam o majuscula
            for maj in majuscule: # incercam toate majusculele
                candidat.append(maj); cnt_apeluri.value += 1
                backy(k + 1, parola, folosit_nr, cnt_min, True, folosit_spec, candidat, gasit, cnt_apeluri )
                candidat.pop()

        if folosit_spec is False: # daca nu este folosit un caracter special, adaugam un caracter special
            for spec in speciale: # incercam toate caracterele speciale
                candidat.append(spec); cnt_apeluri.value += 1
                backy(k + 1, parola, folosit_nr, cnt_min, folosit_maj, True, candidat, gasit, cnt_apeluri )
                candidat.pop()

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
        parola = get_hash('0aaaA!') # obtinem hash-ul pt parola

        # initial...
        candidat = [] # ...candidatul este nul
        folosit_maj = False # ...nu sunt folosite majuscule
        folosit_nr = False # ...nu sunt folosite numere
        folosit_spec = False # ...nu sunt folosite caractere speciale
        cnt_min = 0 # ...nu sunt folosite minuscule

        # pornim un proces care incearca candidatii ce incep cu o cifra
        folosit_nr = True
        for i in range(0, 10):
            candidat.append(str(i))
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_nr = False

        # pornim un proces care incearca candidatii care incep cu majuscule
        folosit_maj = True
        for maj in majuscule:
            candidat.append(maj)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_maj = False

        # pornim un proces care incearca candidatii care incep cu minuscule
        cnt_min += 1
        for Min in minuscule:
            candidat.append(Min)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        cnt_min -= 1

        # pornim un proces care incearca candidatii care incepd cu caractere speciale
        folosit_spec = True
        for spec in speciale:
            candidat.append(spec)
            proces(k + 1, parola, folosit_nr, cnt_min, folosit_maj, folosit_spec, candidat, gasit, cnt_apeluri )
            candidat.pop()
        folosit_spec = False

if __name__ == '__main__':
    main()
