#ifndef LAB3_STUDENT_H
#define LAB3_STUDENT_H

#include <string>
#include <iostream>

using namespace std;

// clasa ce memoreaza datele despre un student
class Student{

protected:
    string nume_complet, spec;
    int an;
    float media;

public:

    // constructor default
    Student():
        an(0),
        media(0.0f){};

    Student(const string& _nume_complet, const string& _specializare,const int& _an, const float& _media):
        nume_complet(_nume_complet),
        spec(_specializare),
        an(_an),
        media(_media){};

    Student(const Student& other):
        nume_complet(other.nume_complet),
        spec(other.spec),
        an(other.an),
        media(other.media){};

    Student(const Student* other):
        nume_complet(other->nume_complet),
        spec(other->spec),
        an(other->an),
        media(other->media){};


    string get_nume_complet() const {
        return nume_complet;
    }

    bool operator==(const Student&) const;

    static bool compNume(Student *, Student *);
    static bool compMedia(Student *, Student *);

    virtual void afiseaza();
    friend class TabStudenti;
    friend class ListaStudenti;
    template<typename tip>
    friend class ListaStudentiOrdonata;
    friend class Nod;

    friend inline ostream& operator<<(ostream&, const Student&);
    friend ostream& operator<<(ostream&, Student*);
};

class StudentCNP:public Student {
protected:
    string cnp;
public:
    StudentCNP():Student(){}
    StudentCNP(const string& _nume_complet, const string& _specializare,const int& _an, const float& _media, const string& _cnp):
        Student(_nume_complet, _specializare, _an, _media),cnp(_cnp){}
    StudentCNP(const StudentCNP& other):Student(other),cnp(other.cnp){}

    StudentCNP(const StudentCNP* other):Student(other),cnp(other->cnp){}

    bool operator==(const StudentCNP&) const;
    virtual void afiseaza();


    static bool compNume(StudentCNP *, StudentCNP *);
    static bool compMedia(StudentCNP *, StudentCNP *);

    friend class TabStudenti;
    friend class ListaStudenti;
    template<typename tip>
    friend class ListaStudentiOrdonata;
    friend class Nod;

    friend inline ostream& operator<<(ostream& out_stream, const StudentCNP& student);
    friend ostream& operator<<(ostream& out_stream, StudentCNP* student);
};

#endif //LAB3_STUDENT_H