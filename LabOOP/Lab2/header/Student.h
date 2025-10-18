#ifndef LAB2_STUDENT_H
#define LAB2_STUDENT_H

#include <iostream>
#include <string>

using namespace std;


// clasa ce retine datele despre un student
class Student {
public:
    Student();

    // constructor de copiere
    Student(const Student& other);

    // functii ce returneaza cate o anumita informatie despre student
    [[nodiscard]] string get_prenume()const{return prenume;}
    [[nodiscard]] string get_nume_de_familie()const{return nume_de_familie;}
    [[nodiscard]] string get_specializare() const{return specializare;}
    [[nodiscard]] int get_an() const{return an;}
    [[nodiscard]] float get_medie() const{return medie;}

    // functii de comparare folosite la sortarea studentilor
    // returneaza 'true' atunci cand este nevoie de o interschimbare, in contextul unei sortari crescatoare
    static bool compare_medie(Student*a, Student*b);
    static bool compare_nume(Student*a, Student*b);

    friend inline ostream& operator<<(ostream& os, Student& student);
    friend class CSVReader;

private:
    string prenume;
    string nume_de_familie;
    string specializare;
    int an;
    float medie;
};

// o supraincarcare a operatorului de deplasare (pentru ostream-uri), ce faciliteaza afisarea datelor studentului
ostream& operator<<(ostream& os, Student& student) {

    cout<<"Nume de familie: "<<student.nume_de_familie<<"\n";
    cout<<"Prenume: "<<student.prenume<<"\n";
    cout<<"Specializare: "<<student.specializare<<"\n";
    cout<<"An de studiu: "<<student.an<<"\n";
    cout<<"Medie: "<<student.medie<<"\n";

    return os;
}

#endif