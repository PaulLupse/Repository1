import numpy as np
import random

# clasa ce implementeaza matricea jocului prin care este reprezentat jocul
# aceasta contine toata functionalitatea legata de cautarea, detectarea si eliminarea formelor, de interschimbari, si de
# alte actiuni specifice jocului Candy Crush, precum gravitatia bomboanelor si reumplerea matricei
class GameMatrix:

    def __init__(self, shape):

        self._shape = shape

        # matricea efectiva a jocului (un numpy.ndarray) este declarata cu 5 linii si coloane in plus datorita
        # mecanismului de detectie a formelor T, si datorita bordarii matricei
        # deoarece matricea este bordata, indexul efectiv al liniilor si coloanelor incepe de la 1 si se termina
        # la shape[0], respectiv shape[1], in mod inclusiv
        self._matrix = np.zeros((shape[0]+5, shape[1]+5), dtype = np.int8)
        # un tabel caracteristic (sau de flag-uri) ce retine daca o coloana are sau nu bomboane distruse
        # implicat in procesul de gravitatie
        self._destroyed = np.zeros(shape[1]+2, dtype=np.bool)

    # genereaza o matrice random
    def generate_matrix(self):

        matrix_shape = self._shape
        for i in range(1, matrix_shape[0]+1):
            for j in range(1, matrix_shape[1]+1):
                # este folosita exclusiv functia randrange pentru a asigura o distributie uniforma
                self._matrix[i][j] = random.randrange(1, 5)

    # type(matrix) = np.ndarray
    # copiaza matricea pasata ca argument in matricea jocului
    def set_matrix(self, matrix):

        for i in range(1, matrix.shape[0]+1):
            for j in range(1, matrix.shape[1]+1):
                self._matrix[i][j] = matrix[i-1][j-1]

    # realizeaza o interschimbare neoficiala intre doua elemente alea matricei
    def swap(self, x1, y1, x2, y2):
        self._matrix[x1][y1], self._matrix[x2][y2] = self._matrix[x2][y2], self._matrix[x1][y1]

    # cauta toate formele de tip linie de 5 DEJA FORMATE in matrice
    def search_pattern_5_line(self):

        matrix_shape = self._shape
        pct_cnt = 0

        # cautare pe orizontala

        # . . . . .
        # b b b b b
        # . . . . .

        # parcurgem, pe fiecare linie, fiecare coloana
        i = 1
        while i <= matrix_shape[0]:
            j = 1
            while j <= matrix_shape[1]-4:
                # daca elemntul i,j este 0, nu are rost sa mai verificam daca este format modelul
                if self._matrix[i][j] == 0:
                    j += 1
                    continue
                # daca este format modelul
                if self.check_5_line(i, j, 0):
                    # adunam punctele aferente
                    pct_cnt += 50
                    # distrugem bomboanele
                    self.destroy_line(i, j, 5, 0)
                    # sarim peste urmatoarele 4 elemente (deoarece au fost distruse)
                    j += 4
                j+=1
            i+=1

        # cautare pe verticala

        # . b .
        # . b .
        # . b .
        # . b .
        # . b .

        # parcurgem, pe fiecare coloana, fiecare linie
        # analog cu procesul de cautare pe orizontala
        j = 1
        while j <= matrix_shape[1]:
            i = 1
            while i <= matrix_shape[0] - 4:
                if self._matrix[i][j] == 0:
                    i += 1
                    continue
                if self.check_5_line(i, j, 1):
                    pct_cnt += 50
                    self.destroy_line(i, j, 5, 1)
                    i += 4
                i += 1
            j += 1

        return pct_cnt

    # cauta toate formele de tip linie de 4 DEJA FORMATE in matrice
    # similar cu procesul de cautare a modelelor de tip linie de 5
    def search_pattern_4_line(self):

        matrix_shape = self._shape
        pct_cnt = 0

        # cautare pe orizontala

        # . . . .
        # b b b b
        # . . . .

        i = 1
        while i <= matrix_shape[0]:
            j = 1
            while j <= matrix_shape[1] - 3:
                if self._matrix[i][j] == 0:
                    j += 1
                    continue
                if self.check_4_line(i, j, 0):
                    pct_cnt += 10
                    self.destroy_line(i, j, 4, 0)
                    j += 3
                j += 1
            i += 1

        # cautare pe verticala

        # . b .
        # . b .
        # . b .
        # . b .

        j = 1
        while j <= matrix_shape[0]:
            i = 1
            while i <= matrix_shape[1]-3:
                if self._matrix[i][j] == 0:
                    i += 1
                    continue
                if self.check_4_line(i, j, 1):
                    pct_cnt += 10
                    self.destroy_line(i, j, 4, 1)
                    i += 3
                i += 1
            j += 1


        return pct_cnt

    # cauta toate formele de tip linie de 3 DEJA FORMATE in matrice
    # similar cu procesul de cautare a modelelor de tip linie de 5
    def search_pattern_3_line(self):

        matrix_shape = self._shape
        pct_cnt = 0

        # cautare pe orizontala

        # . . .
        # b b b
        # . . .

        i = 1
        while i <= matrix_shape[0]:
            j = 1
            while j <= matrix_shape[1]-3:
                if self._matrix[i][j] == 0:
                    j += 1
                    continue
                if self.check_3_line(i, j, 0):
                    pct_cnt += 5
                    self.destroy_line(i, j, 3, 0)
                    j += 2
                j += 1
            i += 1

        # cautare pe orizontala

        # . b .
        # . b .
        # . b .

        j = 1
        while j <= matrix_shape[1]:
            i = 1
            while i <= matrix_shape[0]-3:
                if self._matrix[i][j] == 0:
                    i += 1
                    continue
                if self.check_3_line(i, j, 1):
                    pct_cnt += 5
                    self.destroy_line(i, j, 3, 1)
                    i += 2
                i += 1
            j += 1


        return pct_cnt

    # efectueaza o cautare a tuturor formelor L DEJA FORMATE in matrice
    def search_pattern_L(self):

        point_cnt = 0

        # pentru un element i,j, consideram elementele i,j+2, i+2,j+2, i+2,j
        # toate aceste 4 elemente reprezinta colturile unui patrat
        # totodata, reprezinta si punctul de intersectie al segmenteleor ce formeaza modele l

        # de exemplu, i,j reprezinta intersectia dintre segmentele ce reprezinta laturile de sus si de stanga ale
        # patratului
        # iar i+2,j+2 reprezinta intersectia dintre segmentele ce reprezinta laturile de jos si de dreapta ale
        # patratului

        # astfel, patratul este format din 4 modele L suprapuse, cu 'mijlocurile' in colturile patratului

        for i in range(1, self._shape[0] - 1):
            for j in range(1, self._shape[1] - 1):

                # verificam daca este format modelul de linie de 3 reprezentat de latura de sus
                if self.check_3_line(i, j, 0):
                    # verificam daca este format modelul de linie de 3 reprezentat de latura din stanga
                    if self.check_3_line(i, j, 1):
                        self.destroy_line(i, j, 3, 0)
                        self.destroy_line(i, j, 3, 1)
                        point_cnt += 20
                    # daca nu, verificam daca este format modelul de linie de 3 reprezentat de latura din dreapta
                    elif self.check_3_line(i, j+2, 1):
                        self.destroy_line(i, j, 3, 0)
                        self.destroy_line(i, j+2, 3, 1)
                        point_cnt += 20
                    else:
                        # daca nu sunt valide laturile de stanga si dreapta, atunci e imposibil ca patratul sa aiba un
                        # model de tip L cu mijlocul in unele din colturi. Deci, continuam la urmatorul element din
                        # matrice
                        continue

                # daca latura de sus nu este valida, o incercam pe cea de jos, folosind aceeasi metodologie
                elif self.check_3_line(i+2, j, 0):
                    if self.check_3_line(i, j, 1):
                        self.destroy_line(i+2, j, 3, 0)
                        self.destroy_line(i, j, 3, 1)
                        point_cnt += 20
                    elif self.check_3_line(i, j + 2, 1):
                        self.destroy_line(i+2, j, 3, 0)
                        self.destroy_line(i, j+2, 3, 1)
                        point_cnt += 20
                    else:
                        continue
                else:
                    continue

        return point_cnt

    # efectueaza o cautare a tuturor formelor T DEJA FORMATE in matrice
    def search_pattern_T(self):

        point_cnt = 0

        # la fel ca la cautarea formelor L, ne putem imagina cautarea formelor T ca fiind sub forma unui patrat care
        # se misca. Mijlocul patratului este determinat de i si j, iar laturile acestuia sunt segmentele de 5 patrate
        # formate de 2 dintre cele 3 brate ale formei T
        # consideram totodata mijlocul fiecarei laturi, dupa care ne vom orienta pentru verificarea existentei formei T

        for i in range(3, self._shape[0]-1):
            for j in range(3, self._shape[1]-1):

                mid_segment_i = (i-2, i, i+2, i)
                mid_segment_j = (j, j+2, j, j-2)

                dir = (1, 2, 3, 0)

                for k in range(0, 4):

                    mid_i, mid_j = mid_segment_i[k], mid_segment_j[k]
                    direction = dir[k]
                    if self.check_T(mid_i, mid_j, direction):
                        self.destroy_T(mid_i, mid_j, direction)
                        point_cnt += 30
                        # daca a fost gasit o forma T care are varful in i,j, nu se mai cauta altele
                        break

        return point_cnt

    # efectueaza o cautare cascada a formelor deja formate in matrice
    # se opreste doar atunci cand nu se mai gasesc alte forme formate
    def search_patterns(self, current_points, target = 10000):

        pcts = 0
        new_pcts = 1
        # cat timp exista noi forme deja formate
        while new_pcts != 0 and (current_points + pcts < target):
            # cautam toate formele deja formate
            pct1 = self.search_pattern_5_line()
            pct2 = self.search_pattern_L()
            pct3 = self.search_pattern_4_line()
            pct4 = self.search_pattern_3_line()
            # adunam toate punctele generate de cautari la totalul de puncte generate
            new_pcts = pct1 + pct2 + pct3 + pct4
            pcts += new_pcts
            if pcts != 0:
                self.gravitate()
                self.fill()

        # daca nu au fost gasita nici o forma deja formata, atunci doar gravitam bomboanele si reumplem matricea
        if pcts == 0:
            self.gravitate()
            self.fill()

        return pcts

    # prin interschimbare neoficiala se intelege o interschimbare care nu este numarata, dar ca de asemenea nu are efect
    # dorit asupra matricei de joc, si care se poate revoca

    # prin model potential se intelege un model creat in urma unei singure interschimbari neoficiale specifice,
    # caz in care interschimbarea devine oficiala si astfel o numaram

    # pentru fiecare tip de cautare se aplica urmatorul procedeu: se realizeaza o interschimbare specifica (neoficiala)
    # apoi se verifica daca s-au produs

    # cauta toate modelel potentiale de tip linie de 5
    def search_potential_pattern_5_line(self, current_points, target = 10000):

        swap_cnt = 0
        pct_cnt = 0

        # datorita faptului ca toate modelele de tip linie de 3 deja formate sunt eliminate din matrice
        # singurul caz in care se poate forma un model de tip linie de 5 este cand se interschimba mijlocul
        # segmentului, fie cu elementul de deasupra/stanga, fie cu elementul de desupt/dreapta

        shape = self._shape

        # asemenea detectiei modelelor deja formate, intai facem o parcurgere a elementelor asezate pe linii, apoi a
        # elementelor asezate pe coloane, pentru a evita verificarile inutile

        # cautare pe orizontala

        # . . b . .
        # b b . b b
        # . . b . .

        i = shape[0]
        while i >= 1 and (current_points + pct_cnt < target):
            j = 1
            while j <= shape[1] - 4:

                # realizam interschimbarea
                self.swap(i, j+2, i-1, j+2); swapped = True
                if not self.check_5_line(i,j,0):
                    # daca nu s-a format modelul, revocam interschimbarea
                    self.swap(i, j + 2, i - 1, j + 2); swapped = False

                # acelasi procedeu
                if not swapped:
                    self.swap(i, j + 2, i - 1, j + 2)
                    swapped = True
                    if not self.check_5_line(i, j, 0):
                        self.swap(i, j + 2, i - 1, j + 2)
                        swapped = False

                # daca a fost realizata o interschimbare neoficiala si nu a fost revocata, aceasta devine oficiala si
                # este numarata
                if swapped:

                    # distrugem cele 5 bomboane
                    self.destroy_line(i, j, 5, 0)

                    # adunam punctele aferente si efectuam cautarea cascada
                    pct_cnt += 50
                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)

                    swap_cnt += 1
                    return pct_cnt, swap_cnt

                j += 1
            i-= 1

        # cautare pe verticala

        # . b .
        # . b .
        # b . b
        # . b .
        # . b .

        # procedeu similar cu cel al cautarii pe orizontala
        j = 1
        while j <= shape[1] and (current_points + pct_cnt < target):

            i = shape[0] - 4
            while i >= 1:

                self.swap(i+2, j , i+2, j-1)
                swapped = True
                if not self.check_5_line(i, j, 1):
                    self.swap(i+2, j, i+2, j-1)
                    swapped = False

                if not swapped:
                    self.swap(i+2, j , i+2, j+1)
                    swapped = True
                    if not self.check_5_line(i, j, 1):
                        self.swap(i+2, j, i+2, j+1)
                        swapped = False

                if swapped:
                    self.destroy_line(i, j, 5, 1)
                    pct_cnt += 50
                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)


                    swap_cnt += 1

                    i -= 4

                    return pct_cnt, swap_cnt

                i -= 1

            j += 1

        return pct_cnt, swap_cnt

    # cauta toate modelel potentiale de tip linie de 4
    def search_potential_pattern_4_line(self, current_points, target = 10000):

        swap_cnt = 0
        pct_cnt = 0

        # datorita faptului ca toate modelele de tip linie de 3 deja formate sunt eliminate din matrice
        # singurele cazuri in care o interschimbare ar produce un model de tip linie de 4 sunt acele in care se
        # interschimba elementele din 'mijlocul' liniei, adica elementele 2 si 3, cu elementele vecine din afara liniei

        shape = self._shape

        # pe orizontala
        i = shape[0]
        while i >= 1 and (current_points + pct_cnt < target):
            j = 1
            while j <= shape[1]-3:

                # efectuam procedeul de interschimbare si verificare pentru elementele 2 si 3 ale segmentului
                # de la coordonatele i,j+1 respectiv i,j+2
                for k in (j+1,j+2):

                    self.swap(i,k,i-1,k); swapped = True
                    if not self.check_4_line(i,j,0):
                        # daca nu s-a format un model, revocam interschimbarea
                        self.swap(i, k, i - 1, k)
                        swapped = False

                    if not swapped:
                        self.swap(i,k,i+1,k);swapped = True
                        if not self.check_4_line(i,j,0):
                            self.swap(i,k,i+1,k)
                            swapped = False

                if swapped:
                    # daca s-a efectuat o interschimbare si nu a fost revocata, aceasta devine oficiala
                    # distrugem cele 4 bomboane
                    self.destroy_line(i, j, 4, 0)
                    # numaram interschimbarea
                    swap_cnt += 1
                    # adaugam punctele aferente
                    pct_cnt += 10
                    # efectuam cautarea cascada
                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)

                    return pct_cnt, swap_cnt

                j += 1
            i -= 1

        # cautare pe verticala
        # similar cu cautarea pe orizontala
        j = 1
        while j <= shape[1] and (current_points + pct_cnt < target):
            i = shape[0]-3
            while i >= 1:

                for k in (i+1,i+2):

                    self.swap(k,j,k,j-1);swapped = True
                    if not self.check_4_line(i,j,1):
                        self.swap(k,j,k,j-1)
                        swapped = False

                    if not swapped:
                        self.swap(k,j,k,j+1); swapped = True
                        if not self.check_4_line(i,j,1):
                            self.swap(k,j,k,j+1)
                            swapped = False

                if swapped:
                    self.destroy_line(i, j, 4, 1)
                    swap_cnt += 1
                    pct_cnt += 10
                    i += 3
                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)

                    return pct_cnt, swap_cnt

                i -= 1
            j += 1

        return pct_cnt, swap_cnt

    # cauta toate modelel potentiale de tip linie de 3
    def search_potential_pattern_3_line(self, current_points, target = 10000):

        pct_cnt = 0
        swap_cnt = 0

        # modelul de tip linie de 3 este cel mai mic dintre toate modelele
        # astfel, acesta poate fii format in urma interschimbarii oricarui element din segment cu oricare alt element
        # din afara segmentului

        shape = self._shape

        # cautare pe orizontala
        i = shape[0]
        while i >= 1 and (current_points + pct_cnt < target):
            j = 1
            while j <= shape[1]-2:
                swapped = False

                # realizam procedeul de interschimbare si verificare pentru fiecare dintre cele 3 elemente care compun
                # modelul
                # intial, interschimbam doar cu elementele laterale

                for k in range(0, 3):

                    self.swap(i, j+k, i-1, j+k); swapped = True
                    if not self.check_3_line(i, j, 0):
                        self.swap(i, j+k, i - 1, j+k)
                        swapped = False
                    else: break

                    self.swap(i, j+k, i + 1, j+k); swapped = True
                    if not self.check_3_line(i, j, 0):
                        self.swap(i, j+k, i + 1, j+k)
                        swapped = False
                    else: break

                # daca nu s-a gasti o interschimbare care sa produca un model valid, incercam interschimbarile capetelor
                # cu elementele in linie cu elementele segmentului
                if not swapped:

                    self.swap(i, j, i, j - 1);swapped = True
                    if not self.check_3_line(i, j, 0):
                        swapped = False
                        self.swap(i, j, i, j - 1)

                    if not swapped:
                        self.swap(i, j+2, i, j + 3)
                        swapped = True
                        if not self.check_3_line(i, j, 0):
                            swapped = False
                            self.swap(i, j+2, i, j + 3)

                if swapped:
                    # daca a fost efectuata o interschimbare si nu a fost revocata, o consideram oficiala si o numaram

                    # distrugem cele 3 bomboane
                    self.destroy_line(i, j, 3, 0)

                    # adunam punctele aferente
                    pct_cnt += 5
                    swap_cnt += 1

                    # efectuam cautarea cascada
                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)

                    return pct_cnt, swap_cnt

                j += 1
            i-= 1

        j = 1
        while j <= self._shape[1] and (current_points + pct_cnt < target):

            i = shape[0] - 2
            while i >= 1:
                swapped = False
                for k in range(0, 4):

                    self.swap(i + k, j, i + k, j - 1)
                    swapped = True
                    if not self.check_3_line(i,j, 1):
                        self.swap(i + k, j, i + k, j - 1)
                        swapped = False
                    else: break

                    if not swapped:
                        self.swap(i + k, j, i + k, j + 1)
                        swapped = True
                        if not self.check_3_line(i, j, 1):
                            self.swap(i + k, j, i + k, j + 1)
                            swapped = False
                        else: break

                if not swapped:


                    self.swap(i, j, i-1, j)
                    swapped = True
                    if not self.check_3_line(i, j, 1):
                        swapped = False
                        self.swap(i, j, i-1, j)

                    if not swapped:
                        self.swap(i+2, j, i+3, j)
                        swapped = True
                        if not self.check_3_line(i, j, 1):
                            swapped = False
                            self.swap(i+2, j, i+3, j)

                if swapped:

                    #print(i, ' ', j, ' ', i+2, ' ', j)
                    self.destroy_line(i, j, 3, 1)

                    pct_cnt += 5
                    swap_cnt += 1

                    pct_cnt += self.search_patterns(current_points + pct_cnt, target)

                    i -= 2

                    return pct_cnt, swap_cnt

                i -= 1
            j += 1

        return pct_cnt, swap_cnt

    # efectueaza o cautare a formelor potentiale L
    def search_potential_pattern_L(self, current_points, target):

        points_cnt = 0
        swap_cnt = 0

        i = self._shape[0] - 2
        while i >= 1 and current_points + points_cnt < target:
            for j in range(1, self._shape[1]-1):

                # cautarea se bazeaza pe un patrat de marime 3x3
                # interschimbam fiecare colt al acestuia cu vecinii ce nu se afla in patrat, pana ce gasim o
                # interschimbare ce produce un model L

                # tuplii ce memoreaza valorile absciselor, respectiv ordonatelor ale colturilor patratului de cautare
                corner_i = (i, i, i+2, i + 2)
                corner_j = (j, j+2, j+2, j)

                # tuplii ce memoreaza indecsii vecinilor colturilor, care se schimba de indecsii colturilor
                # de ex, daca coltul 2,2 trb sa fie interschimbat cu 2,1, atunci memoram doar acel '1' al indexului j

                swap_i = (i-1, i-1, i+3, i+3)
                swap_j = (j-1, j+3, j+3, j-1)

                # tuplii ce memoreaza orientarea 'bratelor' L-ului
                vert_dir = (1, 1, 3, 3)
                hor_dir = (0, 2, 2, 0)

                swapped = False

                # parcurgem fiecare dintre cele 4 colturi
                for k in range(0, 4):

                    # retinem variabilele necesare
                    c_i, c_j = corner_i[k], corner_j[k]
                    s_i, s_j = swap_i[k], swap_j[k]
                    v_dir, h_dir = vert_dir[k], hor_dir[k]


                    # initial facem o interschimbare cu coltul pe orizontala
                    swapped = True
                    self.swap(c_i, c_j, c_i, s_j)
                    # daca s-a format un L, atunci destrugem bomboanele
                    if self.check_3_line(c_i, c_j, h_dir) and self.check_3_line(c_i, c_j, v_dir):
                        self.destroy_line(c_i, c_j, 3, h_dir)
                        self.destroy_line(c_i, c_j, 3, v_dir)
                        break
                    else:
                        self.swap(c_i, c_j, c_i, s_j)
                        swapped = False

                    # apoi pe verticala
                    if not swapped:
                        self.swap(c_i, c_j, s_i, c_j)
                        swapped = True
                        if self.check_3_line(c_i, c_j, h_dir) and self.check_3_line(c_i, c_j, v_dir):
                            self.destroy_line(c_i, c_j, 3, h_dir)
                            self.destroy_line(c_i, c_j, 3, v_dir)
                            break
                        else:
                            self.swap(c_i, c_j, s_i, c_j)
                            swapped = False

                # daca s-a efectuat o interschimbare, adaugam punctele aferente modelului si crestem contorul de interschimbari
                # apoi efectuam cautarea cascada a formelor
                if swapped:
                    points_cnt += 20
                    swap_cnt += 1
                    points_cnt += self.search_patterns(points_cnt + current_points, target)

                    return points_cnt, swap_cnt

            i -= 1

        return points_cnt, swap_cnt

    # efectueaza o cautare a formelor potentiale T
    def search_potential_pattern_T(self, current_points, target):

        points_cnt = 0
        swap_cnt = 0

        # formele T sufera de aceeasi restrictionare ca si formele linie de 5, din aceleasi motive,
        # la care se adauga faptul ca doar intr-o parte se poate efectua interschimbarea cu 'mijlocul' (datorita
        # existentei bratului perpendicular)

        # deci, verificam daca interschimbarea mijlocului (punctul de intersectie intre cele 3 segmente de lungime 3)
        # cu elementul de pe partea opusa cu bratul perpendicular, determina formarea modelului T

        # folosim totodata un rationament ca si la cautarea modelelor L potentiale, un patrat de latura 5, a carui
        # laturi sunt formate din segmentele 'lungi' ale 4 forme T, astfel incat varfurile segmenteleor perpendiculare
        # sa aiba punct comun in mijlocul patratului

        # a a a a a
        # b . a . b
        # b b a b b
        # b . b . b
        # b b b b b

        i = 3
        while i <= self._shape[0] and current_points + points_cnt < target:
            for j in range(3, self._shape[1]):

                # tuplii ce memoreaza coordonatele mijlocurilor celor patru T-uri
                mid_segment_i = (i - 2, i, i + 2, i)
                mid_segment_j = (j, j + 2, j, j - 2)

                # tuplii ce memoreaza coordonatele elementelor ce se pot interschimba cu mijlocurile celor 4 T-uri
                swap_i = (i-3, i, i+3, i)
                swap_j = (j, j+3, j, j-3)

                # directiile bratelor perpendiculare pentru fiecare model T (utilizare la operatiile de verificare si
                # eliminare)

                # 0 = dreapta
                # 1 = jos
                # 2 = stanga
                # 3 = sus

                dir = (1, 2, 3, 0)

                # aplicam rationamentul descris mai sus pentru fiecare dintre cele 4 T-uri
                swapped = False
                for k in range(0, 4):

                    mid_i = mid_segment_i[k]
                    mid_j = mid_segment_j[k]

                    s_i = swap_i[k]
                    s_j = swap_j[k]

                    direction = dir[k]

                    # realizam interschimbare intre mijlocul T-ului si elementul cu care il putem interschimba
                    self.swap(mid_i, mid_j, s_i, s_j)
                    swapped = True
                    if self.check_T(mid_i, mid_j, direction):
                        # daca s-a format modelul T, distrugem bomboanele care formeaza modelul si iesim din bucla
                        # celor 4 T-uri
                        self.destroy_T(mid_i, mid_j, direction)
                        break
                    else:
                        # altfel revocam interschimbarea
                        self.swap(mid_i, mid_j, s_i, s_j)
                        swapped = False

                if swapped:
                    # daca a fost efectuata o interschimbare si nu a fost revocata, atunci devine oficiala si o luam
                    # in considerare
                    points_cnt += 30
                    swap_cnt += 1
                    points_cnt += self.search_patterns(current_points, target)

            i += 1

        return points_cnt, swap_cnt

    # distruge o linie de lungime [length] in directia [dir]
    def destroy_line(self, i, j, length, dir):

        # ->
        if dir == 0:
            for k in range(0, length):
                self._matrix[i][j+k] = 0
                self._destroyed[j+k] = 1
            return

        # |
        # V
        elif dir == 1:
            for k in range(0, length):
                self._matrix[i+k][j] = 0
            self._destroyed[j] = 1

        # <-
        elif dir == 2:
            for k in range(0, length):
                self._matrix[i][j-k] = 0
                self._destroyed[j-k] = 1

        # ^
        # |
        else:
            for k in range(0, length):
                self._matrix[i-k][j] = 0
            self._destroyed[j] = 1

    # verifica daca segmentul de 3 elemente incepand cu elementul de pe pozitia x,y si continuand in directia dir
    # formeaza un model de tip linie de 3
    def check_3_line(self, x, y, dir):

        if dir == 0:
            return self._matrix[x][y] == self._matrix[x][y+1] == self._matrix[x][y+2]
        elif dir == 1:
            return self._matrix[x][y] == self._matrix[x+1][y] == self._matrix[x+2][y]
        elif dir == 2:
            return self._matrix[x][y] == self._matrix[x][y - 1] == self._matrix[x][y - 2]
        return self._matrix[x][y] == self._matrix[x-1][y] == self._matrix[x-2][y]

    # verifica daca segmentul de 4 elemente incepand cu elementul de pe pozitia x,y si continuand in directia dir
    # formeaza un model de tip linie de 4
    def check_4_line(self, x, y, dir):

        if dir == 0:
            return self._matrix[x][y] == self._matrix[x][y+1] == self._matrix[x][y+2] == self._matrix[x][y+3]
        elif dir == 1:
            return self._matrix[x][y] == self._matrix[x+1][y] == self._matrix[x+2][y] == self._matrix[x+3][y]
        elif dir == 2:
            return self._matrix[x][y] == self._matrix[x][y - 1] == self._matrix[x][y - 2] == self._matrix[x][y-3]
        return self._matrix[x][y] == self._matrix[x-1][y] == self._matrix[x-2][y] == self._matrix[x+3][y]

    # verifica daca segmentul de 5 elemente incepand cu elementul de pe pozitia x,y si continuand in directia dir
    # formeaza un model de tip linie de 5
    def check_5_line(self, x, y, dir):

        if dir == 0:
            return self._matrix[x][y] == self._matrix[x][y+1] == self._matrix[x][y+2] == self._matrix[x][y+3] == self._matrix[x][y + 4]
        elif dir == 1:
            return self._matrix[x][y] == self._matrix[x+1][y] == self._matrix[x+2][y] == self._matrix[x+3][y] == self._matrix[x+4][y]
        elif dir == 2:
            return self._matrix[x][y] == self._matrix[x][y - 1] == self._matrix[x][y - 2] == self._matrix[x][y-3] == self._matrix[x][y - 4]
        return self._matrix[x][y] == self._matrix[x-1][y] == self._matrix[x-2][y] == self._matrix[x+3][y] == self._matrix[x-4][y]

    # verifica daca elementele asezate sub forma modelului T avand mijlocul in x,y formeaza un model T complet, in
    # directia specificata
    # x-ul si y-ul reprezinta coordonatele punctului de intersectie a celor 3 brate
    def check_T(self, x, y, dir):

        if dir == 0:
            return self.check_3_line(x, y, 0) and self.check_5_line(x-2, y, 1)
        elif dir == 1:
            return self.check_3_line(x, y, 1) and self.check_5_line(x, y-2, 0)
        elif dir == 2:
            return self.check_3_line(x, y, 2) and self.check_5_line(x-2, y, 1)
        else: return self.check_3_line(x, y, 3) and self.check_5_line(x, y-2, 0)

    # distruge elementele asezate sub forma modelului T avand mijlocul in x,y in directia specificata
    def destroy_T(self, x, y, dir):
        if dir == 0:
            self.destroy_line(x, y, 3, 0)
            self.destroy_line(x-2, y, 5, 1)
        elif dir == 1:
            self.destroy_line(x, y, 3, 1)
            self.destroy_line(x, y-2, 5, 0)
        elif dir == 2:
            self.destroy_line(x, y, 3, 2)
            self.destroy_line(x-2, y, 5, 1)
        else:
            self.destroy_line(x, y, 3, 3)
            self.destroy_line(x, y - 2, 5, 0)

    # graviteaza toate bomboanele in jos, ocupand spatiile libere, marcate cu 0
    def gravitate(self):

        # selecteaza toate coloanele care au bomboane distruse, folosindu-se de self._destroyed
        columns = []
        for i in range(1, self._shape[1]+1):
            if self._destroyed[i]:
                columns.append(i)
                self._destroyed[i] = 0

        # merge pe la fiecare coloana
        for col in columns:

            # cauta pozitia pe care se afla primul loc liber si o memoreaza
            last_zero_pos = self._shape[0]
            while last_zero_pos > 0 and (self._matrix[last_zero_pos][col] != 0):
                last_zero_pos -= 1

            # pana cand nu mai sunt bomboane de gravitat, aseaza ultima bomboana gasita pe prima prima pozitie libera
            # din coloana
            for line in range(last_zero_pos, 0, -1):
                if self._matrix[line][col] != 0:

                    self._matrix[last_zero_pos][col] = self._matrix[line][col]
                    self._matrix[line][col] = 0

                    last_zero_pos -= 1

    # reumple matricea cu bomboane
    def fill(self):

        for col in range(1, self._shape[1]+1):

            line = 1
            while self._matrix[line][col] == 0 and line <= self._shape[0]:
                # se foloseste randrange pentru asigurarea unei distributii uniforme a bomboanelor
                self._matrix[line][col] = random.randrange(1, 5)
                line += 1

    # afiseaza matricea de joc
    def print(self):
        for col in range(0, self._shape[1]*2):
            print("=", end='')
        print()
        print('',end='')
        for line in range(1, self._shape[0]+1):
            print('', end='')
            for col in range(1, self._shape[1]+1):
                if self._matrix[line][col] == 0:
                    print(self._matrix[line][col], end=' ')
                else:
                    print(self._matrix[line][col], end=' ')
            print('')
        print('')
        for col in range(0, self._shape[1]*2):
            print("=", end='')
        print()

if __name__ == "__main__":
    a = GameMatrix((9,9))
    a.set_matrix(np.array([[1, 2, 1, 2, 1, 2, 1, 2, 1],
                           [2, 1, 2, 1, 2, 1, 2, 1, 2],
                           [1, 2, 1, 2, 1, 2, 1, 2, 1],
                           [2, 1, 2, 1, 2, 1, 2, 1, 2],
                           [4, 4, 1, 2, 1, 2, 1, 3, 1],
                           [2, 1, 4, 1, 2, 1, 2, 3, 2],
                           [4, 4, 2, 4, 4, 3, 3, 2, 1],
                           [2, 1, 4, 1, 2, 1, 2, 3, 2],
                           [1, 2, 4, 2, 1, 2, 1, 3, 1]]))
