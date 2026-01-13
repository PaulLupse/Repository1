#include "Student.h"
#include "ListaStudenti.h"
#include <iostream>
#include <Windows.h>
using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);

    auto *ls1 = new ListaStudentiOrdonata<Student>("studenti1.txt",&Student::compMedia);

    cout<<*ls1;

    delete ls1;
    return 0;
}