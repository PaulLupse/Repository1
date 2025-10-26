#include "Student.h"
#include "CSVReader.h"
#include <vector>

// Student

// metoda ce afiseaza la consola datele unui student
void Student::afiseaza() {
    cout<<"\nNume: " << nume_complet<<'\n';
    cout<<"Specializare: " << spec<<'\n';
    cout<<"An: " << an<<'\n';
    cout<<"Medie: " << media<<'\n';
}


// medota ce compara doi studenti dupa medie
// returneaza true daca media primului student este mai mica decat celui de-al doilea
bool Student::compMedia(Student* a, Student* b) {
    return (a->media > b->media);
}

// metoda ce compara doi studenti dupa numele complet
// returneaza true daca numele primului student este lexicografic mai maire decat celui de-al doilea
bool Student::compNume(Student *a, Student *b) {
    int cmp = a->nume_complet.compare(b->nume_complet);
    if (cmp > 0) return true;
    return false;
}

// functie ce faciliteaza afisarea datelor unui student
ostream& operator<<(ostream& out_stream, const Student& student) {

    out_stream<<"Nume de familie: "<<student.nume_complet<<"\n";
    out_stream<<"Specializare: "<<student.spec<<"\n";
    out_stream<<"An de studiu: "<<student.an<<"\n";
    out_stream<<"Medie: "<<student.media<<"\n";

    return out_stream;
}

// TabStudenti

TabStudenti::TabStudenti(string nume_fisier) {

    // metoda foloseste un obiect de tip CSVReader pentru citirea fisierului cu nume 'nume_fisier'
    CSVReader cititor_fisier(nume_fisier);
    // citirea returneaza un vector de Studenti
    vector<Student> vector_studenti = cititor_fisier.citeste();
    n = vector_studenti.size();

    studenti = new Student*[n];

    int index = 0;
    for (auto i = vector_studenti.begin(); i != vector_studenti.end(); i++, index++) {
        studenti[index] = new Student((*i).nume_complet, (*i).spec, (*i).an, (*i).media);
    }
}

TabStudenti::~TabStudenti() {
    delete [] studenti;
}

// afiseaza tabloul de studenti prin apelarea metodei de afisare a fiecarui studenti
void TabStudenti::afiseaza() {
    for (int i = 0; i < n; i++) {
        studenti[i]->afiseaza();
    }
}

// interschimba valorile de pe pozitiile i si j al tabloului studenti
void TabStudenti::swap_studenti(int i, int j) {
    Student* aux = studenti[i];
    studenti[i] = studenti[j];
    studenti[j] = aux;
}


// implementeaza Bubble Sort
void TabStudenti::sorteaza(bool (*comparare)(Student*, Student*)) {
    bool sorted = false;
    while (!sorted) {
        sorted = true;
        for (int i = 0; i < n-1; i++) {
            if (comparare(studenti[i], studenti[i + 1])) {
                sorted = false;
                swap_studenti(i, i+1);
            }
        }
    }
}

// partitioneaza tabloul studenti, pentru quicksort
// returneaza indexul de sfarsit al partii mai mici decat pivotul ales
int TabStudenti::partitie(int i, int j, bool (*comp)(Student *, Student *)) {

    int d = 0;

    // pivotul (studenti[i]) este pus in mijlocul tabloului
    swap_studenti(i, (i+j)/2);
    while (i < j) { // cat timp nu se intersecteaza indecsii
        if (comp(studenti[i], studenti[j])) {
            swap_studenti(i, j);
            // de fiecare data cand este realizata o insterschimbare, se schimba indexul care este modificat
            d = 1 - d;
        }
        // este modificat un sigur index la fiecare pas
        // fie creste i, fie scade j
        if (d == 0)
            i ++;
        else
            j --;
    }
    return i;
}

// implementeaza quicksort, se foloseste de metoda partitie pentru partitionare
void TabStudenti::quicksort(int st, int dr, bool (*comp)(Student*, Student*)) {
    if (st < dr) {
        int mid = partitie(st, dr, comp);
        quicksort(st, mid-1, comp);
        quicksort(mid, dr, comp);
    }
}

// functie ce sorteaza primele n elemente din vectorul de studenti, folosind functia precizata ca si comparator
void TabStudenti::sorteazaQ(bool (*comp)(Student*, Student*)) {
    quicksort(0, n-1, comp);
}

ostream& operator<<(ostream& out_stream, TabStudenti& tablou_studenti) {

    for (int i = 0; i < tablou_studenti.n; i++) {
        out_stream << *(tablou_studenti.studenti[i]);
    }
    return out_stream;
}

