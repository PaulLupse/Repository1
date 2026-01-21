#include <Student.h>


Student::Student() {
    prenume = string();
    nume_de_familie = string();
    specializare = string();
    an = 0;
    medie = 0.0f;
}

Student::Student(const Student& other) {
    prenume = other.prenume;
    nume_de_familie = other.nume_de_familie;
    specializare = other.specializare;
    an = other.an;
    medie = other.medie;
}

bool Student::compare_medie(Student *a, Student *b)  {
    return (a->medie > b->medie);
}

bool Student::compare_nume(Student *a, Student *b)  {

    int cmp = a->nume_de_familie.compare(b->nume_de_familie);
    if (cmp == 0) {
        if (a->prenume.compare(b->prenume) > 0)
            return true;
    }
    else if (cmp > 0) return true;
    return false;
}
