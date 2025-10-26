#ifndef LAB3_STUDENT_H
#define LAB3_STUDENT_H

#include <string>
#include <iostream>
using namespace std;

// clasa ce memoreaza datele despre un student
class Student{

    string nume_complet, spec;
    int an;
    float media;

public:

    Student():
    nume_complet(),
        spec(),
        an(0),
        media(0.0f){};

    Student(const string& _nume_complet, const string& _specializare,const int& _an, const float& _media):
        nume_complet(_nume_complet),
        spec(_specializare),
        an(_an),
        media(_media){};

    static bool compNume(Student *, Student *);
    static bool compMedia(Student *, Student *);

    void afiseaza();
    friend class TabStudenti;

    friend inline ostream& operator<<(ostream& os, const Student& student);

};

class TabStudenti{

    int n; //numărul de studenți
    Student ** studenti; //pointer către tabloul de studenți
    int partitie(int, int, bool (*)(Student*, Student*)); //pentru quicksort
    void quicksort(int, int, bool (* comparator)(Student*, Student*));

    void swap_studenti(int, int);

public:

    explicit TabStudenti(string);//citeste datele din fișierul al cărui nume e specificat prin parametru
    ~TabStudenti();

    int getN() {return n;}; //returnează numărul de studenți
    void afiseaza();
    void sorteaza(bool (*)(Student*, Student*));
    void sorteazaQ(bool (*)(Student*, Student*));

    friend ostream& operator<<(ostream&, TabStudenti&);

};

// o supraincarcare a operatorului de deplasare (pentru ostream-uri), ce faciliteaza afisarea datelor studentului
ostream& operator<<(ostream&, Student&);


#endif //LAB3_STUDENT_H