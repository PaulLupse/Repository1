#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct _string{
    char value[105];
};

int triunghi(int matrice[][105],int n, int pos, int elemente[])
{

    int index_elemente = 0;
    if(pos == 1)
    {
        for(int i = 0; i <= n / 2 - 1 - (n % 2 == 0); i ++)
        {
            for(int j = i + 1; j < n - i - 1; j ++)
            {
                elemente[index_elemente++] = matrice[i][j];
                //printf("i: %d, j: %d, m: %d\n", i, j, matrice[i][j]);
            }
            //printf("\n");
        }
    }
    else if(pos == 2)
    {
        for(int i = n / 2 + 1; i < n; i ++)
        {
            for(int j = n - i; j < i; j ++)
            {
                elemente[index_elemente++] = matrice[i][j];
                //printf("i: %d, j: %d, m: %d\n", i, j, matrice[i][j]);
            }
            //printf("\n");
        }
    }
    else if(pos == 3)
    {
        for(int i = 0; i <= n / 2 - 1 - (n % 2 == 0); i ++)
        {
            for(int j = i + 1; j < n - i - 1; j ++)
            {
                elemente[index_elemente++] = matrice[j][i];
                //printf("i: %d, j: %d, m: %d\n", i, j, matrice[j][i]);
            }
            //printf("\n");
        }
    }
    else
    {
        for(int i = n / 2 + 1; i < n; i ++)
        {
            for(int j = n - i; j < i; j ++)
            {
                elemente[index_elemente++] = matrice[j][i];
                //printf("i: %d, j: %d, m: %d\n", i, j, matrice[j][i]);
            }
            //printf("\n");
        }
    }
    return index_elemente;
}

int zig_zag(int matrice[][105], int n, int elemente[])
{
    int index_elemente = 0;
    for(int i = 0; i < n; i ++)
    {
        if(i % 2 == 0)
        {
            for(int j = 0; j <= i; j ++)
            {
                //printf("i: %d, j: %d, m: %d\n", i-j, j, matrice[i-j][j]);
                elemente[index_elemente ++] = matrice[i-j][j];
            }
        }
        else
        {
            for(int j = i; j >= 0; j --)
            {
                //printf("i: %d, j: %d, m: %d\n", i-j, j, matrice[i-j][j]);
                elemente[index_elemente ++] = matrice[i-j][j];
            }
        }
    }
    for(int i = 0; i < n; i ++)
    {
        if(i % 2 != n % 2)
        {
            for(int j = n - 1; j > i; j --)
            {
                //printf("i: %d, j: %d, m: %d\n", i + (n - j), j, matrice[i + (n - j)][j]);
                elemente[index_elemente ++] = matrice[i + (n - j)][j];
            }
        }
        else
        {
            for(int j = i + 1; j < n; j ++)
            {
                //printf("i: %d, j: %d, m: %d\n", i + (n - j), j, matrice[i + (n - j)][j]);
                elemente[index_elemente ++] = matrice[i + (n - j)][j];
            }
        }
    }
    return index_elemente;
}

int spirala(int matrice[][105], int n, int elemente[])
{
    int margine_stanga = 0, margine_dreapta = 0, margine_sus = 0, margine_jos = 0;
    int index_elemente = 0;
    int i = 0, j = 0;
    int parcurgere = 0;
    while(index_elemente < n*n)
    {
        while(j < (n - margine_dreapta) && index_elemente < n*n)
        {
            elemente[index_elemente++] = matrice[i][j];
            j ++;
        }
        j--;
        margine_sus ++;
        i = margine_sus;
        while(i < (n - margine_jos) && index_elemente < n*n)
        {
            elemente[index_elemente++] = matrice[i][j];
            i ++;
        }
        i--;
        margine_dreapta ++;
        j = n - margine_dreapta - 1;
        while(j >= margine_stanga && index_elemente < n*n)
        {
            elemente[index_elemente++] = matrice[i][j];
            j --;
        }
        j++;
        margine_jos ++;
        i = n - margine_jos - 1;
        while(i >= margine_sus && index_elemente < n*n)
        {
            elemente[index_elemente++] = matrice[i][j];
            i --;
        }
        i ++;
        j = margine_stanga + 1;
        margine_stanga ++;
    }
}

void citire_matrice(int matrice[][105], int *n)
{
    scanf("%d", n);
    for(int i = 0; i < *n; i ++)
        for(int j = 0; j < *n; j ++)
            scanf("%d", &matrice[i][j]);
}

int main()
{
    // matrice exemplu
    /*int M[105][105] = { {1,  2,  3,  4,  5, 0},
                        {6,  7,  8,  9,  10, 0},
                        {11, 12, 13, 14, 15, 0},
                        {16, 17, 18, 19, 20, 0},
                        {21, 22, 23, 24, 25, 0},
                        {26, 27, 28, 29, 30, 0}};*/

    int matrice[105][105] = {0}, dimensiune_matrice = 0;
    citire_matrice(matrice, &dimensiune_matrice);

    // 1 == triunghiul superior
    // 2 == tringhiul inferior
    // 3 == triunghiul din stanga
    // 4 == triunghiul din dreapta

    struct _string denumire_triunghiuri[5];
    strcpy(denumire_triunghiuri[0].value, "Superior");
    strcpy(denumire_triunghiuri[1].value, "Inferior");
    strcpy(denumire_triunghiuri[2].value, "Dreapta");
    strcpy(denumire_triunghiuri[3].value, "Stanga");

    printf("Triunghiurile:\n");
    for(int k = 1; k <= 4; k ++)
    {
        printf("%d. %s: ",k, denumire_triunghiuri[k - 1].value);
        int elemente[105] = {0};
        int lungime_vector_elemente = triunghi(matrice, dimensiune_matrice, k, elemente);
        for(int i = 0; i < lungime_vector_elemente; i ++)
        {
            printf("%d ", elemente[i]);
        }
        printf("\n");
    }

    printf("Elementele zig-zag:\n");

    int elemente_zig_zag[105] = {0};
    int lungime_vector_elemente = zig_zag(matrice, dimensiune_matrice, elemente_zig_zag);
    for(int i = 0; i < lungime_vector_elemente; i ++)
        {
            printf("%d ", elemente_zig_zag[i]);
        }

    printf("\n");

    printf("Elementele in spirala:\n");

    int elemente_spirala[105] = {0};
    lungime_vector_elemente = spirala(matrice, dimensiune_matrice, elemente_spirala);
    for(int i = 0; i < lungime_vector_elemente; i ++)
        {
            printf("%d ", elemente_spirala[i]);
        }

    return 0;
}
