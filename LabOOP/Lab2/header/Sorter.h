#ifndef LAB2_SORTER_H
#define LAB2_SORTER_H

#include <vector>
#include "student.h"
using namespace std;

// functie ce implementeaza quick sort pentru un vector de studenti, folosind functia precizata ca si comparator
void quick_sort(vector<Student>& v, int st, int dr, bool (*compare)(Student*, Student*));

// functie ce sorteaza primele n elemente din vectorul de studenti, folosind functia precizata ca si comparator
inline void sort_vector(vector<Student>& v,int n, bool (*compare)(Student*, Student*)) {
    quick_sort(v, 0, n-1, compare);
}

#endif