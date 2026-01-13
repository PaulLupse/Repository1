from src.ListaStudenti import ListaStudenti

def main():

    ls = ListaStudenti(nume_fisier="studenti.txt")
    ls.afiseaza()

if __name__ == "__main__":
    main()