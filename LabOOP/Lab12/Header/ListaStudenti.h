#ifndef LAB3_STIVA_H
#define LAB3_STIVA_H

#include "Student.h"

class Nod;

template<typename tip>
class ListaStudentiOrdonata;

template<typename tip>
class ListaStudenti;

// specializare a clasei ListaStudenti pentru obiecte de tip Student
template<>
class ListaStudenti<Student>{

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

        template<typename tip>
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
class ListaStudentiOrdonata<Student>:public ListaStudenti<Student> {

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

// generalizare a ListaStudenti (practic o lista simpla)
template<typename tip>
class ListaStudenti {

protected:

    class Nod {

        tip* date;
        Nod *next, *prev;

    public:

        // constructor default
        Nod():date(new tip()),next(nullptr),prev(nullptr){};
        // constructor de copiere
        Nod(const Nod& other):
            date(new tip(*other.date)),
            next(nullptr),
            prev(nullptr){};

        Nod(tip* obiect);

        ~Nod();

        // returneaza datele memorate de nod
        tip* get_date()const{return date;}

        // seteaza datele nodului
        void set_date(tip *obiect){date = obiect;}

        template<typename alt_tip>
        friend class ListaStudenti;
        template<typename alt_tip>
        friend class ListaStudentiOrdonata;
        template<typename alt_tip>
        friend ostream& operator<<(ostream&, ListaStudenti<alt_tip>&);
        template<typename alt_tip>
        friend ostream& operator<<(ostream&, ListaStudentiOrdonata<alt_tip>&);
    };

    Nod *baza, *varf;
    int nrNoduri;

    // folosita la quicksort
    Nod* partitie(Nod*, Nod*, bool (*)(tip*, tip*));
    void quicksort(Nod*, Nod*, bool (*)(tip*, tip*));

    // interschimba doua obiecte de tip student
    static void swap_obiecte(tip*&, tip*&);

public:

    ListaStudenti():baza(nullptr),varf(nullptr),nrNoduri(0){};
    explicit ListaStudenti(string nume_fisier);
    ListaStudenti(const ListaStudenti & other);
    ~ListaStudenti();

    void adaugaVarf(tip * obiect);
    void adaugaBaza(tip * obiect);

    void eliminaVarf();
    void eliminaBaza();

    // extrage un varf din capatul listei
    tip* extrageVarf() const;

    // extrage un varf de la inceputul listei
    tip* extrageBaza() const;

    void afiseaza() const;
    // sorteaza folosind bubblesort
    void sorteaza(bool (*)(tip*, tip*));
    // sorteaza folosind quicksort
    void sorteazaQ(bool (*)(tip*, tip*));

    int lungime()const{return nrNoduri;};

    tip*& operator[](int index);
    ListaStudenti operator+(ListaStudenti&);
    ListaStudenti operator-(ListaStudenti&);
    ListaStudenti& operator=(ListaStudenti);


    template<typename alt_tip>
    friend class ListaStudenti;
    template<typename alt_tip>
    friend class ListaStudentiOrdonata;

    template<typename alt_tip>
    friend ostream& operator<<(ostream&, ListaStudenti<alt_tip>&);
};


template<typename tip>
class ListaStudentiOrdonata:public ListaStudenti<tip> {

public:
    bool (*comparator)(tip*, tip*);

    // constructor default
    ListaStudentiOrdonata():ListaStudenti<tip>(),comparator(&tip::compare){};

    explicit ListaStudentiOrdonata(bool (*_comparator)(tip*, tip*)):
        ListaStudenti<tip>(),comparator(_comparator){};
    explicit ListaStudentiOrdonata(string nume_fisier, bool (*_comparator)(tip*, tip*)):
        ListaStudenti<tip>(nume_fisier),comparator(_comparator){sorteazaQ(_comparator);};

    // constructor de copiere
    ListaStudentiOrdonata(const ListaStudentiOrdonata & other):ListaStudenti<tip>(other),comparator(other.comparator){};

