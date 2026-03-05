from __future__ import annotations
from dataclasses import dataclass
from student import StudentCNP


@dataclass
class Nod:
    student: StudentCNP
    urmator: Nod | None = None

    # adaugă automat un constructor Nod(_text, _urmator)

    def __str__(self):
        return str(self.student)


def comparator_medie(s1:StudentCNP, s2:StudentCNP) -> bool:
    return s1.medie > s2.medie

class Stiva:

    def __init__(self, fisier: str):
        self.varf = None
        self.n = 0
        with open(fisier, "r", encoding="utf-8") as f:
            for linie in f:
                linie = linie.strip()
                if not linie:
                    continue
                parts = [p.strip() for p in linie.split(",")]

                if len(parts) != 6:
                    raise ValueError(f"Linie CSV invalidă: {linie}")

                nume, prenume, spec, an, medie, cnp = parts
                st = StudentCNP(
                    nume_prenume=f"{nume} {prenume}",
                    specializare=spec,
                    an_studiu=int(an),
                    medie=float(medie),
                    cnp=cnp
                )
                self.adauga(st)

    def adauga(self, student: StudentCNP) -> None:
        self.varf = Nod(student, self.varf)
        self.n += 1

    def afiseaza(self):
        print()
        a = self.varf
        while a:
            print(str(a))
            a = a.urmator

    def __getitem__(self, i: int) -> StudentCNP:
        return self.sari_peste(i).student

    def __setitem__(self, i: int, student: StudentCNP) -> None:
        self.sari_peste(i).student = student

    def elimina(self, index: int) -> None:

        # daca indexul este 0, se elimina practic varful
        if index == 0:
            self.varf = self.varf.urmator
            return

        element_inainte_de_index = self.sari_peste(index-1)

        element_inainte_de_index.urmator = element_inainte_de_index.urmator.urmator

        self.n -= 1


    def sari_peste(self, i: int) -> Nod:
        # voi permite doar indici pozitivi. Se poate moderniza și pentru negativi
        a = self.varf
        if i < 0 or i >= self.n:
            raise ValueError(f"Index out of range: {i}")
        for _ in range(i):
            a = a.urmator
        return a

    def sorteaza(self) -> None:
        sortat = False
        while not sortat:
            sortat = True
            for i in range(self.n - 1):
                if self[i].medie < self[i + 1].medie:
                    self[i], self[i + 1] = self[i + 1], self[i]
                    sortat = False

    def partitie(self, s: int, d: int, comp) -> int:
        pivot = self[d]
        poz = s
        i = s
        while i < d:
            if comp(self[i], pivot):
            # if self[i].medie > pivot.medie:
                self[i], self[poz] = self[poz], self[i]
                poz += 1
            i += 1
        self[poz], self[d] = self[d], self[poz] # aduc pivotul pe poziția poz. Atenție, nu folosi valiabila locală pivot. Trebuie schimbate elementele din listă
        return poz

    def sorteazaQ(self, s: int, d: int, comp):
        if s < d:
            poz = self.partitie(s, d, comp)
            self.sorteazaQ(s, poz - 1, comp)
            self.sorteazaQ(poz + 1, d, comp)

    def __sub__(self, other: Stiva)->Stiva:

        i:int = 0
        while i < self.n:
            gasit = False
            for j in range(0, other.n):
                if self[i] == other[j]:

                    gasit = True
                    break
            if gasit:
                self.elimina(i)
                continue
            i += 1

        return self

def main():

    a = Stiva('studenti.txt')
    b = Stiva('studenti.txt')

    b.elimina(0)
    b.elimina(0)

    a.adauga(StudentCNP('A', 'info', 1, 10.0, '0'))

    a.afiseaza()
    b.afiseaza()

    a = a-b

    a.afiseaza()

if __name__=='__main__':
    main()
