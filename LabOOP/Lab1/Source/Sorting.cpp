
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/*
Functie care implementeaza algoritmul "bubble sort"
Verifica elementele de pe pozitii vecine, doua cate doua,
si le interschimba daca elementul cu index-ul mai mare este
mai mic decat elementul cu index-ul mai mic.
Este repetat acest rationament pana ce nu mai este nevoie de interschimbari.
*/
void bubble_sort(int* v, int n) {

    bool sorted = false;
    while (!sorted) {
        sorted = true;
        for (int i = 0; i < n-1; i++) {
            if (v[i] > v[i + 1]) {
                sorted = false;
                swap(v + i, v + i + 1);
            }
        }
    }
}

/*
Itereaza de n-1 ori prin tabloul de elemente,
incrementand pozitia de incepere de fiecare data.
La fiecare iteratie cauta elementul cu valoare minima,
si interschimba acest element cu elementul de la pozitia de incepere.
 */

void selection_sort(int* v, int n) {
    for (int i = 0; i < n-1; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (v[j] < v[min_index])
                min_index = j;
        }
        swap(v+min_index, v+i);
    }
}

void quick_sort(int*v, int st, int dr);

void quick_sort(int* v, int n) {
    quick_sort(v, 0, n-1);
}

/*
Partitioneaza vectorul in doua parti in functie de un pivot,
astfel incat partea din stanga contine doar elemente mai mici ca pivotul,
iar partea din dreapta contine elemente mai mari ca si pivotul.
Repeta, recursiv, acest rationament pentru fiecare parte, pana ce
partitiile sunt de marime mai mica decat 2.
*/

void quick_sort(int*v, const int st, const int dr) {

    if (st < dr) {
        int i = st, j = dr;
        swap(v +(st+dr)/2, v + st);
        int d = 0;
        while (i < j) {
            if (v[i] > v[j]) {
                swap(v+i, v+j);
                d = 1 - d;
            }
            i += 1-d;
            j -= d;
        }
        quick_sort(v, st, i-1);
        quick_sort(v, i, dr);
    }
}