    void adauga(tip* obiect);
    void adaugaVarf(tip * obiect);
    void adaugaBaza(tip * obiect);

    ListaStudentiOrdonata& operator=(ListaStudentiOrdonata);

    template<typename alt_tip>
    friend ostream& operator<<(ostream&, ListaStudentiOrdonata<alt_tip>&);
};





template<typename tip>
ListaStudenti<tip>::~ListaStudenti() {

    while (varf) {
        eliminaVarf();
    }
}

template<typename tip>
ListaStudenti<tip>::ListaStudenti(const ListaStudenti<tip>& other):baza(nullptr), varf(nullptr),nrNoduri(0) {

    // mergem pe la fiecare nod din lista other si il adaugam in lista
    for (Nod* iterator = other.baza; iterator != nullptr; iterator = iterator->next)
        adaugaVarf(new tip(*(iterator->date)));

}

template<typename tip>
ListaStudenti<tip>::Nod::Nod(tip* obiect):next(nullptr),prev(nullptr) {

    date = new tip(*obiect);
}

template<typename tip>
ListaStudenti<tip>::Nod::~Nod() {
    // datele din nod sunt alocate dinamic deci trebuie eliberata memoria la distrugere
    delete date;
}

template<typename tip>// adauga un student la finalul cozii
void ListaStudenti<tip>::adaugaVarf(tip * obiect) {

    Nod* nod_nou = new Nod(obiect);
    if (varf == nullptr) { // daca lista e nula, noul nod devine inceputul si sfarsitul
        varf = nod_nou;
        baza = varf;
        nrNoduri=1;
    }
    else {
        // altfel, noul nod devine succesorul varfului, iar varful devine predecesorul acestuia
        varf->next = nod_nou;
        nod_nou -> prev = varf;
        // noul nod devine varful
        varf = nod_nou;
        nrNoduri++;
    }
}

template<typename tip>
void ListaStudenti<tip>::adaugaBaza(tip * obiect) {

    Nod* nod_nou = new Nod(obiect);
    if (varf == nullptr) { // daca lista e nula, noul nod devine inceputul si sfarsitul
        varf = nod_nou;
        baza = varf;
        nrNoduri=1;
    }
    else {
        // altfel, noul nod devine predecesorul bazei, iar baza devine succesorul noului nod
        baza->prev = nod_nou;
        nod_nou -> next = baza;
        // noul nod devine baza
        baza = nod_nou;
        nrNoduri++;
    }
}

template<typename tip>
void ListaStudenti<tip>::eliminaVarf() {

    if (varf == nullptr) {
        cerr<<"Eroare: Incercarea eliminarii elementelor dintr-o listă goală.\n";
        return;
    }
    if (varf == baza) { // daca exista un singur element in lista
        delete varf;
        // lista devine nula
        varf = baza = nullptr;
        nrNoduri=0;
    }
    else {
        // nodul predecesor varfului curent devine noul varf
        varf = varf->prev;
        // varf -> next este acum varful anterior, ce trebuie eliminat
        delete varf->next;
        varf->next = nullptr;

        nrNoduri--;
    }
}

template<typename tip>
void ListaStudenti<tip>::eliminaBaza() {
    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea eliminarii elementelor dintr-o listă goală.\n";
        return;
    }
    if (varf == baza) { // daca exista un singur element in lista
        delete baza;
        // lista devine nula
        varf = baza = nullptr;
        nrNoduri=0;
    }
    else {
        // nodul succesor bazei curente devine noua baza
        baza = baza -> next;
        // baza -> prev este acum baza anterioara, ce trebuie eliminata
        delete baza->prev;
        baza->prev = nullptr;

        nrNoduri--;
    }
}

template<typename tip>
tip *ListaStudenti<tip>::extrageVarf() const {
    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea extragerii unui element dintr-o listă goală.\n";
        return nullptr;
    }
    return varf->date;
}

template<typename tip>
tip *ListaStudenti<tip>::extrageBaza() const{
    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea extragerii unui element dintr-o listă goală.\n";
        return nullptr;
    }
    return baza->date;
}

