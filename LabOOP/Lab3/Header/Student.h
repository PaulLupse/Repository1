#ifndef LAB3_STUDENT_H
#define LAB3_STUDENT_H

#include <string>
#include <iostream>
using namespace std;

class Student{

    string nume_complet, spec;
    int an;
    float media;

public:

    Student(string _nume_complet, string _specializare, int _an, float _media):
        nume_complet(_nume_complet),
        spec(_specializare),
        an(_an),
        media(_media){};

    static bool compNume(Student *, Student *);
    static bool compMedia(Student *, Student *);

    void afiseaza();
    friend class TabStudenti;

    friend inline ostream& operator<<(ostream& os, Student& student);

};

class TabStudenti{

    int n; //numărul de studenți
    Student ** studenti; //pointer către tabloul de studenți
    int partitie(int, int, bool (*)(Student*, Student*)); //pentru quicksort
    void quicksort(int, int, bool (* comparator)(Student*, Student*));

public:

    explicit TabStudenti(string);//citeste datele din fișierul al cărui nume e specificat prin parametru
    int getN() const {return n;}; //returnează numărul de studenți
    void afiseaza();
    void sorteaza(bool (*)(Student*, Student*));
    void sorteazaQ(bool (*)(Student*, Student*));

    friend inline ostream& operator<<(ostream& os, TabStudenti& tablou_studenti);

};

// o supraincarcare a operatorului de deplasare (pentru ostream-uri), ce faciliteaza afisarea datelor studentului
ostream& operator<<(ostream& os, Student& student) {

    cout<<"Nume de familie: "<<student.nume_complet<<"\n";
    cout<<"Specializare: "<<student.spec<<"\n";
    cout<<"An de studiu: "<<student.an<<"\n";
    cout<<"Medie: "<<student.media<<"\n";

    return os;
}

ostream& operator<<(ostream& os, TabStudenti& tablou_studenti) {

    tablou_studenti.afiseaza();
    return os;
}

#endif //LAB3_STUDENT_H