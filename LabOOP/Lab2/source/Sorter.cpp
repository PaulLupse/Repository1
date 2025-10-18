#include "Sorter.h"

void quick_sort(vector<Student>& v, const int st, const int dr, bool (*compare)(Student*, Student*)) {
    if (st < dr) {
        int i = st, j = dr;
        int d = 0;
        while (i < j) {
            if (compare(&(v[i]), &(v[j]))) {
                swap(v[i], v[j]);
                d = 1 - d;
            }
            i += 1-d;
            j -= d;
        }
        quick_sort(v, st, i-1, compare);
        quick_sort(v, i, dr, compare);
    }
}

