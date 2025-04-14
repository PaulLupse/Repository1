#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int Pow(a, n)
{
    if(n == 0) return 1;
    if(n % 2 == 1) return a * Pow(a , n - 1);
    int p = Pow(a , n / 2);
    return p * p;
}

int main()
{
    int n, k;
    int v[100] = {0};
    printf("n = ");
    scanf("%d", &n);
    printf("k = ");
    scanf("%d", &k);
    printf("v: ");
    for(int i = 0; i < n; i ++)
    {
        int nr;
        scanf("%d", &nr);
        v[i] = nr;
    }

    switch(k)
    {
        case 0:
            for(int i = 0; i < n; i ++) { v[i] ++; printf("%d ", v[i]);} break;
        case 1:
            for(int i = 0; i < n; i ++) { v[i] *= 2; printf("%d ", v[i]);}break;
        case 2:
            for(int i = 0; i < n; i ++) { v[i] /= 2; printf("%d ", v[i]);}break;
        case 3:
            for(int i = 0; i < n; i ++) { v[i] = Pow(v[i], 2); printf("%d ", v[i]);}break;
        case 4:
            for(int i = 0; i < n; i ++) { double a = sqrt(v[i]); printf("%.6lf ", a);}break;
    }

    return 0;
}
