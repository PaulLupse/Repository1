#include <stdio.h>
#include <stdlib.h>

void rotire_stanga(int v[100], int n, int k)
{
    k = k % n;
    int v_rotit[100] = {0};
    for(int i = k, j = 0; i < n; i ++, j ++)
        v_rotit[j] = v[i];
    for(int i = 0, j = n - k; i < k; i ++, j ++)
        v_rotit[j] = v[i];
    for(int i = 0; i < n; i ++)
        printf("%d ", v_rotit[i]);
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

    rotire_stanga(v, n, k);

    return 0;
}
