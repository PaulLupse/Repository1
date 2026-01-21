#ifndef LAB3_STIVA_H
#define LAB3_STIVA_H

#include "Student.h"

class Nod;

template<typename tip>
class ListaStudentiOrdonata;
// clasa care implementeaza o lista dublu inlantuita pentru tipul Studenti
class ListaStudenti{

    // clasa folosita pentru implementarea listei dublu inlantuite
protected:
    class Nod {

        Student* date;
        Nod *next, *prev;

    public:

        // constructor default
        Nod():date(new Student()),next(nullptr),prev(nullptr){};
        // constructor de copiere
        Nod(const Nod& other):
            date(new Student(*other.date)),
            next(nullptr),
            prev(nullptr){};

        explicit Nod(Student* student);

        ~Nod();

        // returneaza datele memorate de nod
        Student* get_date()const{return date;}

        // seteaza datele nodului
        void set_date(Student *student){date = student;}

        friend class ListaStudenti;
        template<typename tip>
        friend class ListaStudentiOrdonata;
        friend ostream& operator<<(ostream&, ListaStudenti&);
        friend ostream& operator<<(ostream&, ListaStudentiOrdonata<Student>&);
    };

    Nod *baza, *varf;
    int nrNoduri;

    // folosita la quicksort
    Nod* partitie(Nod*, Nod*, bool (*)(Student*, Student*));
    void quicksort(Nod*, Nod*, bool (*)(Student*, Student*));

    // interschimba doua obiecte de tip student
    static void swap_studenti(Student*&, Student*&);

public:

    ListaStudenti():baza(nullptr),varf(nullptr),nrNoduri(0){};
    explicit ListaStudenti(string nume_fisier);
    ListaStudenti(const ListaStudenti & other);
    ~ListaStudenti();

    void adaugaVarf(Student * student);
    void adaugaBaza(Student * student);

    void eliminaVarf();
    void eliminaBaza();

    // extrage un varf din capatul listei
    Student* extrageVarf() const;

    // extrage un varf de la inceputul listei
    Student* extrageBaza() const;

    void afiseaza() const;
    // sterge dupa nume
    void sterge(string);
    // sorteaza folosind bubblesort
    void sorteaza(bool (*)(Student*, Student*));
    // sorteaza folosind quicksort
    void sorteazaQ(bool (*)(Student*, Student*));

    int lungime()const{return nrNoduri;};

    Student*& operator[](int index);
    ListaStudenti operator+(ListaStudenti&);
    ListaStudenti operator-(ListaStudenti&);
    ListaStudenti& operator=(ListaStudenti);

    friend ostream& operator<<(ostream&, ListaStudenti&);
};

template<>
class ListaStudentiOrdonata<Student>:public ListaStudenti {

public:
    bool (*comparator)(Student*, Student*);

    // constructor default
    ListaStudentiOrdonata():ListaStudenti(),comparator(&Student::compMedia){};

    explicit ListaStudentiOrdonata(bool (*_comparator)(Student*, Student*)):
        ListaStudenti(),comparator(_comparator){};
    explicit ListaStudentiOrdonata(string nume_fisier, bool (*_comparator)(Student*, Student*)):
        ListaStudenti(nume_fisier),comparator(_comparator){sorteazaQ(_comparator);};

    // constructor de copiere
    ListaStudentiOrdonata(const ListaStudentiOrdonata & other):ListaStudenti(other),comparator(other.comparator){};

    ~ListaStudentiOrdonata(){ListaStudenti::~ListaStudenti();};

    void adauga(Student* student);
    void adaugaVarf(Student * student);
    void adaugaBaza(Student * student);

    ListaStudentiOrdonata& operator=(ListaStudentiOrdonata);

    friend ostream& operator<<(ostream&, ListaStudentiOrdonata&);
};



#endif //LAB3_STIVA_H