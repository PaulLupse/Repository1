
class Student:

    def __init__(self, nume_prenume:str, specializare:str, an_studiu:int, medie:float):

        self._nume_prenume:str = nume_prenume
        self._specializare:str = specializare
        self._an_studiu:int = an_studiu
        self._medie:float = medie

    def afiseaza(self):
        print ( f"Nume complet: {self._nume_prenume}\nSpecializare: {self._specializare}\nAn: {self._an_studiu}\nMedie: {self._medie}" )
        if type(self) == Student:
            print()


class StudentCNP(Student):

    def __init__(self, nume_prenume:str, specializare:str, an_studiu:int, medie:float, cnp:str):
        super().__init__(nume_prenume, specializare, an_studiu, medie)
        self._cnp:str = cnp

    def afiseaza(self):

        super().afiseaza()
        print(f"CNP: {self._cnp}")

