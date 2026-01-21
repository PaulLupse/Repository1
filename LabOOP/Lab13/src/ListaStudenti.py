from src.Student import Student, StudentCNP
from typing import Union
from src.CititorFisierCsv import CititorFisierCsv

class ListaStudenti:

    class _Nod:

        def __init__(self, student:Union[Student, StudentCNP]):

            self._student:Union[Student, StudentCNP] = student
            self.prev_nod:ListaStudenti._Nod|None = None
            self.next_nod:ListaStudenti._Nod|None = None

    def __init__(self, **optiuni):

        self._nr_noduri:int = 0
        self._baza:ListaStudenti._Nod|None = None
        self._varf:ListaStudenti._Nod|None = None

        # daca in optiuni este specifiat numele unui fisier, atunci vom incerca citirea din acel fisier
        nume_fisier:str = optiuni.get("nume_fisier")
        if nume_fisier:
            lista_studenti:list[Student|StudentCNP] = CititorFisierCsv(nume_fisier).citeste()

            for student in lista_studenti:
                self.adauga_varf(student)

    def adauga_varf(self, student:Union[Student, StudentCNP]):

        nod_nou = ListaStudenti._Nod(student)

        if self._nr_noduri == 0:
            self._varf = self._baza = nod_nou

        elif self._nr_noduri == 1:
            self._varf = nod_nou
            self._baza.next_nod = self._varf
            self._varf._prev_nod = self._baza

        else:
            self._varf.next_nod = nod_nou
            nod_nou.prev_nod = self._varf
            self._varf = nod_nou

        self._nr_noduri += 1

    def adauga_baza(self, student:Union[Student, StudentCNP]):

        nod_nou:ListaStudenti._Nod = ListaStudenti._Nod(student)

        if self._nr_noduri == 0:
            self._varf = self._baza = nod_nou

        elif self._nr_noduri == 1:
            self._baza = nod_nou
            self._baza.next_nod = self._varf
            self._varf._prev_nod = self._baza

        else:
            self._baza.prev_nod = nod_nou
            nod_nou.next_nod = self._baza
            self._baza = nod_nou

        self._nr_noduri += 1

    def elimina_varf(self):

        self._varf = self._varf.prev_nod
        self._varf.next_nod = None

        self._nr_noduri -= 1

    def elimina_baza(self):

        self._baza = self._baza.next_nod
        self._baza.prev_nod = None

        self._nr_noduri -= 1


    def afiseaza(self):

        print(f"Total studenți: {self._nr_noduri}.\n")
        iterator:ListaStudenti._Nod = self._baza

        if self._nr_noduri:

            while iterator != self._varf:
                iterator._student.afiseaza()
                iterator = iterator.next_nod

            iterator._student.afiseaza()

            print()






