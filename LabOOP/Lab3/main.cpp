#include "Student.h"
#include <iostream>
#include <string>
using namespace std;

int main() {

    TabStudenti ts("studenti.txt");
    cout<<"\nAm citit " << ts.getN() << " studenti:"<<'\n';
    ts.afiseaza();

    cout<<"\nQuickSort Studentii sortati alfabetic:"<<'\n';
    ts.sorteazaQ(Student::compNume);
    ts.afiseaza();

    cout<<"\nQuickSort Studentii sortati dupa medii:"<<'\n';
    ts.sorteazaQ(Student::compMedia);
    ts.afiseaza();

    cout<<"\nBubbleSort Studentii sortati alfabetic:"<<'\n';
    ts.sorteaza(Student::compNume);
    ts.afiseaza();

    cout<<"\nBubbleSort Studentii sortati dupa medii:"<<'\n';
    ts.sorteaza(Student::compMedia);
    ts.afiseaza();

    return 0;
}