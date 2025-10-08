#include<cstdlib>
#include<cstdio>
#include<iostream>
#include "Sorting.h"

// V = tabloul in care sunt memorate numerele
// n = numarul total de numere
void read_file(int *(*v), int *n) {
    FILE *input_file = fopen("input.txt", "r");

    *v = (int*)malloc(sizeof(int) * 1005);
    int index = 0;
    while (fscanf(input_file, "%d,", *v + index) != EOF) { // NOLINT(*-err34-c)
        index++;
    }
    *n = index;
    fclose(input_file);
}

int main() {
    int *v = nullptr; int n = 0;
    read_file(&v, &n);

    quick_sort(v, n);
    print_array(v, n);

    free(v);
    return 0;
}