#ifndef LAB3_STIVA_H
#define LAB3_STIVA_H

#include "Student.h"

class Nod;

class ListaStudenti{

    class Nod {

        Student date;
        Nod *next, *prev;

    public:

        Nod():date(Student()),next(nullptr),prev(nullptr){};
        Nod(const Nod& other):
            date(other.date),
            next(other.next),
            prev(other.prev){};

        explicit Nod(const Student* student):date(*student),next(nullptr),prev(nullptr){};
        explicit Nod(const Student& student):date(student),next(nullptr),prev(nullptr){};

        Student get_date()const{return date;}
        Nod* get_next()const{return next;}
        Nod* get_prev()const{return prev;}

        void set_date(const Student &student){date = student;}

        friend ostream& operator<<(ostream& out_stream, const Nod& nod);

    };

    Nod * varf, *baza;
    void eliminaVarf();
    void eliminaBaza();
    int nrNoduri;
    int partitie(int, int, bool (*)(Student*, Student*));
    void quicksort(int, int, bool (*)(Student*, Student*));

public:

    ListaStudenti():varf(nullptr),baza(nullptr),nrNoduri(0){};
    ListaStudenti(const ListaStudenti & other);
    ~ListaStudenti();
    void adauga(Student * student);
    Student* extrage(); //opțional (nu e necesar)
    void afiseaza();
    // sterge dupa nume
    void sterge(string);
    // sorteaza folosind bubblesort
    void sorteaza(bool (*)(Student*, Student*));
    // sorteaza folosind quicksort
    void sorteazaQ(bool (*)(Student*, Student*));
    int lungime(){return nrNoduri;};

    friend ostream& operator<<(ostream&, const Nod&);

};


#endif //LAB3_STIVA_H