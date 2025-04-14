#include <stdio.h>
#include <stdlib.h>
#define N 100

int max(int a, int b){return a > b ? a : b;}
int min(int a, int b){return a < b ? a : b;}

void sum_right_neighbour(int v[N], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        v[i] += v[i+1];
    }
}

void sum_left_neighbour(int v[N], int n)
{
    for (int i = 1; i < n; i++)
    {
        v[i] += v[i-1];
    }
}

void elements_product_vector(int v[N], int n)
{
    int prod = 1;
    int prod_vector[N] = {0};
    for(int i = 0; i < n; i ++)
        prod *= v[i];

    for(int i = 0; i < n; i ++)
        prod_vector[i] = prod / v[i];
}

void print_vector(int v[N], int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", v[i]);
    }
    printf("\n");
}

void delete_element(int v[N], int n, int pos)
{
    for(int i = pos; i < n - 1; i ++)
        v[i] = v[i + 1];
    v[n - 1] = 0;
}

int main(void)
{
    int v[N] = {1, 2, 3, 4, 5};
    print_vector(v, 5);
    sum_right_neighbour(v, 5);
    print_vector(v, 5);

    int n = 5;
    while(1)
    {
        int optiune = 0;
        printf("1. Eliminare element minim.\n");
        printf("2. Eliminare element maxim.\n");
        printf("3. Printare vector.\n");
        printf("0. Iesire.\n");
        scanf("%d", &optiune);
        system("cls");
        if(optiune == 0)
            break;
        else if(optiune == 1)
        {
            int Min = v[0];
            for(int i = 0; i < n; i ++)
                Min = min(Min, v[i]);

            printf("Eliminare element minim.\nElementul minim: %d\n", Min);

            int cnt = 0;
            for(int i = 0; i < n; i ++)
                if(v[i] == Min)
                    {delete_element(v, n, i);
                    printf("a");
                    cnt ++;}
            n -= cnt;

            printf("Element minim eliminat.\n");
        }
        else if(optiune == 2)
        {
            int Max = v[0];
            for(int i = 0; i < n; i ++)
                Max = max(Max, v[i]);

            printf("Eliminare element maxim.\nElementul maxim: %d\n", Max);

            int cnt = 0;
            for(int i = 0; i < n; i ++)
                if(v[i] == Max)
                {
                    delete_element(v, n, i);
                    cnt ++;
                }
            n -= cnt;

            printf("Element maxim eliminat.\n");
        }
        else
        {
            print_vector(v, n);
        }
        printf("\nApasa orice tasta pentru a reveni la meniul principal.");
        _getch();
        system("cls");
    }

    return 0;
}
