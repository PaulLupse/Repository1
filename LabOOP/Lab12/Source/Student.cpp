#include "Student.h"

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

bool Student::operator==(const Student & other) const {
    return ((nume_complet == other.nume_complet)&&(spec == other.spec)
        &&(an == other.an)&&(media == other.media));
}


//functie ce faciliteaza afisarea datelor unui student
ostream& operator<<(ostream& out_stream, const Student& student) {

    out_stream<<"Nume de familie: "<<student.nume_complet<<"\n";
    out_stream<<"Specializare: "<<student.spec<<"\n";
    out_stream<<"An de studiu: "<<student.an<<"\n";
    out_stream<<"Medie: "<<student.media<<"\n";

    return out_stream;
}

ostream& operator<<(ostream& out_stream, Student* student) {
    if (student == nullptr) {
        return out_stream;
    }
    if (typeid(*student) == typeid(StudentCNP)) {
        out_stream << (StudentCNP*)student;
        return out_stream;
    }

    out_stream<<"Nume de familie: "<<student->nume_complet<<"\n";
    out_stream<<"Specializare: "<<student->spec<<"\n";
    out_stream<<"An de studiu: "<<student->an<<"\n";
    out_stream<<"Medie: "<<student->media<<"\n";

    return out_stream;
}


void StudentCNP::afiseaza() {
    Student::afiseaza();
    cout<<"CNP: "<<cnp<<'\n';
}

bool StudentCNP::operator==(const StudentCNP& other) const {
    return(Student::operator==(other) &&  cnp == other.cnp);
}

bool StudentCNP::compMedia(StudentCNP *a, StudentCNP *b) {
    return Student::compMedia(a, b);
}

bool StudentCNP::compNume(StudentCNP *a, StudentCNP *b) {
    return Student::compNume(a, b);
}


ostream& operator<<(ostream& out_stream, const StudentCNP& student) {
    out_stream<<Student(student)<<"CNP: "<<student.cnp<<"\n";
    return out_stream;
}

ostream& operator<<(ostream& out_stream, StudentCNP* student) {
    if (student == nullptr) {
        return out_stream;
    }
    out_stream<<Student(*student)<<"CNP: "<<student->cnp<<"\n";
    return out_stream;
}
