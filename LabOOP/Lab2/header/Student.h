#ifndef LAB2_STUDENT_H
#define LAB2_STUDENT_H

#include <iostream>
#include <string>
#include <ostream>

class Student {
public:
    Student();
    Student(const Student& other);
    ~Student();

    string get_first_name();
    string get_last_name();
    string get_field();
    int get_study_year();
    float get_grade_average();

    friend ostream& operator<<(ostream& strm, const Student& student);
    friend class CSVReader;

private:
    string first_name;
    string last_name;
    string field;
    int study_year;
    float grade_average;
};

inline ostream& operator<<(ostream& os, const Student& student) {

    cout<<"Prenume: "<<student.first_name<<"\n";
    cout<<"Nume de familie: "<<student.first_name<<"\n";
    cout<<"Specializare: "<<student.first_name<<"\n";
    cout<<"An de studiu: "<<student.first_name<<"\n";
    cout<<"Medie: "<<student.first_name<<"\n";

    return os;
}

#endif