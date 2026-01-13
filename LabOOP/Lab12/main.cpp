#include "Student.h"
#include "ListaStudenti.h"
#include <iostream>
#include <Windows.h>
#include "TipuriDeDate.h"
using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);

    ListaStudentiOrdonata<Student> ls;

    ListaStudentiOrdonata<Int> li;

    ListaStudentiOrdonata<Float> lf;



    ls.adauga(new StudentCNP("Pop Ion", "Info", 2, 8.50f, "1234567890123"));

    ls.adauga(new  StudentCNP("Avram Vasile", "Info", 3, 9.10f, "2345678901234"));

    ls.adauga(new StudentCNP("Dumitru Ana", "Mate", 1, 7.80f, "3456789012345"));



    li.adauga(new Int(10));

    li.adauga(new Int(20));

    li.adauga(new Int(15));





    lf.adauga(new Float(3.1415));

    lf.adauga(new Float(12.345));

    lf.adauga(new Float(1.2));



    cout<<ls;

    cout<<lf;

    cout<<li;
}