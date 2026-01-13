# include "ListaStudenti.h"

#include <iostream>
#include <stdexcept>

#include "CSVReader.h"

ListaStudenti::~ListaStudenti() {

    while (varf) {
        eliminaVarf();
    }
}

ListaStudenti::ListaStudenti(const ListaStudenti& other):baza(nullptr), varf(nullptr),nrNoduri(0) {

    // mergem pe la fiecare nod din lista other si il adaugam in lista
    for (Nod* iterator = other.baza; iterator != nullptr; iterator = iterator->next)
        adaugaVarf(new Student(*(iterator->date)));

}

ListaStudenti::ListaStudenti(string nume_fisier):baza(nullptr), varf(nullptr), nrNoduri(0) {

    CSVReader cititor_fisier(nume_fisier);
    vector<Student*> studenti = cititor_fisier.citeste();

    for (Student* student : studenti) {
        adaugaVarf(student);
    }
}

ListaStudenti::Nod::Nod(Student* student):next(nullptr),prev(nullptr) {


    if (typeid(*student) == typeid(StudentCNP)) {
        date = new StudentCNP((StudentCNP*)student);
    }
    else date = new Student(student);
}

ListaStudenti::Nod::~Nod() {
    // datele din nod sunt alocate dinamic deci trebuie eliberata memoria la distrugere
    delete date;
}

// adauga un student la finalul cozii
void ListaStudenti::adaugaVarf(Student * student) {

    Nod* nod_nou = new Nod(student);
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

void ListaStudenti::adaugaBaza(Student * student) {

    Nod* nod_nou = new Nod(student);
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

void ListaStudenti::eliminaVarf() {

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

void ListaStudenti::eliminaBaza() {
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

Student *ListaStudenti::extrageVarf() const {
    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea extragerii unui element dintr-o listă goală.\n";
        return nullptr;
    }
    return varf->date;
}

Student *ListaStudenti::extrageBaza() const{
    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea extragerii unui element dintr-o listă goală.\n";
        return nullptr;
    }
    return baza->date;
}

// afiseaza la consola lista de studenti
void ListaStudenti::afiseaza() const{
    // folosim un iterator pentru a parcurge lista de studenti
    for (Nod* iterator = baza; iterator != nullptr; iterator = iterator->next) {
        cout<<iterator->date;
    }
}

void ListaStudenti::sterge(string nume_student) {

    if (nrNoduri == 0) {
        cerr<<"Eroare: Incercarea eliminarii elementelor dintr-o listă goală.\n";
        return;
    }

    while (baza->date->nume_complet == nume_student && baza != nullptr)
        eliminaBaza();

    while (varf->date->nume_complet == nume_student && varf != nullptr)
        eliminaVarf();

    Nod* iterator = baza;
    while (iterator != nullptr){
        if (iterator->date->get_nume_complet() == nume_student) {
            // daca s-a gasit nodul care retine datele despre studentul cu numele specificat
            iterator->prev->next = iterator->next; // succesorul predecesorului nodului devine succesorul nodului
            iterator->next->prev = iterator->prev; // predecesorul succesorului nodului devine predecesorul nodului

            // nodul gasit este eliminat
            Nod* cp_iterator = iterator;
            iterator = iterator->next;
            delete cp_iterator;
        }
        else iterator = iterator->next;
    }
}

Student*& ListaStudenti::operator[](int index) {
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

ListaStudenti ListaStudenti::operator+(ListaStudenti& other_lista) {

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

ListaStudenti ListaStudenti::operator-(ListaStudenti& other_lista) {

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

ListaStudenti& ListaStudenti::operator=(ListaStudenti other) {

    while (varf) {
        eliminaVarf();
    }
    varf = other.varf;
    baza = other.baza;
    nrNoduri = other.nrNoduri;
    other.baza = other.varf = nullptr;
    return *this;
}

void ListaStudenti::swap_studenti(Student*& a, Student*& b) {
    Student* aux = a;
    a = b;
    b = aux;
}

void ListaStudenti::sorteaza(bool (*compara)(Student*, Student*)) {
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
ListaStudenti::Nod* ListaStudenti::partitie(Nod* st, Nod* dr, bool (*compare)(Student *, Student *)) {
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

void ListaStudenti::quicksort(Nod* st, Nod* dr, bool (*compare)(Student *, Student *)) {

    // deoarece lucram cu adrese, putem doar sa verificam doar daca iteratorii nu sunt egali intre ei sau daca sunt nuli
    if (st != dr && st != nullptr && dr != nullptr) {
        Nod* mid = partitie(st, dr, compare);
        quicksort(st, mid->prev, compare);
        quicksort(mid, dr, compare);
    }
}

void ListaStudenti::sorteazaQ(bool (*compare)(Student *, Student *)) {
    if (nrNoduri == 0) return;
    quicksort(baza, varf, compare);
}

void ListaStudentiOrdonata<Student>::adauga(Student *student) {

    // daca student retine, de fapt, referinta la un StudentCNP (alocat dinamic), atunci are un cnp ce trebuie verificat
    if (typeid(*student) == typeid(StudentCNP)) {

        StudentCNP* student_cnp = (StudentCNP*) student;

        Nod* iterator = baza;
        while (iterator != nullptr) {
            if (typeid(*(iterator->date)) == typeid(StudentCNP)) {
                StudentCNP* iterator_student = (StudentCNP*) iterator->date;
                if (student_cnp->cnp == iterator_student->cnp) {
                    return;
                }
            }
            iterator = iterator->next;
        }
    }

    if (varf == baza) {
        if ((varf == nullptr) || comparator(student, varf->date))
            ListaStudenti::adaugaVarf(student);
        else ListaStudenti::adaugaBaza(student);

        return;
    }

    Nod* new_nod = new Nod(student);
    Nod* iterator = varf;

    // efectueaza, practic, o operatie de tip adaugare intr-o coada de prioritate
    while (iterator!= nullptr) {
        if (comparator(student,iterator->date)) {
            break;
        }
        iterator = iterator->prev;
    }

    if (iterator == nullptr)
        ListaStudenti::adaugaBaza(student);
    else if (iterator == varf)
        ListaStudenti::adaugaVarf(student);
    else {
        new_nod->prev = iterator;
        new_nod->next = iterator->next;
        iterator->next->prev = new_nod;
        iterator->next = new_nod;

        ++nrNoduri;
    }

}

void ListaStudentiOrdonata<Student>::adaugaVarf(Student *student) {
    adauga(student);
}

void ListaStudentiOrdonata<Student>::adaugaBaza(Student *student) {
    adauga(student);
}

ListaStudentiOrdonata<Student> &ListaStudentiOrdonata<Student>::operator=(ListaStudentiOrdonata<Student> other) {
    this->ListaStudenti::operator=(ListaStudenti(other));
    comparator = other.comparator;
    return *this;
}

ostream& operator<<(ostream& out_stream, ListaStudenti& lista) {

    out_stream << "Total studenți: " << lista.nrNoduri << endl;
    for (ListaStudenti::Nod* iterator = lista.baza; iterator != nullptr; iterator = iterator->next) {
        out_stream<<iterator->date;
    }
    out_stream<<"\n";
    return out_stream;
}

ostream &operator<<(ostream &out_stream, ListaStudentiOrdonata<Student> &lista) {

    out_stream << "Total studenți: " << lista.nrNoduri << endl;
    for (ListaStudentiOrdonata<Student>::Nod* iterator = lista.baza; iterator != nullptr; iterator = iterator->next) {
        cout<<endl;
        out_stream<<iterator->date;
    }
    out_stream<<"\n";
    return out_stream;
}