// afiseaza la consola lista de studenti
template<typename tip>
void ListaStudenti<tip>::afiseaza() const{
    // folosim un iterator pentru a parcurge lista de studenti
    for (Nod* iterator = baza; iterator != nullptr; iterator = iterator->next) {
        cout<<iterator->date;
    }
}


template<typename tip>
tip*& ListaStudenti<tip>::operator[](int index) {
    if (nrNoduri == 0) {
        throw range_error("Eroare: Incercarea extragerii unui element dintr-o listă goală.");
    }
    if (index < 0 || index > nrNoduri)
        throw range_error("Eroare: Index in afara capetelor listei.");
    // daca studentul cautat se afla in prima jumatate a listei
    if (index < nrNoduri/2) {
        // incepem cautarea de la baza
        Nod * iterator = baza;
        // si mergem spre varf
        for (int i = 0; i < index; i++) {
            iterator = iterator->next;
        }
        return iterator->date;
    }
    // altfel
    else {
        // incepem de la varf
        Nod * iterator = varf;
        // si mergem spre baza
        for (int i = nrNoduri-1; i > index; i--) {
            iterator = iterator->prev;
        }
        return iterator->date;
    }
}

template<typename tip>
ListaStudenti<tip> ListaStudenti<tip>::operator+(ListaStudenti<tip>& other_lista) {

    ListaStudenti rezultat(*this);
    ListaStudenti other(other_lista);

    if (rezultat.varf == nullptr)
        return rezultat;
    if (other.baza == nullptr)
        return other;

    rezultat.varf->next = other.baza;
    other.baza->prev = rezultat.varf;
    rezultat.nrNoduri += other.nrNoduri;

    rezultat.varf = other.varf;
    // ca sa nu se stearga datele copiei listei care se alipeste la aceasta lista
    other.baza = other.varf = nullptr;

    return rezultat;
}

template<typename tip>
ListaStudenti<tip> ListaStudenti<tip>::operator-(ListaStudenti<tip>& other_lista) {

    ListaStudenti rezultat(*this);
    ListaStudenti other(other_lista);

    if (rezultat.varf == nullptr)
        return rezultat;
    if (other.varf == nullptr)
        return other;

    Nod* iterator = rezultat.baza;
    while (iterator !=  nullptr) {

        Nod* other_iterator = other.baza;
        bool step = true;
        while (other_iterator != nullptr){
            if (*(iterator->date) == *(other_iterator->date)) {

                if (iterator == rezultat.baza) {
                    rezultat.eliminaBaza();
                    iterator = rezultat.baza;
                }
                else if (iterator == rezultat.varf) {
                    rezultat.eliminaVarf();
                    iterator = rezultat.varf;
                }
                else {
                    Nod* cp_iterator = iterator;
                    iterator->prev->next = iterator->next;
                    iterator->next->prev = iterator->prev;
                    iterator = iterator->next;
                    delete cp_iterator;
                }
                step = false;
                break;
            }
            other_iterator = other_iterator->next;
        }
        if (step)
            iterator = iterator->next;
    }

    return rezultat;
}

template<typename tip>
ListaStudenti<tip>& ListaStudenti<tip>::operator=(ListaStudenti<tip> other) {

    while (varf) {
        eliminaVarf();
    }
    varf = other.varf;
    baza = other.baza;
    nrNoduri = other.nrNoduri;
    other.baza = other.varf = nullptr;
    return *this;
}

template<typename tip>
void ListaStudenti<tip>::swap_obiecte(tip*& a, tip*& b) {
    tip* aux = a;
    a = b;
    b = aux;
}

template<typename tip>
void ListaStudenti<tip>::sorteaza(bool (*compara)(tip*, tip*)) {
    if (nrNoduri == 0) return;
    bool sortat = false;
    while (!sortat) {
        sortat = true;
        // folosim un iterator pentru a accesa elementele din lista
        Nod * iterator = baza;
        while (iterator->next != nullptr) {
            // compara datele iteratorului si datele succesorului iteratorului
            if (compara(iterator->date,iterator->next->date)) {
                sortat = false;
                // interschimba datele iteratorului si datele succesorului iteratorului
                swap(iterator->date,iterator->next->date);
            }
            // 'incrementam' iteratorul
            iterator = iterator -> next;
        }
    }
}

