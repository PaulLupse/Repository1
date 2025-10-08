#include <cstdio>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void print_array(const int* v, int n) {
    printf("[");
    for (int i = 0; i < n-1; i++) {
        printf("%d, ", v[i]);
    }
    printf("%d]\n", v[n-1]);
}

void bubble_sort(int* v, int n) {

    bool sorted = false;
    while (!sorted) {
        sorted = true;
        for (int i = 0; i < n; i++) {
            if (v[i] > v[i + 1]) {
                sorted = false;
                swap(v + i, v + i + 1);
            }
        }
    }
}
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
void quick_sort(int*v, const int st, const int dr) {

    print_array(v, dr);
    if (st < dr) {
        int pivot = v[st];
        int i = st, j = dr;
        while (i < j) {
            printf("%d %d\n", i, j);
            while (i < j && v[i] < pivot) {
                i++;
            }
            while (i < j && v[j] > pivot) {
                j--;
            }
            if (v[i] >= v[j])
                swap(v+i, v+j);
        }
        quick_sort(v, st, i-1);
        quick_sort(v, i+1, dr-1);
    }
}