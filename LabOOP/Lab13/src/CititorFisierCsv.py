from src.Student import Student, StudentCNP

class CititorFisierCsv:

    def __init__(self, nume_fisier:str):

        self.nume_fisier:str = nume_fisier

    def citeste(self):

        lista_studenti:list[Student|StudentCNP] = []
        with open(self.nume_fisier, 'r') as fisier:

            for index_linie, linie in enumerate(fisier):

                date_student:list[str|int|float] = linie.split(',')
                # daca date_student contine 6 elemente, atunci este prezent si un cnp
                if len(date_student) == 6:
                    lista_studenti.append(StudentCNP(date_student[0] + ' '+ date_student[1], date_student[2],
                                                     date_student[3], date_student[4], date_student[5]))
                elif len(date_student) == 5: lista_studenti.append(Student(date_student[0] + ' ' + date_student[1], date_student[2],
                                                     date_student[3], date_student[4]))
                else: raise Exception(f"Linia {index_linie} din fisierul {self.nume_fisier} este invalida.")

            fisier.close()

        return lista_studenti