// implementeaza partitia lui Hoare pentru quicksort folosind doua noduri pe post de iteratori
// care este mai eficienta (d.p.d.v al timpului) fata de implementarea folosind indecsi si operatorul de indexare []
template<typename tip>
typename ListaStudenti<tip>::Nod* ListaStudenti<tip>::partitie(Nod* st, Nod* dr, bool (*compare)(tip *, tip *)) {
    int d = 1;
    // in acest caz este luat varful ca fiind index
    // deoarece se modifica intai iteratorul de stanga (daca nu a avut loc initial o interschimbare)
    while (st != dr) {
        if (compare(st->date, dr->date)) {
            swap(st->date, dr->date);
            d = 1-d;
        }
        if (d == 0)
            dr = dr->prev;
        else
            st = st->next;
    }
    return st;
}

template<typename tip>
void ListaStudenti<tip>::quicksort(Nod* st, Nod* dr, bool (*compare)(tip *, tip *)) {

    // deoarece lucram cu adrese, putem doar sa verificam doar daca iteratorii nu sunt egali intre ei sau daca sunt nuli
    if (st != dr && st != nullptr && dr != nullptr) {
        Nod* mid = partitie(st, dr, compare);
        quicksort(st, mid->prev, compare);
        quicksort(mid, dr, compare);
    }
}

template<typename tip>
void ListaStudenti<tip>::sorteazaQ(bool (*compare)(tip *, tip *)) {
    if (nrNoduri == 0) return;
    quicksort(baza, varf, compare);
}



template<typename tip>
void ListaStudentiOrdonata<tip>::adaugaVarf(tip *obiect) {
    adauga(obiect);
}

template<typename tip>
void ListaStudentiOrdonata<tip>::adaugaBaza(tip *obiect) {
    adauga(obiect);
}

template<typename tip>
ListaStudentiOrdonata<tip> &ListaStudentiOrdonata<tip>::operator=(ListaStudentiOrdonata<tip> other) {
    this->ListaStudenti<tip>::operator=(ListaStudenti<tip>(other));
    comparator = other.comparator;
    return *this;
}

template<typename tip>
ostream &operator<<(ostream &out_stream, ListaStudentiOrdonata<tip> &lista) {

    out_stream << "Total obiecte: " << lista.nrNoduri << endl;
    for (typename ListaStudentiOrdonata<tip>::Nod* iterator = lista.baza; iterator != nullptr; iterator = iterator->next) {
        cout<<endl;
        out_stream<<iterator->date;
    }
    out_stream<<"\n";
    return out_stream;
}


template<typename tip>
void ListaStudentiOrdonata<tip>::adauga(tip *obiect) {


    if (this->varf == this->baza) {
        if ((this->varf == nullptr) || comparator(obiect, this->varf->date))
            ListaStudenti<tip>::adaugaVarf(obiect);
        else ListaStudenti<tip>::adaugaBaza(obiect);

        return;
    }

    auto new_nod = new typename ListaStudenti<tip>::Nod(obiect);
    typename ListaStudenti<tip>::Nod* iterator = this->varf;

    // efectueaza, practic, o operatie de tip adaugare intr-o coada de prioritate
    while (iterator!= nullptr) {
        if (comparator(obiect,iterator->date)) {
            break;
        }
        iterator = iterator->prev;
    }

    if (iterator == nullptr)
        ListaStudenti<tip>::adaugaBaza(obiect);
    else if (iterator == this->varf)
        ListaStudenti<tip>::adaugaVarf(obiect);
    else {
        new_nod->prev = iterator;
        new_nod->next = iterator->next;
        iterator->next->prev = new_nod;
        iterator->next = new_nod;

        ++this->nrNoduri;
    }

}

#endif //LAB3_STIVA_H

