#include<cstdlib>
#include<cstdio>
#include<iostream>
#include"Sorting.h"

// Functie ce citeste numerele din fisier.
// v = tabloul in care sunt memorate numerele
// n = numarul total de numere
void read_file(int *v, int *n) {
    FILE *input_file = fopen("input.txt", "r");
    int index = 0;
    int nr = 0;
    while (fscanf(input_file, "%d,", &nr) != EOF) { // NOLINT(*-err34-c)
        v[index] = nr;
        index++;
    }
    *n = index;
    fclose(input_file);
}

// functie ce afiseaza primele n numere dintr-un vector v
void print_array(const int* v, const int n) {
    printf("[");
    for (int i = 0; i < n-1; i++) {
        printf("%d, ", v[i]);
    }
    printf("%d]\n", v[n-1]);
}

// copiaza in tabloul vcopy elementele din tabloul v
inline void copy_array(const int* v, int *vcopy, const int n){
    for (int i = 0; i < n; i++)
        vcopy[i] = v[i];
}

int main() {
    int *v = (int*)malloc(sizeof(int)*1005); int n = 0;
    read_file(v, &n);

    int* vcopy = (int*)malloc(sizeof(int)*1005);

    printf("Tabloul initial:\n");
    print_array(v, n);

    printf("Bubble sort:\n");
    copy_array(v, vcopy, n);
    bubble_sort(vcopy, n);
    print_array(vcopy, n);

    printf("Selection sort:\n");
    copy_array(v, vcopy,n);
    selection_sort(vcopy, n);
    print_array(vcopy, n);

    printf("Quick sort:\n");
    copy_array(v, vcopy,n);
    quick_sort(vcopy, n);
    print_array(vcopy, n);

    free(v);free(vcopy);
    return 0;
}