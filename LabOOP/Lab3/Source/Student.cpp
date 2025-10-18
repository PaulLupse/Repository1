#include "Student.h"
#include "CSVReader.h"
#include <vector>
#include <CSVReader.h>

void Student::afiseaza() {
    cout<<"Nume: " << nume_complet<<'\n';
    cout<<"Specializare: " << spec<<'\n';
    cout<<"An: " << an<<'\n';
    cout<<"Medie: " << media<<'\n';
}

bool Student::compMedia(Student* a, Student* b) {
    return (a->media > b->media);
}

bool Student::compNume(Student *a, Student *b) {
    int cmp = a->nume_complet.compare(b->nume_complet);
    if (cmp > 0) return true;
    return false;
}


TabStudenti::TabStudenti(string nume_fisier) {

    CSVReader cititor_fisier(nume_fisier);
    vector<Student> vector_studenti;
    n = vector_studenti.size();

    Student* tablou_studenti = (Student*)malloc(sizeof(Student)*n);

    int index = 0;
    for (auto i = vector_studenti.begin(); i != vector_studenti.end(); i++, index++) {
        tablou_studenti[index] = Student(i->nume_complet, i->spec, i->an, i->media);
    }

    studenti = &tablou_studenti;
}

void TabStudenti::afiseaza() {
    for (int i = 0; i < n; i++) {
        (*studenti)[i].afiseaza();
    }
}
