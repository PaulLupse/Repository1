#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <math.h>

int Max(int a, int b)
{
    if(a > b)
        return a;
    else return b;
}

int cmmdc(int a, int b)
{
    return b == 0 ? a : cmmdc(b ,a % b);
}

int fib(n)
{
    unsigned long long int val0 = 0, val1 = 1, val2;
    while(n)
    {
        val2 = val1 + val0;
        printf("%d", val0);
        if(n - 1 == 0) printf(".");
        else printf(", ");
        val0 = val1;
        val1 = val2;
        n --;
    }
}


int main()
{
    int optiune = 0;
    while(1)
    {
        printf("1. Maximul dintre n numere.\n");
        printf("2. Cmmdc & cmmmc a n numere.\n");
        printf("3. Reprezentarea numarului n in baza b.\n");
        printf("4. Primele n numere din sirul Fibonacci.\n");
        printf("0. Iesire.\n");
        scanf("%d", &optiune);
        system("cls");
        if(optiune == 0)
            break;
        else if(optiune == 1)
        {
            printf("Maximul dintre n numere si frecventa acestuia.\n");
            printf("Introduceti numarul de numere: ");

            int n;
            int max;
            int nr;
            int frcv = 0;

            scanf("%d", &n);
            printf("Introduceti numerele: ");

            for(int i = 1; i <= n; i ++)
            {
                scanf("%d", &nr);
                if(max < nr)
                {
                    max = nr;
                    frcv = 1;
                }
                else if(max == nr)
                    frcv ++;
            }
            printf("Rezultat: %d, frecventa: %d\n", max, frcv);
        }
        else if(optiune == 2)
        {
            printf("Cel mai mare divizor comun si cel mai mic multiplu comun a doua numere.\n");
            printf("Introduceti numerele: ");

            int n;
            int m;

            scanf("%d", &n);
            scanf("%d", &m);

            int Cmmdc = cmmdc(n, m);
            int Cmmmc = n * m/cmmdc(n, m);

            printf("Cmmdc: %d\n", Cmmdc);
            printf("Cmmmc: %d\n", Cmmmc);
        }
        else if(optiune == 3)
        {
            printf("Scrierea in baza b al unui numar natural.\n");
            printf("Introduceti numarul: ");

            int n;
            int b;

            scanf("%d", &n);

            printf("Introduceti baza: ");

            scanf("%d", &b);

            int nr = 0, nrDig = 0;
            while(n > 0)
            {
                nrDig ++;
                nr = nr*10 + (n % b);
                n /= b;
            }

            printf("Rezultat: ");
            while(nr)
            {
                printf("%d", nr%10);
                nr /= 10;
                nrDig --;
            }
            while(nrDig)
            {
                printf("0");
                nrDig --;
            }
        }
        else
        {
            int n;
            printf("Primele n numere din sirul Fibonacci.\nIntroduceti numarul de numere: ");
            scanf("%d", &n);
            printf("Rezultat: ");
            fib(n);
        }
        printf("\nApasa orice tasta pentru a reveni la meniul principal.");
        _getch();
        system("cls");
    }

    return 0;
}
